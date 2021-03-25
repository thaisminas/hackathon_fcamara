from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
  cpf = models.IntegerField(blank=True, null=True)
  nm_aluno = models.CharField(max_length=255)
  cpf_aluno = models.IntegerField(blank=True, null=True)
  serie_aluno = models.IntegerField(blank=True, null=True)
  endereco = models.TextField(blank=True)
  