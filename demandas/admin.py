from django.contrib import admin
from .models import Categoria, Demanda

# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(Demanda)
class DemandaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'cliente',
        'categoria',
        'solicitante',
        'setor',
        'status',
        'data_hora',
    )
    list_filter = (
        'status',
        'categoria',
        'setor',
    )

    search_fields = (
        'cliente',
        'telefone',
    )
