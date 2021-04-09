from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email =  forms.EmailField(label="Qual é o seu email?",widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':"Insira seu email",}))
    first_name = forms.CharField(max_length=255, label="Qual é o seu nome?", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Insira seu nome", }))
    last_name = forms.CharField(max_length=255, label="Qual é o seu sobrenome?", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Insira seu sobrenome",}))

    class Meta:
      model = User
      fields = ('first_name', 'last_name', 'username',  'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
      super(SignUpForm, self).__init__(*args, **kwargs)

      self.fields['username'].widget.attrs['class'] = 'form-control'
      self.fields['username'].widget.attrs['placeholder'] = 'Insira seu CPF | Apenas números'
      self.fields['username'].label = 'Qual é o seu CPF?'

      self.fields['password1'].widget.attrs['class'] = 'form-control'
      self.fields['password1'].label = 'Qual senha você quer?'
      self.fields['password1'].widget.attrs['placeholder'] = 'Insira sua senha '

      self.fields['password2'].widget.attrs['class'] = 'form-control'
      self.fields['password2'].label = 'Confirme sua senha'
      self.fields['password2'].widget.attrs['placeholder'] = 'Confirme a sua senha'
