from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Donate, Student
from .forms import DonateForm, StudentForm

# def home(request):
#  return render(request, 'home.html', {})

class HomeView(ListView):
  model = Donate
  template_name = 'home.html'
  ordering = ['-created_at']


class LandingView(ListView):
  model = Donate
  template_name = 'landing.html'


class AddStudentView(CreateView):
  model = Donate
  template_name = 'add_student.html'
  form_class = StudentForm


class AddDonateView(CreateView):
  model = Donate
  template_name = 'add_donate.html'
  form_class = DonateForm

class StudentView(ListView):
  model = Student
  template_name = 'student.html'