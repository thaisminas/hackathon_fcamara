from django.db import models
from django.urls import reverse
from datetime import datetime, date
from users.models import User

class Category(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name

  def get_absolute_url(self): 
    return reverse('home')


class Post(models.Model):
  title = models.CharField(max_length=255)
  body = models.TextField()
  created_at = models.DateField(auto_now_add=True)
  category = models.CharField(max_length=255, default="coding")
  author = models.ForeignKey(User, default="1", on_delete=models.CASCADE)

  def __str__(self):
    return self.title 

  def get_absolute_url(self): 
    return reverse('home') 