from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import UsuarioCreateForm, UsuarioUpdateForm, UpdatePasswordForm
from .models import Usuario
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rolepermissions.decorators import has_permission_decorator
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse

def Login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse('home'))
        return render(request, 'usuarios/login.html')
    elif request.method == 'POST':
        usuario = request.POST.get('username')
        senha =  request.POST.get('password')

        user = authenticate(username=usuario, password=senha)
        if user is not None:
            login(request, user)
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Usuário ou senha não encontrados!')
            return render(request, 'usuarios/login.html')
    
def Logout(request):
    if request.method == 'GET':
        logout(request)
        return redirect(reverse('login'))

# TODO Corrigir os messages para erros
@login_required
@has_permission_decorator('gerenciar_usuarios')
def UsuarioCreate(request):        
    if request.method == 'POST':
        form = UsuarioCreateForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            senha = form.cleaned_data.get('password')
            nome = form.cleaned_data.get('first_name')
            cargo = form.cleaned_data.get('cargo')

            if Usuario.objects.filter(username=username, is_active=True).exists():
                messages.error(request, 'Já existe um usuário que utiliza esse username, utilize outro.')
            else:
                Usuario.objects.create_user(username=username, password=senha, first_name=nome, cargo=cargo)
                messages.success(request, 'Usuário cadastrado com sucesso!')
                return redirect(reverse('usuario-create'))
            
    usuarios = Usuario.objects.filter(is_active=True).order_by('-id').exclude(is_superuser=True)

    return render(request, 'usuarios/usuario_create.html', {'usuarios': usuarios})

# TODO Corrigir os messages para erros
@login_required
@has_permission_decorator('gerenciar_usuarios')
def UsuarioUpdate(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    username_banco = usuario.username

    # ATUALIZAR O SIGNALS PARA APLICAR A PERMISSÃO DE ACORDO COM O CARGO ESCOLHIDO!
    if request.method == 'POST':
        form = UsuarioUpdateForm(request.POST or None, instance=usuario) 
        if form.is_valid():
            username_input = form.cleaned_data.get('username')

            if username_banco != username_input:
                if Usuario.objects.filter(username=username_input, is_active=True).exists():
                    messages.error(request, 'Já existe um usuário que utiliza esse username, utilize outro.')
                
            form.save()
            messages.success(request, 'Usuário atualizado com sucesso!')
            return redirect(reverse('usuario-create'))

        else:
            messages.error(request, 'Dados inválidos no formulário!')
    else:
        form = UsuarioUpdateForm(instance=usuario)
    
    return render(request, 'usuarios/usuario_update.html', {'form':form})

# TODO Corrigir os messages para erros
@login_required
@has_permission_decorator('gerenciar_usuarios')
def UpdatePassword(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    senha_banco_hashe = usuario.password # Senha com HASHE salva no banco de dados  

    if request.method == 'POST':
        form = UpdatePasswordForm(request.POST or None, instance=usuario)
        if form.is_valid():
            senha_atual = form.cleaned_data.get('password')
            nova_senha = request.POST.get('new_password')
            confirmar_senha = request.POST.get('new_password_confirm')

            if senha_atual and nova_senha == confirmar_senha:
                if check_password(senha_atual, senha_banco_hashe):
                    usuario.set_password(nova_senha)
                    usuario.save()
                    messages.success(request, 'Senha atualizada com sucesso!')
                    return redirect(reverse('usuario-create'))
                else:
                    messages.error(request, 'Senha diferentes...')
        else:
            messages.error(request, 'Dados inválidos no formulário!')
    else:
        form = UpdatePasswordForm(instance=usuario)

    return render(request, 'usuarios/update_password.html', {'form':form})