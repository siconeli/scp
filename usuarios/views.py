from django.shortcuts import render, redirect
from .models import Usuario
from django.http import HttpResponse
from django.contrib import messages
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_permission_decorator

@has_permission_decorator('gerenciar_usuarios')
def UsuarioCreate(request):        
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        cargo = request.POST.get('cargo')

        if not (usuario and senha and cargo):
            messages.error(request, 'Todos os campos são obrigatórios!')
        elif Usuario.objects.filter(username=usuario, is_active=True).exists():
            messages.error(request, 'Já existe um usuário que utiliza esse username, utilize outro.')
        else:
            Usuario.objects.create_user(username=usuario, password=senha, cargo=cargo)
            messages.success(request, 'Usuário cadastrado com sucesso!')
            
        return redirect('usuario-create')

    return render(request, 'usuarios/user_create.html')