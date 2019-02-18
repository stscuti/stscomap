from Decreto_143_18.models import Empresa_Datos_Formales
from Decreto_143_18.models import Tipo_Contribuyente
from Decreto_143_18.models import Empresa_FIT
from Decreto_143_18.models import Tipo_Inversiones
from Decreto_143_18.models import Expediente_Dec_143_18
from Decreto_143_18.models import Localizacion_Proyecto
from Decreto_143_18.forms import Empresa_Datos_Formales_Form
from Decreto_143_18.forms import Tipo_Contribuyente_Form
from Decreto_143_18.forms import Empresa_FIT_Form
from Decreto_143_18.forms import Tipo_Inversiones_Form
from Decreto_143_18.forms import Expediente_Dec_143_18_Form
from Decreto_143_18.forms import Localizacion_Proyecto_Form
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMessage

# Create your views here.
def Nuevo_Empresa_Datos_Formales(request):
    if request.method=='POST':
        formulario = Empresa_Datos_Formales_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/Decreto_143_18')
    else:
        formulario=Empresa_Datos_Formales_Form()
    return render_to_response('Empresa_Datos_Formales_Form.html', {'formulario':formulario})


































