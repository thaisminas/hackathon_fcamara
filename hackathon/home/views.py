from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm

# def home(request):
#   return render(request, 'home.html')

class HomeView(ListView):
  model = Post
  template_name = 'home.html'


class ArticleDetailView(DetailView):
  model = Post
  template_name = 'article_details.html'


class AddPostView(CreateView):
  model = Post
  form_class= PostForm
  template_name = 'add_post.html'


class UpdatePostView(CreateView):
  model = Post
  template_name = 'update_post.html'
  fields = ['title', 'body']