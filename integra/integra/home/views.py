from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Donate, Student, School, Profile, ItemSelection, StudentList, Item
from .forms import DonateForm, StudentForm, ProfileForm, ListFormSet, DeliverForm, ColectForm
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django import forms
import operator

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
  success_url = reverse_lazy('my_donations')

  def get_context_data(self, **kwargs):
      context = super(AddDonateView, self).get_context_data(**kwargs)
      students = Student.objects.all()

      context['pk'] = self.kwargs['pk']
      context['students'] = students

      return context


class StudentView(ListView):
  model = Student
  template_name = 'student.html'


  # def get_context_data(self, **kwargs):
    #lists = List.objects.all()

    #context = super(StudentView, self).get_context_data(**kwargs)
    #context['lists'] = lists

    #return context


class ProfileRegisterView(CreateView):
  model = Profile
  template_name = 'profile_register.html'
  form_class = ProfileForm
  success_url = reverse_lazy('home')


def Createlist(request, pk):
  ListFormSet = inlineformset_factory(Student, ItemSelection, fields=('item', 'item_quantity'), extra=26,  
  labels = {'item_quantity': '', 'item': ''}, 
  widgets= {'item': forms.Select(attrs={'class': 'form-control'}),
  'item_quantity': forms.NumberInput(attrs={'class': 'form-control'})})
  student = Student.objects.get(id=pk)
  formset = ListFormSet(instance=student)
  #form = ListForm(initial={'student':student})

  if request.method == "POST":
    formset = ListFormSet(request.POST, instance=student)
    if formset.is_valid():
      formset.save()
      return redirect('student')
  
  context = {'formset':formset}
  return render(request, 'add_list.html', context)


def Updatelist(request, pk):
  selection = ItemSelection.objects.get(student=pk)
  items = Item.objects.all()
  formset = ListFormSet(instance=student)
  if request.method == "POST":
    formset = ListFormSet(request.POST, instance=student)
    if formset.is_valid():
      formset.save()
      return redirect('student')

  context = {'form':form}
  return render(request, 'add_list.html', context)


""" def AddListView(request, pk):
   student = Student.objects.get(id=pk)
   items = request.POST.getlist('item')
   students = request.POST.getlist('student')
   quantitys = request.POST.getlist('quantity')
   res = []

  def get_context_data(self, **kwargs):
    items = Item.objects.all()
    students = Student.objects.all()
    selections = ItemSelection.objects.all()

    
    context = super(AddListView, self).get_context_data(**kwargs)
    context['items'] = items
    context['pk'] = self.kwargs['pk']
    context['students'] = students
    context['selections'] = selections

   for item, student, quantity in zip(items,students,quantitys):
       innerlist = []
       innerlist.append(objid+', '+name+', '+size+', '+number)
       res.append(innerlist)
 """

""" class AddListView(CreateView):
  model = StudentList
  template_name = 'add_list.html'
  form_class = ListForm
  def get_success_url(self):
    return self.request.path
  

  def get_context_data(self, **kwargs):
    items = Item.objects.all()
    students = Student.objects.all()
    selections = ItemSelection.objects.all()

    
    context = super(AddListView, self).get_context_data(**kwargs)
    context['items'] = items
    context['pk'] = self.kwargs['pk']
    context['students'] = students
    context['selections'] = selections


    return context#

 """


class DeliveredDonateView(UpdateView):
  model = Donate
  template_name = 'delivered_donations.html'
  form_class = DeliverForm
  success_url = reverse_lazy('my_donations')

  def get_context_data(self, **kwargs):
      donates = Donate.objects.all().order_by('-created_at')
      context = super(DeliveredDonateView, self).get_context_data(**kwargs)

      context['pk'] = self.kwargs['pk']
      context['donates'] = donates
      

      return context     


class ColectedDonateView(UpdateView):
  model = Donate
  template_name = 'colected_donation.html'
  form_class = ColectForm
  success_url = reverse_lazy('donated')

  def get_context_data(self, **kwargs):
      donates = Donate.objects.all().order_by('-created_at')
      context = super(ColectedDonateView, self).get_context_data(**kwargs)

      context['pk'] = self.kwargs['pk']
      context['donates'] = donates

      return context     


def LocalStateView(request, stt):
  schools = School.objects.filter(state=stt)
  return render(request, 'local_state.html', {'stt':stt,'schools': schools})


def FindSchoolView(request):
  schools = School.objects.all()
  profiles = Profile.objects.all()
  return render(request, 'find_school.html', {'profiles':profiles,'schools': schools})
