from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# def home(request):
#   return render(request, 'home.html')

class HomeView(ListView):
  model = Post
  template_name = 'home.html'
  ordering = ['-created_at']

  def get_context_data(self, *args, **kwargs):
    cat_menu = Category.objects.all()
    context = super(HomeView, self).get_context_data(*args, **kwargs)
    context['cat_menu'] = cat_menu
    return context


def CategoryView(request, cats):
  category_post = Post.objects.filter(category=cats.replace('-',' '))
  return render(request, 'categories.html', {'cats':cats.title().replace('-',' '), 'category_post':category_post })


class ArticleDetailView(DetailView):
  model = Post
  template_name = 'article_details.html'


class AddPostView(CreateView):
  model = Post
  form_class= PostForm
  template_name = 'add_post.html'


class UpdatePostView(CreateView):
  model = Post
  form_class= PostForm
  template_name = 'update_post.html'
  # fields = ['title', 'body']


class DeletePostView(DeleteView):
  model = Post
  form_class= EditForm
  template_name = 'delete_post.html'
  success_url = reverse_lazy('home')