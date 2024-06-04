from django.urls import path
from . import views

urlpatterns = [
    path('usuario/create/', views.UsuarioCreate, name='usuario-create'),
    path('usuario/update/<int:id>/', views.UsuarioUpdate, name='usuario-update'),
    path('usuario/update/password/<int:id>/', views.UpdatePassword, name="update-password"),
]