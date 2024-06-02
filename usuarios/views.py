from django.shortcuts import render
from .models import Usuario
from django.http import HttpResponse
from django.contrib import messages
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_permission_decorator

@has_permission_decorator('cadastrar_usuarios')
def UsuarioCreate(request):        
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        cargo = request.POST.get('cargo')

        if Usuario.objects.filter(username=usuario, is_active=True).exists():
            messages.success(request, 'Já existe um usuário que utiliza esse username, por favor utilize outro.')
            return render(request, 'usuarios/user_create.html')
        
        usuario_obj = Usuario.objects.create_user(username=usuario, password=senha, cargo=cargo)
        if cargo == 'G':
            assign_role(usuario_obj, 'gerente')
        elif cargo == 'A':
            assign_role(usuario_obj, 'atendente')

        messages.success(request, 'Usuário cadastrado com sucesso!')

    return render(request, 'usuarios/user_create.html')