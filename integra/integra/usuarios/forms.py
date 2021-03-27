from django import forms
from .models import Usuario


class UsuarioForm(forms.ModelForm):
    name = forms.CharField(

    )


