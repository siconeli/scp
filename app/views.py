from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import CompanyForm
from django.contrib import messages
from .models import Company
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from rolepermissions.decorators import has_permission_decorator

# @login_required
def Home(request):
    return render(request, 'home.html')

@login_required
def CompanyView(request):
    try:
        company = Company.objects.filter(ativo=True).latest('id')
    except ObjectDoesNotExist:
        company = None    
    context = {
        'company': company
    }

    return render(request, 'company/company_view.html', context)

@login_required
@has_permission_decorator('gerenciar_empresa')
def CompanyCreate(request):
    form = CompanyForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            if Company.objects.filter(ativo=True).exists():
                messages.error(request, 'Já existe uma empresa cadastrada, não é permitido cadastrar outra!') # TODO Tratar o error no front-end.
                return redirect(reverse('company-create'))
            else: 
                company_instance = form.save(commit=False)
                company_instance.criado_por = request.user
                company_instance.logo = request.FILES.get('logo')
                company_instance.save()
                return redirect(reverse('company-view'))
        else:
            messages.error(request, 'Erro ao cadastrar empresa, o formulário não é válido!')
            
    return render(request, 'company/company_create.html', {'form': form} )

@login_required
@has_permission_decorator('gerenciar_empresa')
def CompanyUpdate(request, id):
    company = get_object_or_404(Company, id=id)
    if request.method == 'POST':
        form = CompanyForm(request.POST or None, request.FILES or None, instance=company)
        if form.is_valid():
            company_instance = form.save(commit=False)
            if 'remove_logo' in request.POST:
                company_instance.logo = None
            elif request.FILES.get('logo'):
                company_instance.logo = request.FILES.get('logo')
            company_instance.save()
            return redirect(reverse('company-view'))
        else:
            messages.error(request, 'Erro ao atualizar empresa, o formulário não é válido! ')
    else:
        form = CompanyForm(instance=company)

    return render(request, 'company/company_update.html', {'form': form})

