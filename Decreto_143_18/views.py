from Decreto_143_18.models import Empresa_Datos_Formales
from Decreto_143_18.models import Tipo_Contribuyente
from Decreto_143_18.models import Empresa_FIT
from Decreto_143_18.models import Tipo_Inversiones
from Decreto_143_18.models import Expediente_Dec_143_18
from Decreto_143_18.models import Localizacion_Proyecto
from Decreto_143_18.models import Contacto
from Decreto_143_18.models import Cuadro_Inversiones_Empresa
from Decreto_143_18.models import Cuadro_Inversiones_Definitivo
from Decreto_143_18.models import Cotizaciones_Interbancarias
from Decreto_143_18.models import Ind_Gral_Empleo
from Decreto_143_18.models import Exp_Bienes_Servicios
from Decreto_143_18.models import Ind_Gral_Exportaciones
from Decreto_143_18.models import Localizacion_Operaciones
from Decreto_143_18.models import Listado_Departamentos
from Decreto_143_18.models import Ind_Gral_Localizacion
from Decreto_143_18.models import Ind_Gral_TL
from Decreto_143_18.models import Ind_Gral_IDi
from Decreto_143_18.models import Ind_Sect_Formacion_Continua
from Decreto_143_18.models import Ind_Sect_Diferenciacion_Prod_Proc
from Decreto_143_18.models import Ind_Sect_Energia_Renovable
from Decreto_143_18.models import Ind_Sect_Mercado_Capitales
from Decreto_143_18.models import Propietarios_Directores_Representantes
from Decreto_143_18.models import Contactos_Proyecto


from Decreto_143_18.forms import Empresa_Datos_Formales_Form   
from Decreto_143_18.forms import Contacto_Form
from Decreto_143_18.forms import Tipo_Inversiones_Form
from Decreto_143_18.forms import Expediente_Dec_143_18_Form
from Decreto_143_18.forms import Localizacion_Proyecto_Form 
from Decreto_143_18.forms import Empresa_FIT_Form
from Decreto_143_18.forms import Cuadro_Inversiones_Empresa_Form
from Decreto_143_18.forms import Cuadro_Inversiones_Definitivo_Form
from Decreto_143_18.forms import Tipo_Contribuyente_Form
from Decreto_143_18.forms import Cotizaciones_Interbancarias_Form
from Decreto_143_18.forms import Ind_Gral_Empleo_Form
from Decreto_143_18.forms import Exp_Bienes_Servicios_Form
from Decreto_143_18.forms import Ind_Gral_Exportaciones_Form
from Decreto_143_18.forms import Localizacion_Operaciones_Form
from Decreto_143_18.forms import Listado_Departamentos_Form
from Decreto_143_18.forms import Ind_Gral_Localizacion_Form
from Decreto_143_18.forms import Ind_Gral_TL_Form
from Decreto_143_18.forms import Ind_Gral_IDi_Form
from Decreto_143_18.forms import Ind_Sect_Formacion_Continua_Form
from Decreto_143_18.forms import Ind_Sect_Diferenciacion_Prod_Proc_Form
from Decreto_143_18.forms import Ind_Sect_Energia_Renovable_Form
from Decreto_143_18.forms import Ind_Sect_Mercado_Capitales_Form
from Decreto_143_18.forms import Propietarios_Directores_Representantes_Form
from Decreto_143_18.forms import Contactos_Proyecto_Form

from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.template import RequestContext, Template, Context
from django.core.mail import EmailMessage
from django.views.generic import CreateView
from django.core.exceptions import ImproperlyConfigured
from django.utils.encoding import force_text
from django.views.generic.base import ContextMixin
from Decreto_143_18 import forms
from Decreto_143_18.multiple_forms import MultipleFormsView
from PIL import Image

from django.views.generic.list import ListView
import io 
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter,landscape,A4,portrait
from reportlab.platypus import Table
from io import BytesIO, StringIO
from reportlab.pdfgen import canvas
from reportlab.platypus.flowables import Flowable
from reportlab.lib.units import inch
from django.views.generic import (TemplateView, CreateView, DetailView, UpdateView, DeleteView, View)

