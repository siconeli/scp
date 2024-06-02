from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['cnpj', 'razao_social', 'porte', 'nome_fantasia', 'logo', 'uf', 'municipio', 'logradouro', 'numero', 'cep', 'bairro', 'complemento', 'celular', 'telefone', 'email']