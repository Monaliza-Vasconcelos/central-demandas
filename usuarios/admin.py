from django.contrib import admin
from .models import Setor, Usuario
# Register your models here.


@admin.register(Setor)
class SetorAdmin(admin.ModelAdmin):
    pass

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    pass
