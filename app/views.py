from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from .models import Company
from django.urls import reverse_lazy

class Home(TemplateView):
    template_name = 'home.html'

class CompanyCreate(CreateView):
    model = Company
    template_name = 'company/company_create.html'
    fields = ['']
    # success_url = reverse_lazy('')

class CompanyUpdate(UpdateView):
    model = Company
    template_name = 'company/company_update.html'
    fields = ['cnpj', 'razao_social', 'porte', 'nome_fantasia', 'logo', 'uf', 'municipio', 'logradouro', 'numero', 'cep', 'bairro', 'complemento', 'celular', 'telefone', 'email']
    success_url = reverse_lazy('company')

    def get_object(self, queryset=None):
        company_id = self.kwargs.get('id')
        return self.model.objects.get(id=company_id)

class CompanyDetail(DetailView):
    model = Company
    template_name = 'company/company_detail.html'

    def get_object(self, queryset=None):
        return self.model.objects.filter(ativo=True).latest('id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company = self.model.objects.filter(ativo=True).latest('id')
        context['company_id'] = company.id
        return context


# class UserCreate(CreateView):
#     template_name = 'user/user_create.html'
#     model = User
#     fields = ['username', 'first_name', 'last_name', 'password']