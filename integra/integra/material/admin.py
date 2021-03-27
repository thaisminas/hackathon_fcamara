# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Material


class MaterialAdmin(admin.ModelAdmin):
    list_display = [
        'id_material',
        'desc_material',
        'quantidade'
    ]

admin.site.register(Material, MaterialAdmin)



class ListaAdmin(admin.ModelAdmin):
    list_display = [
        'id_lista'
    ]

    #Usarei este codigo quando tiver dados para serem utilizados
    # def nome_doador(self, obj):
    #     obj.lista.usuario_lista.nome
    # nome_doador.short_description = 'Usuario'