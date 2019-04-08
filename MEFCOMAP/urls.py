"""MEFCOMAP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from Decreto_143_18 import views
from MEFCOMAP import views
from Decreto_143_18.apps import Decreto14318Config

from Login import views

import Decreto_143_18
import Login
from django.conf.urls.static import static
from django.views.generic import TemplateView



admin.autodiscover()

urlpatterns = [
    #path('registro/',include('Login.urls')),
    path('',include('Login.urls')),
    
    path('accounts/profile/',include('Login.urls'),name='secret'),
    #path('Contacto/logout/',include('Login.urls'),name='secret'),
    path('admin/', admin.site.urls),
    path('Empresa_Datos_Formales/', include('Decreto_143_18.urls'), name='PruebaPrincipal'),
    #path('signup/',include('Login.urls')),
    path('Empresa_FIT/', include('Decreto_143_18.urls'), name='PruebaFIT'),
    path('Tipo_Inversiones/', include('Decreto_143_18.urls'), name='PruebaTipoInversiones'),
    path('Tipo_Contribuyente/', include('Decreto_143_18.urls'), name='PruebaTipoContribuyente'),
    path('Localizacion_Proyecto/', include('Decreto_143_18.urls'), name='PruebaLocalizacionProyecto'),
    path('Expediente_Dec_143_18/', include('Decreto_143_18.urls'), name='PruebaExpedienteDec14318'),
    path('Cuadro_Inversiones_Empresa/', include('Decreto_143_18.urls'), name='PruebaCuadroInversionesEmpresa'),
    path('Cuadro_Inversiones_Definitivo/', include('Decreto_143_18.urls'), name='PruebaCuadroInversionesDefinitivo'),
    
    path('Cuadro_Cotizaciones_Interbancarias/', include('Decreto_143_18.urls'), name='PruebaCuadroCotizacionesInterbancarias'),
    path('Cuadro_Ind_Gral_Empleo/', include('Decreto_143_18.urls'), name='PruebaCuadroIndGralEmpleo'),
    path('Cuadro_Exp_Bienes_Servicios/', include('Decreto_143_18.urls'), name='PruebaCuadroExpBienesServicios'),
    path('Cuadro_Ind_Gral_Exportaciones/', include('Decreto_143_18.urls'), name='PruebaCuadroIndGralExportaciones'),
    path('Cuadro_Localizacion_Operaciones/', include('Decreto_143_18.urls'), name='PruebaCuadroLocalizacionOperaciones'),
    path('Cuadro_Listado_Departamentos/', include('Decreto_143_18.urls'), name='PruebaCuadroListadoDepartamentos'),
    path('Cuadro_Ind_Gral_Localizacion/', include('Decreto_143_18.urls'), name='PruebaCuadroInd_Gral_Localizacion'),
    path('Cuadro_Ind_Gral_TL/', include('Decreto_143_18.urls'), name='PruebaCuadroIndGralTL'),
    path('Cuadro_Ind_Gral_IDi/', include('Decreto_143_18.urls'), name='PruebaCuadroIndGralIDi'),
    path('Cuadro_Ind_Sect_Form_Cont/', include('Decreto_143_18.urls'), name='PruebaCuadroIndSectFormCont'),
    path('Cuadro_Ind_Sect_Dif_Pro_Proc/', include('Decreto_143_18.urls'), name='PruebaCuadroIndSectDifProProc'),
    path('Cuadro_Ind_Sect_Energia_Renovable/', include('Decreto_143_18.urls'), name='PruebaCuadroIndSectEnergiaRenovable'),
    path('Cuadro_Mercado_Capitales/', include('Decreto_143_18.urls'), name='PruebaCuadroIndSectMercadoCapitales'),
    path('Cuadro_Propietarios/', include('Decreto_143_18.urls'), name='PruebaCuadroPropietarios'),
    path('Cuadro_Contactos_Proyectos/', include('Decreto_143_18.urls'), name='PruebaCuadroContactosProyecto'),
    path('Registro_Empresas/', include('Decreto_143_18.urls'), name='RegistroEmpresa'),
    path('Lista_Empresa_Datos_Formales/', include('Decreto_143_18.urls'), name='ListaEmpresa'),
    path('Lista_Multiple_Empresa_Datos_Formales/', include('Decreto_143_18.urls'), name='ListaMultipleEmpresa'),
    path('Lista_Multiple_Empresa_Datos_Formales/getdata', include('Decreto_143_18.urls'),name='LME'),
    path('Contacto/login/main/index/', include('Login.urls'), name='secret'),
    
    #path('', views.login_page, name='login'),
    path('Contacto/', include('Decreto_143_18.urls'), name='PruebaContacto'),
    #path(r'^accounts/', include('django.contrib.auth.urls')),
    path('descargas/', include('Login.urls'), name='descargas'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
