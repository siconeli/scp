from django import forms
from django.contrib.auth import forms as contrib_auth_forms
from .models import Usuario

class UserChangeForm(contrib_auth_forms.UserChangeForm):
    class Meta(contrib_auth_forms.UserChangeForm.Meta):
        model = Usuario
    
class UserCreationForm(contrib_auth_forms.UserCreationForm):
    class Meta(contrib_auth_forms.UserCreationForm.Meta):
        model = Usuario

class UsuarioCreateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password', 'first_name', 'cargo']

class UsuarioUpdateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['is_active', 'username', 'first_name', 'cargo']

class UsuarioUpdatePasswordForm(forms.ModelForm):
    model = Usuario
    fields = ['password']