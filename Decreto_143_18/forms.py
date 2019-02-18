from django.forms import ModelForm
from django import forms
from Decreto_143_18.models import Empresa_Datos_Formales
from Decreto_143_18.models import Tipo_Contribuyente
from Decreto_143_18.models import Empresa_FIT
from Decreto_143_18.models import Tipo_Inversiones
from Decreto_143_18.models import Expediente_Dec_143_18
from Decreto_143_18.models import Localizacion_Proyecto

class Empresa_Datos_Formales_Form(ModelForm):
    class Meta:
        model=Empresa_Datos_Formales
        fields = '__all__'
class Tipo_Contribuyente_Form(ModelForm):
    class Meta:
        model=Tipo_Contribuyente
        fields = '__all__'
class Empresa_FIT_Form(ModelForm):
    class Meta:
        model=Empresa_FIT
        fields = '__all__'
class Tipo_Inversiones_Form(ModelForm):
    class Meta:
        model=Tipo_Inversiones
        fields = '__all__'
class Expediente_Dec_143_18_Form(ModelForm):
    class Meta:
        model=Expediente_Dec_143_18
        fields = '__all__'
class Localizacion_Proyecto_Form(ModelForm):
    class Meta:
        model=Localizacion_Proyecto
        fields = '__all__'









































