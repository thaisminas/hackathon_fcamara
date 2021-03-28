from django import forms
from .models import Donate, School, Grade, Student, DonationType

class DonateForm(forms.ModelForm):
  class Meta:
    model = Donate
    fields = ('student', 'author', 'donation_type', 'message', 'anon')
    widgets = {
      'student': forms.Select(attrs={'class': 'form-select'}),
      'author': forms.Select(attrs={'class': 'form-select'}),
      'donation_type': forms.Select(attrs={'class': 'form-select'}),
      'message': forms.Textarea(attrs={'class': 'form-control'}),
      'anon': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    }

class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ('name', 'cpf', 'birth_date', 'grade', 'school')
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control'}),
      'cpf': forms.TextInput(attrs={'class': 'form-control'}),
      'birth_date': forms.DateInput(attrs={'class': 'form-control'}),
      'grade': forms.Select(attrs={'class': 'form-select'}),
      'school': forms.Select(attrs={'class': 'form-select'}),
    }
