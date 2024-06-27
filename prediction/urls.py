# prediction/urls.py

from django.urls import path
from django.views.generic import RedirectView

from .views import *

urlpatterns = [
    path('', RedirectView.as_view(url='login/', permanent=False)),  # Redirect to login page, adjust as needed
    # Add other URL patterns specific to your app
    path('register/',register, name='register'),
    path('login/', user_login, name='login'),
    path('predict/',predict, name='predict'),
    path('user_logout/',user_logout,name='user_logout')
    # Add more URL patterns as necessary
]

from django.conf import settings 
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

  