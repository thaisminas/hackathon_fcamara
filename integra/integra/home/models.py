from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class ProfileType(models.Model):
  name = models.CharField(max_length=255, null=True)

  def __str__(self):
    return self.name


class Profile(models.Model):
  user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
  cpf = models.CharField(max_length=255)
  profile_type = models.ForeignKey(ProfileType, on_delete=models.CASCADE, null=True)
  cep = models.CharField(max_length=255, null=True)
  rua = models.CharField(max_length=255, null=True)
  bairro = models.CharField(max_length=255, null=True)
  cidade = models.CharField(max_length=255, null=True)
  estado = models.CharField(max_length=255, null=True)

  def __str__(self):
    return str(self.user)
  

class Grade(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name


class DonationType(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name


class School(models.Model):
  name = models.CharField(max_length=255)
  state = models.CharField(max_length=2)
  city = models.CharField(max_length=255)
  street = models.CharField(max_length=255)
  number = models.CharField(max_length=5)
  cep = models.BigIntegerField(null=True)
  cnpj = models.BigIntegerField(null=True)

  def __str__(self):
    return self.name


class Item(models.Model):
  name = models.CharField(max_length=255)
  pic = models.ImageField(null=True, blank=True, upload_to="images/")

  def __str__(self):
    return self.name


class Student(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  name = models.CharField(max_length=255, null=True)
  cpf = models.BigIntegerField(null=True)
  birth_date = models.DateField(null=True)
  grade = models.ForeignKey(Grade, on_delete=models.CASCADE, null=True)
  school = models.CharField(max_length=255, null=True)
  #mylist = models.OneToOneField(List, on_delete=models.CASCADE, null=True)
  profile_pic = models.ImageField(null=True, blank=True, upload_to="images/")
  registration_pic = models.ImageField(null=True, blank=True, upload_to="images/")


  def __str__(self):
    return self.name

  def get_absolute_url(self): 
    return reverse('student') 


class ItemSelection(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
  item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
  item_quantity = models.IntegerField(default=0)

  class Meta:
        unique_together = ('student', 'item')

  def __str__(self):
    return str(self.item_quantity) + "x " + self.item.name 


class StudentList(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
  item_selection = models.ForeignKey(ItemSelection, on_delete=models.CASCADE, null=True)


class Donate(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  message = models.TextField(null=True)
  donation_type = models.ForeignKey(DonationType, on_delete=models.CASCADE, null=True)
  anon = models.BooleanField(default=False)
  closed = models.BooleanField(default=False)
  notify = models.BooleanField(default=False)
  created_at = models.DateTimeField(null= True, auto_now_add=True)
  
  def __str__(self):
    if self.anon:
      return 'De: Anônimo Para: ' + self.student.name
    else:
      return 'De: ' + str(self.author) + ' Para: ' + self.student.name



  def get_absolute_url(self): 
    return reverse('home') 
