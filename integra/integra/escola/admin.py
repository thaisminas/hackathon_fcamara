# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Escola
from .models import Aluno


class EscolaAdmin(admin.ModelAdmin):
    list_display = [
        'id_escola',
        'nm_escola',
        'cnpj'
    ]

admin.site.register(Escola, EscolaAdmin)


class AlunoAdmin(admin.ModelAdmin):
    list_display = [
        'id_aluno',
        'nm_aluno',
        'cpf',
        'dt_nascimento'
    ]

    #Usarei este codigo quando tiver dados para serem utilizados
    # def escola_aluno(self, obj):
    #     obj.lista.escola.nome
    # escola_aluno.short_description = 'Escola'

    # def nome_responsavel(self, obj):
    #     obj.lista.usuario.nome
    # nome_responsavel.short_description = 'Usuario'


admin.site.register(Aluno, AlunoAdmin)