from itertools import chain
from operator import attrgetter
from django.utils import timezone
import datetime

from rlextra.rml2pdf import rml2pdf
#import cStringIO

# Create your views here.
def Nuevo_Empresa_Datos_Formales(request):
    if request.method=='POST':
        formulario = Empresa_Datos_Formales_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('PruebaFIT')
    else:
        formulario=Empresa_Datos_Formales_Form()
    return render(request, 'Empresa_Datos_Formales_Form.html', {'formulario':formulario})

def Nuevo_Empresa_FIT(request):
    if request.method=='POST':
        formulario = Empresa_FIT_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('PruebaExpedienteDec14318')
    else:
        formulario=Empresa_FIT_Form()
    return render(request,'Empresa_FIT_Form.html', {'formulario':formulario})



def Nuevo_Tipo_Inversiones(request):
    message = ""
    if request.method=='POST':
        formulario = Tipo_Inversiones_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            #return HttpResponseRedirect('Expediente_Dec_143_18/Tipo_Inversiones')
            formulario = Tipo_Inversiones_Form() 
            success = True
            message = "Datos Guardados Correctamente"
            return render(request,'Tipo_Inversiones_Form.html', {'formulario':formulario, 'mensaje':message})
    else:
        formulario=Tipo_Inversiones_Form()
    return render(request,'Tipo_Inversiones_Form.html', {'formulario':formulario})




def Nuevo_Tipo_Contribuyente(request):
    message = ""
    if request.method=='POST':
        formulario = Tipo_Contribuyente_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            #return HttpResponseRedirect('/Decreto_143_18')
            formulario = Tipo_Contribuyente_Form() 
            success = True
            message = "Datos Guardados Correctamente"
            return render(request,'Tipo_Contribuyente_Form.html', {'formulario':formulario, 'mensaje':message})
    else:
        formulario = Tipo_Contribuyente_Form()
    return render(request,'Tipo_Contribuyente_Form.html', {'formulario':formulario})




def Nuevo_Localizacion_Proyecto(request):
    
    if request.method=='POST':
        formulario = Localizacion_Proyecto_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('PruebaCuadroIndGralEmpleo')
    else:
        formulario=Localizacion_Proyecto_Form()
    return render(request,'Localizacion_Proyecto_Form.html', {'formulario':formulario})



def Nuevo_Expediente_Dec_143_18(request):
    if request.method=='POST':
        formulario = Expediente_Dec_143_18_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('PruebaLocalizacionProyecto')
    else:
        formulario=Expediente_Dec_143_18_Form()
    return render(request,'Expediente_Dec_143_18_Form.html', {'formulario':formulario})

def Nuevo_Cuadro_Inversiones_Empresa(request):
    message = ""
    if request.method=='POST':
        formulario = Cuadro_Inversiones_Empresa_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            #return HttpResponseRedirect('/Decreto_143_18')
            formulario = Cuadro_Inversiones_Empresa_Form() 
            success = True
            message = "Datos Guardados Correctamente"
            return render(request,'Cuadro_Inversiones_Empresa_Form.html', {'formulario':formulario, 'mensaje':message})
    else:
        formulario=Cuadro_Inversiones_Empresa_Form()
    return render(request,'Cuadro_Inversiones_Empresa_Form.html', {'formulario':formulario})

def Nuevo_Cuadro_Inversiones_Definitivo(request):
    message = ""
    if request.method=='POST':
        formulario = Cuadro_Inversiones_Definitivo_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            #return HttpResponseRedirect('/Decreto_143_18')
            formulario = Cuadro_Inversiones_Definitivo_Form() 
            success = True
            message = "Datos Guardados Correctamente"
            return render(request,'Cuadro_Inversiones_Definitivo_Form.html', {'formulario':formulario, 'mensaje':message})
    else:
        formulario=Cuadro_Inversiones_Definitivo_Form()
    return render(request,'Cuadro_Inversiones_Definitivo_Form.html', {'formulario':formulario})

