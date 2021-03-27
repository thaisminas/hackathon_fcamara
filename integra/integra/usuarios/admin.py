# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Usuario


class UsuarioAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'cpf',
        'tipo'
    ]


admin.site.register(Usuario, UsuarioAdmin)