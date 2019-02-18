from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from Decreto_143_18 import views


admin.autodiscover()

urlpatterns = [
    path('', views.Nuevo_Empresa_Datos_Formales, name='PruebaPrincipal'),
]