def Nuevo_Contacto(request):
    message = ""
    if request.method=='POST':
        formulario = Contacto_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            #return HttpResponseRedirect('/Decreto_143_18')
            formulario = Contacto_Form() 
            success = True
            message = "Datos Guardados Correctamente"
            return render(request,'Contacto_Form.html', {'formulario':formulario, 'mensaje':message})
    else:
        formulario = Contacto_Form()
    return render(request,'Contacto_Form.html', {'formulario':formulario})

def Nuevo_Cotizaciones_Interbancarias(request):
    message = ""
    if request.method=='POST':
        formulario = Cotizaciones_Interbancarias_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            #return HttpResponseRedirect('/Decreto_143_18')
            formulario = Cotizaciones_Interbancarias_Form() 
            success = True
            message = "Datos Guardados Correctamente"
            return render(request,'Cotizaciones_Interbancarias_Form.html', {'formulario':formulario, 'mensaje':message})
    else:
        formulario = Cotizaciones_Interbancarias_Form()
    return render(request,'Cotizaciones_Interbancarias_Form.html', {'formulario':formulario})    

def Nuevo_Ind_Gral_Empleo(request):
    message = ""
    if request.method=='POST':
        formulario = Ind_Gral_Empleo_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            #return HttpResponseRedirect('/Decreto_143_18')
            formulario = Ind_Gral_Empleo_Form() 
            success = True
            message = "Datos Guardados Correctamente"
            return render(request,'Ind_Gral_Empleo_Form.html', {'formulario':formulario, 'mensaje':message})
    else:
        formulario = Ind_Gral_Empleo_Form()
    return render(request,'Ind_Gral_Empleo_Form.html', {'formulario':formulario})

def Nuevo_Exp_Bienes_Servicios(request):
    message = ""
    if request.method=='POST':
        formulario = Exp_Bienes_Servicios_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            #return HttpResponseRedirect('/Decreto_143_18')
            formulario = Exp_Bienes_Servicios_Form() 
            success = True
            message = "Datos Guardados Correctamente"
            return render(request,'Exp_Bienes_Servicios_Form.html', {'formulario':formulario, 'mensaje':message})
    else:
        formulario = Exp_Bienes_Servicios_Form()
    return render(request,'Exp_Bienes_Servicios_Form.html', {'formulario':formulario})

def Nuevo_Ind_Gral_Exportaciones(request):
    message = ""
    if request.method=='POST':
        formulario = Ind_Gral_Exportaciones_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            #return HttpResponseRedirect('/Decreto_143_18')
            formulario = Ind_Gral_Exportaciones_Form() 
            success = True
            message = "Datos Guardados Correctamente"
            return render(request,'Ind_Gral_Exportaciones_Form.html', {'formulario':formulario, 'mensaje':message})
    else:
        formulario = Ind_Gral_Exportaciones_Form()
    return render(request,'Ind_Gral_Exportaciones_Form.html', {'formulario':formulario})

def Nuevo_Localizacion_Operaciones(request):
    message = ""
    if request.method=='POST':
        formulario = Localizacion_Operaciones_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            #return HttpResponseRedirect('/Decreto_143_18')
            formulario = Localizacion_Operaciones_Form() 
            success = True
            message = "Datos Guardados Correctamente"
            return render(request,'Localizacion_Operaciones_Form.html', {'formulario':formulario, 'mensaje':message})
    else:
        formulario = Localizacion_Operaciones_Form()
    return render(request,'Localizacion_Operaciones_Form.html', {'formulario':formulario})

def Nuevo_Listado_Departamentos(request):
    message = ""
    if request.method=='POST':
        formulario = Listado_Departamentos_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            #return HttpResponseRedirect('/Decreto_143_18')
            formulario = Listado_Departamentos_Form() 
            success = True
            message = "Datos Guardados Correctamente"
            return render(request,'Listado_Departamentos_Form.html', {'formulario':formulario, 'mensaje':message})
    else:
        formulario = Listado_Departamentos_Form()
    return render(request,'Listado_Departamentos_Form.html', {'formulario':formulario})

