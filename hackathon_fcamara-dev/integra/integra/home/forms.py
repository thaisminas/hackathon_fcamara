from django import forms
from .models import Donate, School, Grade, Student, DonationType, Profile, ItemSelection
from integra import settings

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
    labels = {'name': 'Qual o nome da sua criança?', 'school': 'Qual é a esscola da sua criaça?', 'cpf': 'Qual é o CPF da sua criança?', 'birth_date': 'Qual a data de nascimento da sua criança nasceu?', 'grade': 'Em qual série a sua criança está?', 'profile_pic': 'Selecione uma foto da sua criança', 'registration_pic': 'Selecione um registro de matrículas' }
    
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o nome do aluno'}),
      'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'owner', 'type': 'hidden'}),
      'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o CPF do aluno'}),
      'birth_date': forms.DateInput(attrs={'class': 'form-control', 'id': 'data', 'placeholder': 'Insira a data de nascimento do aluno'}),
      'grade': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Selecione a série do aluno'}),
      'school': forms.Select(attrs={ 'class': 'form-select', 'placeholder': 'Selecione o nome do aluno'}),
    }


class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ('user', 'profile_type', 'cep', 'estado', 'cidade', 'rua', 'bairro', 'numero')
    labels = {'profile_type': 'Você é doador ou Responável?', 'cep': 'Qual é o seu CEP?','numero': 'Qual complemento da sua casa?', 'estado': 'Qual é o seu Estado?', 'bairro': 'Qual é o nome do seu bairro?', 'cidade': 'Qual é o nome da sua cidade?', 'rua': 'Qual é o nome da sua rua?'}
    widgets = {
      'cep': forms.TextInput(attrs={'class': 'form-control', 'id': 'cep', 'placeholder':'Insira seu CEP'}),
      'rua': forms.TextInput(attrs={'class': 'form-control', 'id': 'logradouro' , 'placeholder':'Insira sua rua'}),
      'numero': forms.TextInput(attrs={'class': 'form-control', 'id': 'numero', 'placeholder':'Insira o complemento'}),
      'bairro': forms.TextInput(attrs={'class': 'form-control', 'id': 'bairro', 'placeholder':'Insira seu bairro'}),
      'estado': forms.TextInput(attrs={'class': 'form-control', 'id': 'uf', 'placeholder':'Insira seu estado'}),
      'cidade': forms.TextInput(attrs={'class': 'form-control', 'id': 'cidade', 'placeholder':'Insira sua cidade'}),
      'user': forms.TextInput(attrs={'class': 'form-control', 'id': 'pUser', 'type': 'hidden'}),
      'profile_type': forms.Select(attrs={'class': 'form-select', 'placeholder':'Selecione se é Responsável ou Doador'}),
    }


class ListFormSet(forms.ModelForm):
  item = forms.CharField(disabled=True)
  class Meta:
    model = ItemSelection
    fields = ('student', 'item', 'item_quantity')
    labels = {'item_quantity': 'Quantidade'}
    widgets = {
      'student': forms.TextInput(attrs={'class': 'form-control', 'id': 'dStudent', 'type': 'hidden'}),
      'item': forms.TextInput(attrs={'class': 'btn btn-outline-primary', 'id': 'item', 'type': 'hidden'}),
      'item_quantity': forms.NumberInput(attrs={'class': 'btn btn-outline-primary'}),
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


class PayForm(forms.ModelForm):
  class Meta:
    model = Donate
    fields = ('closed', 'notify')
    labels = {'closed': 'Confirmar'}
    widgets = { 
      'closed': forms.CheckboxInput(attrs={'class': 'btn btn-secondary'}),
      'notify': forms.CheckboxInput(attrs={'class': 'btn btn-secondary', 'name': 'foo', 'type': 'hidden'})
    }


class UpdateItemSelectionForm(forms.ModelForm):
  class Meta:
    model = ItemSelection
    fields = ('item_quantity', 'item')
    labels = {'item_quantity': 'Quantidade do item'}
    widgets = { 
      'item_quantity': forms.NumberInput(attrs={'class': 'btn btn-outline-primary'}),
      'item': forms.TextInput(attrs={'class': 'form-control', 'id': 'item', 'type': 'hidden'}),
    }


class AddItemForm(forms.ModelForm):
  class Meta:
    model = ItemSelection
    fields = ('student', 'item', 'item_quantity')
    labels = {'item_quantity': 'Quantidade do item'}
    widgets = { 
      'student': forms.TextInput(attrs={'class': 'form-control', 'id': 'dStudent', 'type': 'hidden'}),
      'item_quantity': forms.NumberInput(attrs={'class': 'btn btn-outline-primary'}),
      'item': forms.Select(attrs={'class': 'form-control', 'id': 'item'}),
    }

