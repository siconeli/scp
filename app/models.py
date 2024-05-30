from django.db import models
from usuarios.models import Usuario

class Base(models.Model):
    ativo = models.BooleanField(default=True)
    criado_em = models.DateField(auto_now_add=True)
    criado_por = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    origem = models.CharField(max_length=10, default='usuario')

    class Meta:
        abstract = True

class Company(Base):
    cnpj = models.CharField(max_length=20)
    razao_social = models.CharField(max_length=100)
    porte = models.CharField(max_length=3)
    nome_fantasia = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='media/', blank=True, null=True)
    uf =  models.CharField(max_length=2)
    municipio = models.CharField(max_length=50)
    logradouro = models.CharField(max_length=50)
    numero = models.CharField(max_length=5)
    cep = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    celular = models.CharField(max_length=20, blank=True, null=True)
    telefone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
            return self.razao_social



