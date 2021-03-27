# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    TIPOS_USUARIO = [
        ('responsavel', 'Responsavel'),
        ('doador', 'Doador')
    ]

    email = models.EmailField('Email', unique=True)
    username = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    nome = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=14)
    endereco = models.CharField('Endereço', max_length=50)
    bairro = models.CharField('Bairro', max_length=50)
    complemento = models.CharField('Complemento', max_length=20, null=True, blank=True)
    cidade = models.CharField('Cidade', max_length=45)
    estado = models.CharField('Estado', max_length=2)
    cep = models.CharField('Cep', max_length=10)
    tipo = models.CharField('Tipo', choices=TIPOS_USUARIO, max_length=45)