def Nuevo_Ind_Gral_Localizacion(request):
    message = ""
    if request.method=='POST':
        formulario = Ind_Gral_Localizacion_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            #return HttpResponseRedirect('/Decreto_143_18')
            formulario = Ind_Gral_Localizacion_Form() 
            success = True
            message = "Datos Guardados Correctamente"
            return render(request,'Ind_Gral_Localizacion_Form.html', {'formulario':formulario, 'mensaje':message})
    else:
        formulario = Ind_Gral_Localizacion_Form()
    return render(request,'Ind_Gral_Localizacion_Form.html', {'formulario':formulario})

def Nuevo_Ind_Gral_TL(request):
    message = ""
    if request.method=='POST':
        formulario = Ind_Gral_TL_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            #return HttpResponseRedirect('/Decreto_143_18')
            formulario = Ind_Gral_TL_Form() 
            success = True
            message = "Datos Guardados Correctamente"
            return render(request,'Ind_Gral_TL_Form.html', {'formulario':formulario, 'mensaje':message})
    else:
        formulario = Ind_Gral_TL_Form()
    return render(request,'Ind_Gral_TL_Form.html', {'formulario':formulario})

def Nuevo_Ind_Gral_IDi(request):
    message = ""
    if request.method=='POST':
        formulario = Ind_Gral_IDi_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            #return HttpResponseRedirect('/Decreto_143_18')
            formulario = Ind_Gral_IDi_Form() 
            success = True
            message = "Datos Guardados Correctamente"
            return render(request,'Ind_Gral_IDi_Form.html', {'formulario':formulario, 'mensaje':message})
    else:
        formulario = Ind_Gral_IDi_Form()
    return render(request,'Ind_Gral_IDi_Form.html', {'formulario':formulario})

def Nuevo_Ind_Sect_Formacion_Continua(request):
    message = ""
    if request.method=='POST':
        formulario = Ind_Sect_Formacion_Continua_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            #return HttpResponseRedirect('/Decreto_143_18')
            formulario = Ind_Sect_Formacion_Continua_Form() 
            success = True
            message = "Datos Guardados Correctamente"
            return render(request,'Ind_Sect_Formacion_Continua_Form.html', {'formulario':formulario, 'mensaje':message})
    else:
        formulario = Ind_Sect_Formacion_Continua_Form()
    return render(request,'Ind_Sect_Formacion_Continua_Form.html', {'formulario':formulario})

def Nuevo_Ind_Sect_Diferenciacion_Prod_Proc(request):
    message = ""
    if request.method=='POST':
        formulario = Ind_Sect_Diferenciacion_Prod_Proc_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            #return HttpResponseRedirect('/Decreto_143_18')
            formulario = Ind_Sect_Diferenciacion_Prod_Proc_Form() 
            success = True
            message = "Datos Guardados Correctamente"
            return render(request,'Ind_Sect_Diferenciacion_Prod_Proc_Form.html', {'formulario':formulario, 'mensaje':message})
    else:
        formulario = Ind_Sect_Diferenciacion_Prod_Proc_Form()
    return render(request,'Ind_Sect_Diferenciacion_Prod_Proc_Form.html', {'formulario':formulario})

def Nuevo_Ind_Sect_Energia_Renovable(request):
    message = ""
    if request.method=='POST':
        formulario = Ind_Sect_Energia_Renovable_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            formulario = Ind_Sect_Energia_Renovable_Form() 
            success = True
            message = "Datos Guardados Correctamente"
            return render(request,'Ind_Sect_Energia_Renovable_Form.html', {'formulario':formulario, 'mensaje':message})
    else:
        formulario = Ind_Sect_Energia_Renovable_Form()
    return render(request,'Ind_Sect_Energia_Renovable_Form.html', {'formulario':formulario})

