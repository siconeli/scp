from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    choices_cargo = {
        ('G', 'Gerente'),
        ('A', 'Atendente')
    }
    cargo = models.CharField(max_length=10, choices=choices_cargo)