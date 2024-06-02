from django.urls import path
from . import views

urlpatterns = [
    path('usuario/create/', views.UsuarioCreate, name='usuario-create'),
]