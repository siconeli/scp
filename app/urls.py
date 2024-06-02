from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('company/create/', views.CompanyCreate, name='company-create'),
    path('company/update/<int:id>/', views.CompanyUpdate, name='company-update'),
    path('company/view/', views.CompanyView, name='company-view'), 
]
