from django import forms
from .models import Donate, School, Grade, Student, DonationType, Profile

class DonateForm(forms.ModelForm):
  class Meta:
    model = Donate
    fields = ('student', 'author', 'donation_type', 'message', 'anon')
    widgets = {
      'student': forms.TextInput(attrs={'class': 'form-control', 'id': 'dStudent'}),
      'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'donator', 'type': 'hidden'}),
      'donation_type': forms.Select(attrs={'class': 'form-select'}),
      'message': forms.Textarea(attrs={'class': 'form-control'}),
      'anon': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    }


choices = School.objects.all().values_list('name', 'name')
choice_list = []

for i in choices:
  choice_list.append(i)


class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ('name', 'cpf', 'birth_date', 'grade', 'school', 'author', 'profile_pic', 'registration_pic')
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control'}),
      'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'owner', 'type': 'hidden'}),
      'cpf': forms.TextInput(attrs={'class': 'form-control'}),
      'birth_date': forms.DateInput(attrs={'class': 'form-control'}),
      'grade': forms.Select(attrs={'class': 'form-select'}),
      'school': forms.Select(choices=choice_list, attrs={ 'class': 'form-select'}),
    }

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ('cpf', 'user', 'profile_type')
    widgets = {
      'user': forms.TextInput(attrs={'class': 'form-control', 'id': 'pUser', 'type': 'hidden'}),
      'cpf': forms.TextInput(attrs={'class': 'form-control'}),
      'profile_type': forms.Select(attrs={'class': 'form-select'}),
    }