def Nuevo_Ind_Sect_Mercado_Capitales(request):
    message = ""
    if request.method=='POST':
        formulario = Ind_Sect_Mercado_Capitales_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            #return HttpResponseRedirect('/Decreto_143_18')
            formulario = Ind_Sect_Mercado_Capitales_Form() 
            success = True
            message = "Datos Guardados Correctamente"
            return render(request,'Ind_Sect_Mercado_Capitales_Form.html', {'formulario':formulario, 'mensaje':message})
    else:
        formulario = Ind_Sect_Mercado_Capitales_Form()
    return render(request,'Ind_Sect_Mercado_Capitales_Form.html', {'formulario':formulario})

def Nuevo_Propietarios_Directores_Representantes(request):
    message = ""
    if request.method=='POST':
        formulario = Propietarios_Directores_Representantes_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            #return HttpResponseRedirect('/Decreto_143_18')
            formulario = Propietarios_Directores_Representantes_Form() 
            success = True
            message = "Datos Guardados Correctamente"
            return render(request,'Propietarios_Directores_Representantes_Form.html', {'formulario':formulario, 'mensaje':message})
    else:
        formulario = Propietarios_Directores_Representantes_Form()
    return render(request,'Propietarios_Directores_Representantes_Form.html', {'formulario':formulario})

def Nuevo_Contactos_Proyecto(request):
    message = ""
    if request.method=='POST':
        formulario = Contactos_Proyecto_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            #return HttpResponseRedirect('/Decreto_143_18')
            formulario = Contactos_Proyecto_Form() 
            success = True
            message = "Datos Guardados Correctamente"
            return render(request,'Contactos_Proyecto_Form.html', {'formulario':formulario, 'mensaje':message})
    else:
        formulario = Contactos_Proyecto_Form()
    return render(request,'Contactos_Proyecto_Form.html', {'formulario':formulario})


# class Registro_Proyecto_View(View):
#     def get(self, request):
#         user_form = UserForm(instance=request.user)
#         profile_form = UserProfileForm(instance=request.user.profile)
#         return render(request, 'profiles/profile.html', {
#             'user_form': user_form,
#             'profile_form': profile_form
#         })
# 
#     def post(self, request):
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = UserProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, _('Your profile was successfully updated!'))
#             return redirect('settings:profile')

# class Registro_Proyecto_View(MultiFormsView):
#     template_name = 'Decreto_143_18/plantillas/Registro_Proyecto.html'
#     success_url = '/'
#     form_class = {
#         'dragon': Empresa_Datos_Formales_Form,
#         'unicornio': Empresa_FIT_Form
#     }

class Registro_Proyecto_View(MultipleFormsView):
    template_name = 'forms.html'
    success_url = reverse_lazy('RegistroEmpresa')

    # here we specify all forms that should be displayed
    forms_classes = [
        forms.Empresa_Datos_Formales_Form,
        forms.Empresa_FIT_Form,
        forms.Expediente_Dec_143_18_Form,
        forms.Localizacion_Proyecto_Form,
        forms.Ind_Gral_Empleo_Form,
        forms.Ind_Gral_Exportaciones_Form,
        forms.Ind_Gral_Localizacion_Form,
        forms.Ind_Gral_TL_Form,
        forms.Ind_Gral_IDi_Form,
        forms.Ind_Sect_Formacion_Continua_Form,
        forms.Ind_Sect_Diferenciacion_Prod_Proc_Form,
        forms.Ind_Sect_Energia_Renovable_Form,
        forms.Ind_Sect_Mercado_Capitales_Form,
        forms.Propietarios_Directores_Representantes_Form,
        forms.Contactos_Proyecto_Form,
        forms.Cuadro_Inversiones_Empresa_Form
        
    ]
    
    def get_forms_classes(self):
        # we hide staff_only forms from not-staff users
        # our goal no. 3 about dynamic amount list of forms 
        forms_classes = super(Registro_Proyecto_View, self).get_forms_classes()
        user = self.request.user
        if not user.is_authenticated or not user.is_staff:
            return list(filter(lambda form: not getattr(form, 'staff_only', False), self.forms_classes))
        return forms_classes

    def form_valid(self, form): 
        print("yay it's valid!")
        form.save()
        return super(Registro_Proyecto_View, self).form_valid(form)

    class Meta:
        verbose_name='Formulario'


