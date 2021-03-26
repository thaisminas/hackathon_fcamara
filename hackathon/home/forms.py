from django import forms
from .models import Post, Category, User

#choices = [('coding', 'coding'),('sports', 'sports'), ('random', 'random')]
choices = Category.objects.all().values_list('name', 'name')
choice_list = []

for i in choices:
  choice_list.append(i) 


class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'body', 'category', 'author')
    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control'}),
      'body': forms.Textarea(attrs={'class': 'form-control'}),
      'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
      'author': forms.Select(attrs={'class': 'form-control'}),
    }


class EditForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('body', 'title')
    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-cont rol'}),
      'body': forms.Textarea(attrs={'class': 'form-control'}),
      'category': forms.Select(attrs={'class': 'form-control'}),
    }