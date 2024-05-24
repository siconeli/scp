from django.contrib import admin
from .models import Company

# @admin.register(UserExtension)
# class UserExtensionAdmin(admin.ModelAdmin):
#     list_display = ('cpf',)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('cnpj', 'razao_social', 'porte', 'nome_fantasia', 'logo', 'uf', 'municipio', 'logradouro', 'numero', 'cep', 'bairro', 'complemento', 'celular', 'telefone', 'email')
    exclude = ['criado_por', 'origem']

    def save_model(self, request, obj, form, change):
        obj.criado_por = request.user
        super().save_model(request, obj, form, change)
