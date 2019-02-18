from django.contrib import admin
from .models import Empresa_Datos_Formales  
from .models import Tipo_Contribuyente
from .models import Empresa_FIT
from .models import Tipo_Inversiones
from .models import Expediente_Dec_143_18
from .models import Localizacion_Proyecto



# Register your models here.
admin.site.register(Localizacion_Proyecto)
admin.site.register(Empresa_Datos_Formales)
admin.site.register(Tipo_Contribuyente)
admin.site.register(Empresa_FIT)
admin.site.register(Expediente_Dec_143_18)
admin.site.register(Tipo_Inversiones)