class Empresa_Datos_Formales_List(ListView):
    template_name = "Lista_Empresa_Datos_Formales.html"
    model = Empresa_Datos_Formales
    context_object_name = "c"

class MiListaMultiple(TemplateView):
    template_name = 'ListaMultiplesEmpresas.html'
    exp=[]
    #if 'Proyectos[]' != None:
        #exp = 'Proyectos[]'
    
    def get_context_data(self, *args, **kwargs):
        media = '/media/'
        context = super().get_context_data(*args, **kwargs)
        exp=[]
        
        #Proyectos = context['Proyectos']
        # if 'Proyectos' != None:
        #     exp = 'Proyectos'
        #exp = context.kwargs['Proyectos'].encode('utf-8')
        qs0 = Expediente_Dec_143_18.objects.all() #Sin Filtros
        #Aplicar Filtros
        qs1 = Empresa_Datos_Formales.objects.all() #your first qs
        qs2 = Empresa_FIT.objects.all() #your second qs
        qs3 = Expediente_Dec_143_18.objects.all() #filter(num_expediente='Proyectos')
        qs4 = Localizacion_Proyecto.objects.all()
        qs5 = Ind_Gral_Empleo.objects.all()
        qs6 = Ind_Gral_Exportaciones.objects.all()
        qs7 = Ind_Gral_Localizacion.objects.all()
        qs8 = Ind_Gral_TL.objects.all()
        qs9 = Ind_Gral_IDi.objects.all()
        qs10 = Ind_Sect_Formacion_Continua.objects.all()
        qs11 = Ind_Sect_Diferenciacion_Prod_Proc.objects.all()
        qs12 = Ind_Sect_Energia_Renovable.objects.all()
        qs13 = Ind_Sect_Mercado_Capitales.objects.all()
        qs14 = Propietarios_Directores_Representantes.objects.all()
        qs15 = Contactos_Proyecto.objects.all()
        qs16 = Cuadro_Inversiones_Empresa.objects.all()
        
        
        return {'Expediente':exp,'Expediente_Dec_143_18_Total': qs0, 'Empresas_Datos_Formales': qs1, 'Empresa_FIT': qs2, 'Expediente_Dec_143_18': qs3, 'Localizacion_Proyecto': qs4, 'Ind_Gral_Empleo':qs5, 'Ind_Gral_Exportaciones':qs6, 'Ind_Gral_Localizacion':qs7, 'Ind_Gral_TL':qs8, 'Ind_Gral_IDi':qs9, 'Ind_Sect_Formacion_Continua':qs10, 'Ind_Sect_Diferenciacion_Prod_Proc':qs11, 'Ind_Sect_Energia_Renovable':qs12, 'Ind_Sect_Mercado_Capitales':qs13, 'Propietarios_Directores_Representantes':qs14, 'Contactos_Proyecto':qs15, 'Cuadro_Inversiones_Empresa':qs16, 'ruta': media}
#     def get(self,request,*args, **kwargs):
#         return request.Proyectos
class MiListaMultiple1(View):
    
    def get(self, request, *args, **kwargs):
        media = '/media/'
        
        clave=[]
        expediente=[]
        rsocial=[]       
        if request.method == 'GET':
            clave = request.GET.getlist('Proyectos[]') #['Proyectos'] .encode('latin') #.encode('utf-8')
        elif request.method == 'POST':
            clave = request.POST['Proyectos']  
        if clave != []:
            #clave=clave[0]
            for i in clave:
                expediente.append(int(i.split(sep="_")[1]))
                rsocial.append(i.split(sep="_")[0])
                
