from django.db import models
from django.contrib.auth.models import User

class Base(models.Model):
    ativo = models.BooleanField(default=True)
    criado_em = models.DateField(auto_now_add=True)
    criador_por = models.ForeignKey(User, on_delete=models.PROTECT)
    origem = models.CharField(max_length=10, default='usuario')

    class Meta:
        abstract = True

class Company(Base):
    logo = models.ImageField(upload_to='logos/')
    cnpj = models.CharField(max_length=20)
    razao_social = models.CharField(max_length=100)
    nome_fantasia = models.CharField(max_length=100)
    # porte = 
    # uf =  
    # municipio = 
    # logradouro = 
    # numero = 
    # cep = 
    # bairro = 
    # complemento = 
    # celular = 
    # telefone = 

    # def __str__(self):
    #         return self.razao_social

# class UserExtension(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     cpf = models.CharField(max_length=20)
    
#     def __str__(self):
#         return self.cpf

