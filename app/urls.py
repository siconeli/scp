from django.contrib import admin
from django.urls import path
from .views import Home, CompanyDetail, CompanyUpdate 

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('company/', CompanyDetail.as_view(), name='company'), 
    path('company/update/<int:id>/', CompanyUpdate.as_view(), name='company-update')
]