#         expediente=int(clave.split(sep="_")[1])
#         rsocial=clave.split(sep="_")[0]    
            
            
        #exp = context.kwargs['Proyectos'].encode('utf-8')
        qs0 = Expediente_Dec_143_18.objects.all() #Sin Filtros
        #Aplicar Filtros
        qs1 = Empresa_Datos_Formales.objects.filter(razon_social__in=rsocial) #your first qs
        qs2 = Empresa_FIT.objects.filter(num_expediente__in=expediente) #your second qs
        qs3 = Expediente_Dec_143_18.objects.filter(num_expediente__in=expediente) #filter(num_expediente=exp) all()
        qs4 = Localizacion_Proyecto.objects.filter(razon_social_num_exp__in=expediente)
        qs5 = Ind_Gral_Empleo.objects.filter(proyecto__in=expediente)
        qs6 = Ind_Gral_Exportaciones.objects.filter(proyecto__in=expediente)
        qs7 = Ind_Gral_Localizacion.objects.filter(proyecto__in=expediente)
        qs8 = Ind_Gral_TL.objects.filter(proyecto__in=expediente)
        qs9 = Ind_Gral_IDi.objects.filter(proyecto__in=expediente)
        qs10 = Ind_Sect_Formacion_Continua.objects.filter(proyecto__in=expediente)
        qs11 = Ind_Sect_Diferenciacion_Prod_Proc.objects.filter(proyecto__in=expediente)
        qs12 = Ind_Sect_Energia_Renovable.objects.filter(proyecto__in=expediente)
        qs13 = Ind_Sect_Mercado_Capitales.objects.filter(proyecto__in=expediente)
        qs14 = Propietarios_Directores_Representantes.objects.filter(proyecto__in=expediente)
        qs15 = Contactos_Proyecto.objects.filter(proyecto__in=expediente)
        qs16 = Cuadro_Inversiones_Empresa.objects.filter(proyecto__in=expediente)
        context = {'rs':rsocial, 'exp':expediente, 'Expediente':clave,'Expediente_Dec_143_18_Total': qs0, 'Empresas_Datos_Formales': qs1, 'Empresa_FIT': qs2, 'Expediente_Dec_143_18': qs3, 'Localizacion_Proyecto': qs4, 'Ind_Gral_Empleo':qs5, 'Ind_Gral_Exportaciones':qs6, 'Ind_Gral_Localizacion':qs7, 'Ind_Gral_TL':qs8, 'Ind_Gral_IDi':qs9, 'Ind_Sect_Formacion_Continua':qs10, 'Ind_Sect_Diferenciacion_Prod_Proc':qs11, 'Ind_Sect_Energia_Renovable':qs12, 'Ind_Sect_Mercado_Capitales':qs13, 'Propietarios_Directores_Representantes':qs14, 'Contactos_Proyecto':qs15, 'Cuadro_Inversiones_Empresa':qs16, 'ruta': media}
        return render(request, 'ListaMultiplesEmpresas.html', context=context)
            
# class MiListaMultiple(ListView):
#     template_name = 'ListaMultiplesEmpresas.html'
#     def get_queryset(self):
#         qs1 = Empresa_Datos_Formales.objects.all() #your first qs
#         qs2 = Empresa_FIT.objects.all() #your second qs
#         qs3 = Expediente_Dec_143_18.objects.all()
#         qs4 = Localizacion_Proyecto.objects.all()
#         
#         #you can add as many qs as you want
#         queryset = sorted(chain(qs1,qs2,qs3,qs4),key=attrgetter('timestamp')),
#         return queryset

def generar_pdf(request):
    #print "Genero el PDF"
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "Empresa_Datos_Formales.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    response['Content-Disposition'] = 'attachment; filename=Empresa_Datos_Formales.pdf' #% pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=landscape(A4),
                            rightMargin=10,
                            leftMargin=10,
                            topMargin=60,
                            bottomMargin=18,
                            )
    datos = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de Empresa", styles['Normal'])
    datos.append(header)
    headings = (        'raz_soc',
                        'nom_com',
                        'rut',
                        'num_bps',
                        'num_mtss',
                        'dom_cons',
                        'dom_fis',
                        'tel',
                        'email',
                        'celular',
                        'c_giro_c',
                        'nom_giro',
                        'f_bal',
                        'tipo' )
    alldatos = [(p.razon_social,
                        p.nombre_comercial,
                        p.rut,
                        p.num_bps,
                        p.num_mtss,
                        p.domicilio_constituido,
                        p.domicilio_fiscal,
                        p.telefono,
                        p.email,
                        p.celular,
                        p.cod_giro_ciiu,
                        p.nombre_giro,
                        p.fecha_balance,
                        p.tipo ) for p in Empresa_Datos_Formales.objects.all()]

    print (alldatos)

    t = Table([headings] + alldatos, colWidths=60, rowHeights=50, style=None )
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))
    datos.append(t)
    doc.build(datos)
    response.write(buff.getvalue())
    buff.close()
    return response


