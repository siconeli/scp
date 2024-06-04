from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import UsuarioForm
from .models import Usuario
from django.contrib import messages
from rolepermissions.decorators import has_permission_decorator
from django.contrib.auth.hashers import check_password

@has_permission_decorator('gerenciar_usuarios')
def UsuarioCreate(request):        
    if request.method == 'POST':
        form = UsuarioForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            senha = form.cleaned_data.get('password')
            nome = form.cleaned_data.get('first_name')
            cargo = form.cleaned_data.get('cargo')

            if Usuario.objects.filter(username=username, is_active=True).exists():
                messages.error(request, 'Já existe um usuário que utiliza esse username, utilize outro.')
            else:
                Usuario.objects.create_user(username=username, password=senha, first_name=nome, cargo=cargo)
                return redirect(reverse('usuario-create'))
            
    usuarios = Usuario.objects.filter(is_active=True).order_by('-id').exclude(is_superuser=True)

    return render(request, 'usuarios/usuario_create.html', {'usuarios': usuarios})

@has_permission_decorator('gerenciar_usuarios')
def UsuarioUpdate(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    senha_banco = usuario.password # Senha com HASHE salva no banco de dados

    if request.method == 'POST':
        form = UsuarioForm(request.POST or None, instance=usuario) 
        if form.is_valid():
            print('é valido')
            senha_atual = form.cleaned_data.get('password')
            nova_senha = request.POST.get('new_password')
            confirmar_senha = request.POST.get('new_password_confirm')

            print(usuario.password)
            if senha_atual and nova_senha == confirmar_senha:
                if check_password(senha_atual, senha_banco):
                    print('bateu')
                    usuario.set_password(nova_senha)
                    usuario.save()
                    print('usuario salvo com nova senha!')
                    return redirect(reverse('usuario-create'))
                else:
                    messages.error(request, 'Problemas com alguma das senhas informadas...')
            else:
                messages.error(request, 'A nova senha e a confirmação da nova senha são diferentes.')
        else:
            print('INVALIDO')
    else:
        form = UsuarioForm(instance=usuario)
    
    return render(request, 'usuarios/usuario_update.html', {'form':form})