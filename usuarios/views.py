from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from .forms import UsuarioForm
# from django.http import HttpResponse
from django.contrib import messages
from rolepermissions.decorators import has_permission_decorator

@has_permission_decorator('gerenciar_usuarios')
def UsuarioCreate(request):        
    form = UsuarioForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username_form = form.cleaned_data['username']
            if Usuario.objects.filter(username=username_form, is_active=True).exists():
                messages.error(request, 'Já existe um usuário que utiliza esse username, utilize outro.')
            else:
                form.save()
                messages.success(request, 'Usuário cadastrado com sucesso!') #TODO Aplicar um tempo de exibição desta mensagem no template com JS.
                return redirect('usuario-create')

    usuarios = Usuario.objects.filter(is_active=True).order_by('-id').exclude(is_superuser=True)

    return render(request, 'usuarios/usuario_create.html', {'form':form, 'usuarios': usuarios})

def UsuarioUpdate(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario) 
        print(form)
        if form.is_valid():
            nova_senha = form.cleaned_data['new_password']
            confirmar_senha = form.cleaned_data['new_password_confirm']
            if nova_senha == confirmar_senha:
                print('IGUAIS!')
        else:
            print('INVALIDO')
    else:
        form = UsuarioForm(instance=usuario)
    
    return render(request, 'usuarios/usuario_update.html', {'form':form})