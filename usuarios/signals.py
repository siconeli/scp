from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Usuario
from rolepermissions.roles import assign_role

@receiver(post_save, sender=Usuario)
def define_permissoes(sender, instance, created, **kwargs):
    if created:
        if instance.cargo == 'G':
            assign_role(instance, 'gerente')
        elif instance.cargo == 'A':
            assign_role(instance, 'atendente')