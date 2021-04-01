from django import forms
from .models import Donate, School, Grade, Student, DonationType, Profile, ItemSelection

class DonateForm(forms.ModelForm):
  class Meta:
    model = Donate
    fields = ('student', 'author', 'donation_type', 'message', 'anon')
    labels = {'donation_type': 'Tipo da Doação', 'message': 'Mensagem', 'anon': 'Deseja realizar essa doação de forma anônima' }
    widgets = {
      'student': forms.TextInput(attrs={'class': 'form-control', 'id': 'dStudent', 'type': 'hidden'}),
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
    labels = {'name': 'Nome do Aluno', 'school': 'Escola', 'cpf': 'CPF', 'birth_date': 'Data de Nascimento', 'grade': 'Série', 'profile_pic': 'Foto do Aluno', 'registration_pic': 'Comprovante de Matrícula' }
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
    fields = ('user', 'profile_type', 'cep', 'estado', 'cidade', 'rua', 'bairro', 'numero')
    labels = {'profile_type': 'Tipo de Usuário', 'cep': 'CEP', 'numero': 'Número'}
    widgets = {
      'cep': forms.TextInput(attrs={'class': 'form-control', 'id': 'cep'}),
      'rua': forms.TextInput(attrs={'class': 'form-control', 'id': 'logradouro'}),
      'numero': forms.TextInput(attrs={'class': 'form-control', 'id': 'numero'}),
      'bairro': forms.TextInput(attrs={'class': 'form-control', 'id': 'bairro'}),
      'estado': forms.TextInput(attrs={'class': 'form-control', 'id': 'uf'}),
      'cidade': forms.TextInput(attrs={'class': 'form-control', 'id': 'cidade'}),
      'user': forms.TextInput(attrs={'class': 'form-control', 'id': 'pUser', 'type': 'hidden'}),
      'profile_type': forms.Select(attrs={'class': 'form-select'}),
    }


class ListFormSet(forms.ModelForm):
  class Meta:
    model = ItemSelection
    fields = ('student', 'item', 'item_quantity')
    labels = {'item_quantity': 'Quantidade'}
    widgets = {
      'student': forms.TextInput(attrs={'class': 'form-control', 'id': 'dStudent', 'type': 'hidden'}),
      'item': forms.Select(attrs={'class': 'form-control', 'id': 'item', 'type': 'hidden'}),
      'item_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
    }


class DeliverForm(forms.ModelForm):
  class Meta:
    model = Donate
    fields = ('notify', )
    labels = {'notify': 'Confirmar'}
    widgets = {
      'notify': forms.CheckboxInput(attrs={'class': 'btn btn-secondary'})
    }


class ColectForm(forms.ModelForm):
  class Meta:
    model = Donate
    fields = ('closed', )
    labels = {'closed': 'Confirmar'}
    widgets = {
      'closed': forms.CheckboxInput(attrs={'class': 'btn btn-secondary'})
    }
