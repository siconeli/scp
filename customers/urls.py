from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('customers-central-admin/', admin.site.urls),
]