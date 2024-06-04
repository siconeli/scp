from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Usuario
from rolepermissions.roles import assign_role, remove_role

@receiver(post_save, sender=Usuario)
def define_permissoes(sender, instance, created, **kwargs):
    if created:
        if instance.cargo == 'G':
            assign_role(instance, 'gerente')
        elif instance.cargo == 'A':
            assign_role(instance, 'atendente')
    else:
        usuario_banco = Usuario.objects.get(id=instance.id)
        if usuario_banco.cargo != instance.cargo:
            # Remover permissões antigas
            if usuario_banco.cargo == 'G':
                remove_role(instance, 'gerente') # 'gerente' -> roles.py
            elif usuario_banco.cargo == 'A':
                remove_role(instance, 'atendente') # 'atendente -> roles.py
            
            # Adicionar novas permissões
            if instance.cargo == 'G':
                assign_role(instance, 'gerente')
            elif instance.cargo == 'A':
                assign_role(instance, 'atendente')