# -*- coding: utf-8 -*-
from django.db import models
from ..material.models import Lista


class Doacao(models.Model):
    TIPOS_DOACAO = [
        ('material', 'Material'),
        ('dinheiro', 'Dinheiro')
    ]

    id_doacao = models.AutoField(primary_key=True)
    doacao_anonima = models.BooleanField('Doacao anonima', default=False)
    msg_doador = models.TextField('Mensagem do Doador')
    msg_responsavel = models.TextField('Mensagem do responsavel')
    tipo_doacao = models.CharField('Tipo de doaçao ', choices=TIPOS_DOACAO, max_length=50)
    valor_doacao = models.DecimalField('Valor', max_digits=5, decimal_places=2)
    lista = models.ForeignKey(Lista, null=True, related_name='listas', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Doaçao"
        verbose_name_plural = "Doacoes"
        ordering = ["-id_doacao"]

        def __str__(self):
            return self.id_doacao