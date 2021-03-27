# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    email = models.EmailField('Email', unique=True)
    username = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    aluno = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    endereco = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    complemento = models.CharField(max_length=20, null=True, blank=True)
    cidade = models.CharField(max_length=45)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=10)
    tipo = models.CharField(max_length=45)


    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
