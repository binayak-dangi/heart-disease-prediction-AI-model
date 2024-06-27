from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import UserRegistrationForm, PredictionForm,User
from .models import RegisterDetail
import joblib
import os
import numpy as np
from .decorators import custom_login_required

# Get the directory of the current file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the model.pkl file
model_path = os.path.join(BASE_DIR, 'model.pkl')

# Load the model
model = joblib.load(model_path)

@custom_login_required
def predict(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            data = np.array([
                form.cleaned_data['age'],
                form.cleaned_data['sex'],
                form.cleaned_data['cp'],
                form.cleaned_data['trestbps'],
                form.cleaned_data['chol'],
                form.cleaned_data['fbs'],
                form.cleaned_data['restecg'],
                form.cleaned_data['thalach'],
                form.cleaned_data['exang'],
                form.cleaned_data['oldpeak'],
                form.cleaned_data['slope'],
                form.cleaned_data['ca'],
                form.cleaned_data['thal']
            ]).reshape(1, -1)
            prediction = model.predict(data)
            result = 'Positive' if prediction[0] == 1 else 'Negative'
            return render(request, 'prediction/result.html', {'result': result})
    else:
        form = PredictionForm()
    return render(request, 'prediction/predict.html', {'form': form})




from django.contrib.auth.hashers import make_password
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            full_name = form.cleaned_data.get('full_name')
            mobile_number = form.cleaned_data.get('mobile_number')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            # Hash the password
            hashed_password = make_password(password)

            gender = form.cleaned_data.get('gender')
            age = form.cleaned_data.get('age')
            weight = form.cleaned_data.get('weight')

            # Create the user profile
            RegisterDetail.objects.create(
                username=username,       # Correct field name
                full_name=full_name,     # Correct field name
                mobile_number=mobile_number, # Correct field name
                email=email,             # Correct field name
                password=hashed_password,       # Correct field name
                gender=gender,           # Correct field name
                age=age,                 # Correct field name
                weight=weight            # Correct field name
            )
            messages.add_message(request,messages.SUCCESS,'user account created successfully')
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'prediction/register.html', {'form': form})

# login
def user_login(request):
    if request.method == 'POST':
        form = User(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            try:
                user = RegisterDetail.objects.get(username=username)
            except RegisterDetail.DoesNotExist:
                messages.add_message(request,messages.ERROR,'Invalid username or password.')
                return render(request, 'prediction/login.html', {'form': form})
            
            if check_password(password, user.password):
                # Assuming you want to manually log in the user
                # Note: This does not use Django's session framework, you can set your own session management here
                request.session['user_id'] = user.id
                return redirect('/predict')  # Redirect to home page or dashboard
            else:
                messages.add_message(request,messages.ERROR,'Invalid username or password.')
                
    else:
        form = User()
    
    return render(request, 'prediction/login.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def predict_view(request):
    return render(request, 'prediction/predict.html')

def user_logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('/login') 