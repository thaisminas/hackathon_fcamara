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
  numero = models.CharField(max_length=255, null=True)

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
  school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
  #mylist = models.OneToOneField(List, on_delete=models.CASCADE, null=True)
  profile_pic = models.ImageField(null=True, blank=True, upload_to="images/")
  registration_pic = models.ImageField(null=True, blank=True, upload_to="images/")


  def __str__(self):
    return self.name

  def get_absolute_url(self): 
    return reverse('student') 


class ItemSelection(models.Model):
  ITEM = (
    ('Agenda escolar', 'Agenda escolar'),
    ('Apontador com depósito', 'Apontador com depósito'),
    ('Borracha escolar', 'Borracha escolar'),
    ('Caderno brochurão - 80 fls', 'Caderno brochurão - 80 fls'),
    ('Caderno de desenho - 96 fls', 'Caderno de desenho - 96 fls'),
    ('Caderno universitário - 200 fls', 'Caderno universitário - 200 fls'),
    ('Calculadora de bolso 8 dígitos', 'Calculadora de bolso 8 dígitos'),
    ('Caneta esferográfica (2 azuis, 1 preta e 1 vermelha)', 'Caneta esferográfica (2 azuis, 1 preta e 1 vermelha)'),
    ('Canetinha hidrográfica (12 cores)', 'Canetinha hidrográfica (12 cores)'),
    ('Cola branca 90g', 'Cola branca 90g'),
    ('Cola colorida', 'Cola colorida'),
    ('Esquadro 45º', 'Esquadro 45º'),
    ('Esquadro 60º', 'Esquadro 60º'),
    ('Giz de cera (12 cores)', 'Giz de cera (12 cores)'),
    ('Grafite 0.7', 'Grafite 0.7'),
    ('Lápis de cor (12 cores)', 'Lápis de cor (12 cores)'),
    ('Lápis grafite', 'Lápis grafite'),
    ('Lapiseira 0.7', 'Lapiseira 0.7'),
    ('Massa para modelar', 'Massa para modelar'),
    ('Material dourado', 'Material dourado'),
    ('Pasta plástica transparente com elástico', 'Pasta plástica transparente com elástico'),
    ('Pincel nº 8', 'Pincel nº 8'),
    ('Régua', 'Régua'),
    ('Tesoura sem ponta', 'Tesoura sem ponta'),
    ('Tinta guache (6 cores)', 'Tinta guache (6 cores)'),
    ('Transferidor 180º', 'Transferidor 180º'),
  )
  student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
  item = models.CharField(max_length=255, null= True, choices=ITEM)
  item_quantity = models.IntegerField(default=0)

  class Meta:
        unique_together = ('student', 'item')

  def __str__(self):
    return str(self.item_quantity) + "x " + str(self.item)


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
