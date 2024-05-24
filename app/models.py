from django.db import models
from django.contrib.auth.models import User

class Base(models.Model):
    ativo = models.BooleanField(default=True)
    criado_em = models.DateField(auto_now_add=True)
    criador_por = models.ForeignKey(User, )
    # origem = 

    class Meta:
        abstract = True

# class Company(Base):
    # logo =
    # cnpj = 
    # razao_social =
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

