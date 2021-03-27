# -*- coding: utf-8 -*-
from django.db import models
from ..usuarios.models import Usuario


def select_storage():
    return MyLocalStorage()

class Escola(models.Model):
    id_escola = models.AutoField(primary_key=True)
    nm_escola = models.CharField('Escola', max_length=70)
    cnpj = models.CharField('CNPJ', max_length=18)
    endereco = models.CharField('Endereço', max_length=50)
    complemento = models.CharField('Complemento', max_length=50)
    bairro = models.CharField('Bairro', max_length=50)
    cidade = models.CharField('Cidade', max_length=50)
    cep = models.CharField('CEP', max_length=10)

    class Meta:
        verbose_name = "Escola"
        verbose_name_plural = "Escolas"
        ordering = ["-id_escola"]

        def __str__(self):
            return self.escola


class Aluno(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    nm_aluno = models.CharField('Aluno(a)', max_length=50)
    cpf = models.CharField('CPF', max_length=10)
    dt_nascimento = models.DateField('Data de Nascimento')
    foto_material = models.ImageField('Foto aluno', upload_to='aluno')
    doc_matricula = models.ImageField('Comprovante', upload_to='aluno')
    endereco = models.CharField('Endereço', max_length=50)
    complemento = models.CharField('complemento', max_length=50)
    bairro = models.CharField('Bairro', max_length=50)
    cidade = models.CharField('Cidade', max_length=50)
    cep = models.CharField('CEP', max_length=10)
    escola = models.ForeignKey(Escola, null=True, related_name='aluno_escola', on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, null=True, related_name='aluno_usuario', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"
        ordering = ["-id_aluno"]

        def __str__(self):
            return self.aluno
