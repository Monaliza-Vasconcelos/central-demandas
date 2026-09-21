from django.contrib import admin
from .models import Categoria, Demanda, Interacao

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
        'fluxo',
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

    list_display_links = (
        'id',
        'cliente',
    )


@admin.register(Interacao)
class InteracaoAdmin(admin.ModelAdmin):
    pass