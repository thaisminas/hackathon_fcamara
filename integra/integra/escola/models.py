# -*- coding: utf-8 -*-
from django.db import models
from integra.integra.usuarios.models import Usuario


class Escola(models.Model):
    id_escola = models.AutoField(primary_key=True)
    nm_escola = models.CharField(max_length=70)
    cnpj = models.CharField(max_length=18)
    endereco = models.CharField(max_length=50)
    complemento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)


class Aluno(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    nm_aluno = models.CharField(50)
    cpf = models.CharField(10)
    dt_nascimento = models.DateField
    endereco = models.CharField(50)
    complemento = models.CharField(50)
    bairro = models.CharField(50)
    cidade = models.CharField(50)
    cep = models.CharField(10)
    escola = models.ForeignKey(Escola, null=True, related_name='aluno_escola', on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, null=True, related_name='aluno_usuario', on_delete=models.CASCADE)
