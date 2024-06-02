from django.shortcuts import render, redirect, get_object_or_404
from .forms import CompanyForm
from django.contrib import messages
from .models import Company
from django.core.exceptions import ObjectDoesNotExist
# from django.http import HttpResponse
from rolepermissions.decorators import has_permission_decorator

def Home(request):
    return render(request, 'home.html')

def CompanyView(request):
    try:
        company = Company.objects.filter(ativo=True).latest('id')
    except ObjectDoesNotExist:
        company = None    
    context = {
        'company': company
    }

    return render(request, 'company/company_view.html', context)

@has_permission_decorator('cadastrar_empresa')
def CompanyCreate(request):
    form = CompanyForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            if Company.objects.filter(ativo=True).exists():
                messages.error(request, 'Já existe uma empresa cadastrada, não é permitido criar outra!') # TODO Tratar o error no front-end.
                return render(request, 'company/company_create.html')
            else: 
                form.instance.criado_por = request.user
                form.save()
                return redirect('company-view')
        else:
            messages.error(request, 'Erro ao cadastrar empresa, o formulário não é válido!')
            
    return render(request, 'company/company_create.html', {'form': form} )

def CompanyUpdate(request, id):
    company = get_object_or_404(Company, id=id)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company-view')
        else:
            messages.error(request, 'Erro ao atualizar empresa, o formulário não é válido! ')
    else:
        form = CompanyForm(instance=company)

    return render(request, 'company/company_update.html', {'form': form})

