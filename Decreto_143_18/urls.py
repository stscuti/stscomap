from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from Decreto_143_18 import views
from django.views.generic import TemplateView


admin.autodiscover()

urlpatterns = [
    path('Empresa_Datos_Formales/', views.Nuevo_Empresa_Datos_Formales, name='PruebaPrincipal'),
    path('Empresa_FIT/', views.Nuevo_Empresa_FIT, name='PruebaFIT'),
    path('Tipo_Inversiones/', views.Nuevo_Tipo_Inversiones, name='PruebaTipoInversiones'),
    path('Tipo_Contribuyente/', views.Nuevo_Tipo_Contribuyente, name='PruebaTipoContribuyente'),
    path('Localizacion_Proyecto/', views.Nuevo_Localizacion_Proyecto, name='PruebaLocalizacionProyecto'),
    path('Expediente_Dec_143_18/', views.Nuevo_Expediente_Dec_143_18, name='PruebaExpedienteDec14318'),
    path('Cuadro_Inversiones_Empresa/', views.Nuevo_Cuadro_Inversiones_Empresa, name='PruebaCuadroInversionesEmpresa'),
    path('Cuadro_Inversiones_Definitivo/', views.Nuevo_Cuadro_Inversiones_Definitivo, name='PruebaCuadroInversionesDefinitivo'),
    path('Cuadro_Cotizaciones_Interbancarias/', views.Nuevo_Cotizaciones_Interbancarias, name='PruebaCuadroCotizacionesInterbancarias'),
    path('Cuadro_Ind_Gral_Empleo/', views.Nuevo_Ind_Gral_Empleo, name='PruebaCuadroIndGralEmpleo'),
    path('Cuadro_Exp_Bienes_Servicios/', views.Nuevo_Exp_Bienes_Servicios, name='PruebaCuadroExpBienesServicios'),
    path('Cuadro_Ind_Gral_Exportaciones/', views.Nuevo_Ind_Gral_Exportaciones, name='PruebaCuadroIndGralExportaciones'),
    path('Cuadro_Localizacion_Operaciones/', views.Nuevo_Localizacion_Operaciones, name='PruebaCuadroLocalizacionOperaciones'),
    path('Cuadro_Listado_Departamentos/', views.Nuevo_Listado_Departamentos, name='PruebaCuadroListadoDepartamentos'),
    path('Cuadro_Ind_Gral_Localizacion/', views.Nuevo_Ind_Gral_Localizacion, name='PruebaCuadroInd_Gral_Localizacion'),
    path('Cuadro_Ind_Gral_TL/', views.Nuevo_Ind_Gral_TL, name='PruebaCuadroIndGralTL'),
    path('Cuadro_Ind_Gral_IDi/', views.Nuevo_Ind_Gral_IDi, name='PruebaCuadroIndGralIDi'),
    path('Cuadro_Ind_Sect_Form_Cont/', views.Nuevo_Ind_Sect_Formacion_Continua, name='PruebaCuadroIndSectFormCont'),
    path('Cuadro_Ind_Sect_Dif_Pro_Proc/', views.Nuevo_Ind_Sect_Diferenciacion_Prod_Proc, name='PruebaCuadroIndSectDifProProc'),
    path('Cuadro_Ind_Sect_Energia_Renovable/', views.Nuevo_Ind_Sect_Energia_Renovable, name='PruebaCuadroIndSectEnergiaRenovable'),
    path('Cuadro_Mercado_Capitales/', views.Nuevo_Ind_Sect_Mercado_Capitales, name='PruebaCuadroIndSectMercadoCapitales'),
    path('Cuadro_Propietarios/', views.Nuevo_Propietarios_Directores_Representantes, name='PruebaCuadroPropietarios'),
    path('Cuadro_Contactos_Proyectos/', views.Nuevo_Contactos_Proyecto, name='PruebaCuadroContactosProyecto'),
    path('Registro_Empresas/', views.Registro_Proyecto_View.as_view(), name='RegistroEmpresa'),
    path('Contacto/', views.Nuevo_Contacto, name='PruebaContacto'),
    path ('Lista_Empresa_Datos_Formales/', views.Empresa_Datos_Formales_List.as_view(), name = 'ListaEmpresaDatosFormales' ),
    path('Lista_Multiple_Empresa_Datos_Formales/', views.MiListaMultiple.as_view(), name='ListaMultipleEmpresa'),
    path('Lista_Multiple_Empresa_Datos_Formales/getdata', views.MiListaMultiple1.as_view(),name='LME'),
    path('generar_pdf/', views.generar_pdf, name='pdf'),
    
    path('',include('django.contrib.auth.urls')),
   
]