def crear_pdf(request, pk):
    # Obtenemos un queryset, para un determinado libro usando pk.
    try:
        qs1 = Empresa_Datos_Formales.objects.get(id=pk) #your first qs
        qs2 = Empresa_FIT.objects.get(id=pk) #your second qs
        qs3 = Expediente_Dec_143_18.objects.get(id=pk)
        qs4 = Localizacion_Proyecto.objects.get(id=pk)
        qs5 = Ind_Gral_Empleo.objects.get(id=pk)
        qs6 = Ind_Gral_Exportaciones.objects.get(id=pk)
        qs7 = Ind_Gral_Localizacion.objects.get(id=pk)
        qs8 = Ind_Gral_TL.objects.get(id=pk)
        qs9 = Ind_Gral_IDi.objects.get(id=pk)
        qs10 = Ind_Sect_Formacion_Continua.objects.get(id=pk)
        qs11 = Ind_Sect_Diferenciacion_Prod_Proc.objects.get(id=pk)
        qs12 = Ind_Sect_Energia_Renovable.objects.get(id=pk)
        qs13 = Ind_Sect_Mercado_Capitales.objects.get(id=pk)
        qs14 = Propietarios_Directores_Representantes.objects.get(id=pk)
        qs15 = Contactos_Proyecto.objects.get(id=pk)
        qs16 = Cuadro_Inversiones_Empresa.objects.get(id=pk)
    except ValueError:
        raise Http404()
    # Creamos un objeto HttpResponse con las cabeceras del PDF correctas.
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "Empresa_Lista_Multiple.pdf"
    # Nos aseguramos que el navegador lo abra directamente.
    response['Content-Disposition'] = 'filename=%pdf_name'
    buffer = BytesIO()

    # Creamos el objeto PDF, usando el objeto BytesIO como si fuera un "archivo".
    p = canvas.Canvas(buffer)

    # Dibujamos cosas en el PDF. Aqui se genera el PDF.
    # Consulta la documentación de ReportLab para una lista completa de funcionalidades.
    p.drawString(100, 800, "Razon Social: " + str(qs1.razon_social))
    p.drawString(100, 780, "Nombre Comercial: " + str(qs1.nombre_comercial))
    p.drawString(100, 760, "RUT: " +  str(qs1.rut))
    #p.drawImage(str(libro.portada.url), 100, 150, width=400, height=600)

    # Cerramos limpiamente el objeto PDF.
    p.showPage()
    p.save()

    # Traemos  el valor de el bufer BytesIO y escribimos la respuesta.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response



def getPDF(request):
    """Returns PDF as a binary stream."""

    if 'q' in request.GET:
            
        rml = getRML(request.GET['q'])  
    
        buf = StringIO()
        
        #create the pdf
        rml2pdf.go(rml, outputFileName=buf)
        buf.reset()
        pdfData = buf.read()
        
        #send the response
        response = HttpResponse(mimetype='application/pdf')
        response.write(pdfData)
        response['Content-Disposition'] = 'attachment; filename=output.pdf'
        return response

def getRML(name):
    """We used django template to write the RML, but you could use any other
    template language of your choice. 
    """
    t = Template(open('ListaMultiplesEmpresas.html').read())
    c = Context({"name": name})
    rml = t.render(c)
    #django templates are unicode, and so need to be encoded to utf-8
    return rml.encode('utf8')






