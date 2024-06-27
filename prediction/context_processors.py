# your_app/context_processors.py
from .models import RegisterDetail

def user_detail(request):
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = RegisterDetail.objects.get(id=user_id)
        except RegisterDetail.DoesNotExist:
            user = None
    else:
        user = None
    return {'custom_user': user}
