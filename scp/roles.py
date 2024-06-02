from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole): # Grupo
    available_permissions  = { # Permissões
        'gerenciar_empresa': True,
        'gerenciar_usuarios': True,
        'cadastrar_processos': True,
        'cadastrar_andamentos': True,
        'gerar_relatorios': True,
    }

class Atendente(AbstractUserRole):
    available_permissions  = {
        'cadastrar_processos': True,
        'cadastrar_andamentos': True,
        'gerar_relatorios': True,
    }