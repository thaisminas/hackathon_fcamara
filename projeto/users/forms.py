from django.contrib.auth import forms
from django.forms import ModelForm 
from django import forms as forms_
from .models import User


class UserChangeForm(forms.UserChangeForm):
  class Meta(forms.UserChangeForm.Meta):
    model = User
 

class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User


class UserModelForm(forms_.ModelForm):
  class Meta:
    model = User
    fields = 'username',
