from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from .models import Company
from django.urls import reverse_lazy
from django.http import HttpResponse

class Home(TemplateView):
    template_name = 'home.html'

class CompanyCreate(CreateView):
    model = Company
    template_name = 'company/company_create.html'
    fields = ['cnpj', 'razao_social', 'porte', 'nome_fantasia', 'logo', 'uf', 'municipio', 'logradouro', 'numero', 'cep', 'bairro', 'complemento', 'celular', 'telefone', 'email']
    success_url = reverse_lazy('company')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user

        if self.model.objects.exists():
            form.add_error(None, 'Empresa já cadastrada.') # TRATAR O ERROR NO LADO DO CLIENTE(TEMPLATE) ***
            return self.form_invalid(form)  
        return super().form_valid(form)

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
        try:
            return self.model.objects.filter(ativo=True).latest('id')
        except self.model.DoesNotExist:
            return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            company = self.model.objects.filter(ativo=True).latest('id')
            context['company_id'] = company.id
        except self.model.DoesNotExist:
            context['company_id'] = None
        
        return context

class UserCreate(CreateView):
    model = User
    template_name = 'user/user_create.html'
    fields = ['username', 'email', 'password']
    success_url = reverse_lazy('')

# class UserExtensionCreate(CreateView):
#     template_name = 'user_extension/user_extension_create.html'
#     model = User
#     fields = ['username', 'first_name', 'last_name', 'password']