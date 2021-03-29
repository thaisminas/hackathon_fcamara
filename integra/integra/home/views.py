from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Donate, Student, School, Profile
from .forms import DonateForm, StudentForm, ProfileForm
from django.urls import reverse_lazy

# def home(request):
#  return render(request, 'home.html', {})

class HomeView(ListView):
  model = Donate
  template_name = 'home.html'
  ordering = ['-created_at']


class MyDonationsView(ListView):
  model = Donate
  template_name = 'my_donations.html'
  ordering = ['-created_at']


class DonatedView(ListView):
  model = Donate
  template_name = 'donated.html'
  ordering = ['-created_at']


def SchoolView(request, schl):
  students = Student.objects.filter(school=schl.replace('-',' '))
  return render(request, 'school.html', {'schl':schl.replace('-',' '), 'students': students})


def LocalSchoolView(request, stt, city):
  schools = School.objects.filter(state=stt, city = city.replace('-',' '))
  return render(request, 'local_school.html', {'stt':stt, 'city': city.replace('-',' '), 'schools': schools})


class LandingView(ListView):
  model = Donate
  template_name = 'landing.html'


class AddStudentView(CreateView):
  model = Donate
  template_name = 'add_student.html'
  form_class = StudentForm
  success_url = reverse_lazy('student')


class AddDonateView(CreateView):
  model = Donate
  template_name = 'add_donate.html'
  form_class = DonateForm

class StudentView(ListView):
  model = Student
  template_name = 'student.html'


class ProfileRegisterView(CreateView):
  model = Profile
  template_name = 'profile_register.html'
  form_class = ProfileForm
  success_url = reverse_lazy('home')