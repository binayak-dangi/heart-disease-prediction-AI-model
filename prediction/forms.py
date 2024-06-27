from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import RegisterDetail

class UserRegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
    full_name = forms.CharField(label='Full Name', max_length=50)
    mobile_number = forms.CharField(label='Mobile Number', max_length=15)
    email = forms.EmailField(label='Email', max_length=75)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=100)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, max_length=100)
    gender = forms.CharField(label='Gender', max_length=6)
    age = forms.IntegerField(label='Age')
    weight = forms.FloatField(label='Weight')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError("Passwords do not match")

        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if RegisterDetail.objects.filter(email=email).exists():  # Correct field name
            raise ValidationError("Email is already in use")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if RegisterDetail.objects.filter(username=username).exists():  # Correct field name
            raise ValidationError("Username is already in use")
        return username


# for prediction
class PredictionForm(forms.Form):
    age = forms.IntegerField(label='Age')
    sex = forms.ChoiceField(choices=[(0, 'Female'), (1, 'Male')], label='Sex')
    cp = forms.ChoiceField(choices=[(0, 'Typical Angina'), (1, 'Atypical Angina'), (2, 'Non-Anginal Pain'), (3, 'Asymptomatic')], label='Chest Pain Type')
    trestbps = forms.IntegerField(label='Resting Blood Pressure')
    chol = forms.IntegerField(label='Serum Cholesterol (mg/dl)')
    fbs = forms.ChoiceField(choices=[(0, 'Less than 120 mg/dl'), (1, 'Greater than 120 mg/dl')], label='Fasting Blood Sugar > 120 mg/dl')
    restecg = forms.ChoiceField(choices=[(0, 'Normal'), (1, 'ST-T wave abnormality'), (2, 'Left ventricular hypertrophy')], label='Resting Electrocardiographic Results')
    thalach = forms.IntegerField(label='Maximum Heart Rate Achieved')
    exang = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')], label='Exercise Induced Angina')
    oldpeak = forms.FloatField(label='ST Depression Induced by Exercise Relative to Rest')
    slope = forms.ChoiceField(choices=[(0, 'Upsloping'), (1, 'Flat'), (2, 'Downsloping')], label='Slope of the Peak Exercise ST Segment')
    ca = forms.ChoiceField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')], label='Number of Major Vessels Colored by Flouroscopy')
    thal = forms.ChoiceField(choices=[(0, 'Normal'), (1, 'Fixed Defect'), (2, 'Reversible Defect')], label='Thallium Heart Scan Results')


# for login
class User(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

