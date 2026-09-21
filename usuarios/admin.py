from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Setor, Usuario
# Register your models here.


@admin.register(Setor)
class SetorAdmin(admin.ModelAdmin):
    pass

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Informações da empresa', {'fields': ('setor',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informações da empresa', {'fields': ('setor',)}),
    )
