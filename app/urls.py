from django.contrib import admin
from django.urls import path
from .views import Home, CompanyDetail, CompanyCreate, CompanyUpdate, UserCreate

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('company/', CompanyDetail.as_view(), name='company'), 
    path('company/create/', CompanyCreate.as_view(), name='company-create'),
    path('company/update/<int:id>/', CompanyUpdate.as_view(), name='company-update'),

    path('user/create/', UserCreate.as_view(), name='user-create'),
]
