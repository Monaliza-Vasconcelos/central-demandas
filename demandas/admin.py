from django.contrib import admin
from .models import Categoria, Demanda

# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(Demanda)
class DemandaAdmin(admin.ModelAdmin):
    pass
