# -*- coding: utf-8 -*-
from django.db import models
from ..usuarios.models import Usuario
from ..escola.models import Escola


class Material(models.Model):
    id_material = models.AutoField(primary_key=True)
    desc_material = models.CharField('Descriçao Material', max_length=50)
    foto_material = models.ImageField( 'Foto material', upload_to='material')
    quantidade = models.IntegerField('Quantidade')

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materias"
        ordering = ["-id_material"]


class Lista(models.Model):
    id_lista = models.AutoField(primary_key=True)
    material_lista = models.ForeignKey(Material, null=True, related_name='lista_material', on_delete=models.CASCADE)
    escola_lista = models.ForeignKey(Escola, null=True, related_name='lista_escola', on_delete=models.CASCADE)
    usuario_lista = models.ForeignKey(Usuario, null=True, related_name='lista_usuario', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Lista"
        verbose_name_plural = "Listas"
        ordering = ["-id_lista"]

        def __str__(self):
            return self.lista
