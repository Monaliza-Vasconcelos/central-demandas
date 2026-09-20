from django.db import models
from django.conf import settings
from usuarios.models import Setor
# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
            return self.nome

class Demanda(models.Model):
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('RESOLVIDO', 'Resolvido'),
    ]

    cliente = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT
    )

    solicitante = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )

    setor = models.ForeignKey(
        Setor,
        on_delete=models.PROTECT
    )

    observacao = models.TextField(blank=True)
    data_hora = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDENTE'
    )

    def __str__(self):
        return f'{self.id} - {self.cliente}'