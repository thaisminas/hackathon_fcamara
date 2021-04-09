from django.urls import path
from .views import UserRegisterView
from home.views import ProfileRegisterView

urlpatterns = [
  path('register/', UserRegisterView.as_view(), name='register'), 
  #path('profile_register/', ProfileRegisterView.as_view, name='profile_register')
]
