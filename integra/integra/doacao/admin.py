# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Doacao


class DoacaoAdmin(admin.ModelAdmin):
    list_display = [
        'id_doacao',
        'tipo_doacao',
        'valor_doacao'
    ]

    #Usarei este codigo quando tiver dados para serem utilizados
    # def nome_doador(self, obj):
    #     obj.lista.usuario_lista.nome
    # nome_doador.short_description = 'Usuario'


admin.site.register(Doacao, DoacaoAdmin)
