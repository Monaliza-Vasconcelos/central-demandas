from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.

class Setor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Usuario(AbstractUser):
    setor = models.ForeignKey(Setor, on_delete=models.SET_NULL, null=True, blank=True)

