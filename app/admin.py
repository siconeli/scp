from django.contrib import admin
from .models import UserExtension

@admin.register(UserExtension)
class UserExtensionAdmin(admin.ModelAdmin):
    list_display = ('cpf',)