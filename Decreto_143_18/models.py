from PIL import Image
from django.db import models
from django.utils import timezone
from model_utils import Choices
# Create your models here.


class Tipo_Inversiones(models.Model):
    lista=(('Maquinaria','Maquinaria'),('Equipos','Equipos'),('Instalaciones','Instalaciones'),('Materiales','Materiales'),('Mano de Obra','Mano de Obra'),('Leyes Sociales','Leyes Sociales'),('Honorarios','Honorarios'))
    #tipo = models.CharField(choices=lista, max_length=100)
    tipo = models.CharField(choices=lista, max_length=100, default='Maquinaria',unique=True)
    grupo1 = models.CharField(max_length=100, unique=True, default='Maquinaria y Equipos')
    grupo2 = models.CharField(max_length=100, unique=True, default='Maquinaria, Equipos e Instalaciones')
    def __str__(self):
        return self.tipo


class Tipo_Contribuyente(models.Model):
    tipo = models.CharField(max_length=100, unique=True, default='Con contabilidad Suficiente')
    def __str__(self):
        return self.tipo
class Empresa_Datos_Formales(models.Model):
    razon_social = models.CharField(max_length=100)
    nombre_comercial = models.CharField(max_length=100)
    rut = models.DecimalField(max_digits=10, decimal_places=0)
    num_bps = models.DecimalField(max_digits=10, decimal_places=0)
    num_mtss = models.DecimalField(max_digits=10, decimal_places=0)
    domicilio_constituido = models.CharField(max_length=200)
    domicilio_fiscal = models.CharField(max_length=200)
    telefono = models.DecimalField(max_digits=8, decimal_places=0)
    email = models.EmailField(max_length=200)
    celular = models.DecimalField(max_digits=9, decimal_places=0)
    cod_giro_ciiu = models.DecimalField(max_digits=10, decimal_places=0)
    nombre_giro = models.CharField(max_length=200)
    fecha_balance = models.DateField(auto_now=False, auto_now_add=False)
    tipo = models.ForeignKey(Tipo_Contribuyente, on_delete=models.CASCADE)
    def __str__(self):
        return self.razon_social

class Empresa_FIT(models.Model):
    razon_social= models.ForeignKey(Empresa_Datos_Formales, on_delete=models.CASCADE)
    num_expediente=models.DecimalField(max_digits=10, decimal_places=0)
    documento_fit=models.ImageField()
    sin_facturacion_ult3ej=models.BooleanField()
    empresa_vinculada=models.BooleanField()
    empresa_vinculada_sfult3ej=models.BooleanField()
    beneficio_MYPE =models.BooleanField()
    cantidad_empleados=models.DecimalField(max_digits=10, decimal_places=4)
    ventas_netas_UI=models.DecimalField(max_digits=14, decimal_places=4)
    ventas_netas_Pesos=models.DecimalField(max_digits=14, decimal_places=4)
    empresa_controlada=models.BooleanField()
    empresa_controlada_supera_MYPE=models.BooleanField()
    pertenece_grupo_economico=models.BooleanField()
    grupo_economico_supera_MYPE=models.BooleanField()
    proyeccion_empleos_siguiente_ejercicio=models.DecimalField(max_digits=10, decimal_places=4)
    proyeccion_ventas_UI_siguiente_ejercicio=models.DecimalField(max_digits=10, decimal_places=4)
    declaro_geco_controlantes_MYPE=models.BooleanField()
    aportes_patronales_art28=models.BooleanField()
    usuario_parque_industrial=models.BooleanField()
    objetivo_proyecto=models.CharField(max_length=150)
    descripcion_ampliada=models.CharField(max_length=500)
    monto_inversion_UI=models.DecimalField(max_digits=14, decimal_places=4)
    tc_Dolar=models.DecimalField(max_digits=8, decimal_places=4)
    tc_Euro=models.DecimalField(max_digits=8, decimal_places=4)
    tc_UI=models.DecimalField(max_digits=8, decimal_places=4)
    anos_ejecucion_inversion=models.DecimalField(max_digits=2, decimal_places=0)
    beneficio_IRAE=models.BooleanField()
    beneficio_IP=models.BooleanField()
    beneficio_IVA=models.BooleanField()
    beneficio_tributos_importacion=models.BooleanField()
    beneficio_transitorios=models.BooleanField()
    indicadores_generales_empleo=models.BooleanField()
    indicadores_generales_exportaciones=models.BooleanField()
    indicadores_generales_descentralizacion=models.BooleanField()
    indicadores_generales_TL=models.BooleanField()
    indicadores_generales_IDi=models.BooleanField()
    indicadores_sectoriales_mef_formacion=models.BooleanField()
    indicadores_sectoriales_mef_diferenciacion=models.BooleanField()
    indicadores_sectoriales_mef_renovables=models.BooleanField()
    indicadores_sectoriales_mef_capitales=models.BooleanField()
    def __str__(self):
        return self.razon_social + '_' + self.num_expediente
    
class Localizacion_Proyecto(models.Model):
    razon_social_num_exp= models.ForeignKey(Empresa_FIT, on_delete=models.CASCADE)
    departamento=models.CharField(max_length=50)
    localidad=models.CharField(max_length=100)
    direccion=models.CharField(max_length=150)
    vinculo_juridico_inversor_predio=models.CharField(max_length=50)
    
    
class Expediente_Dec_143_18(models.Model):
    razon_social=models.ForeignKey(Empresa_Datos_Formales, on_delete=models.CASCADE)
    num_expediente=models.ForeignKey(Empresa_FIT, on_delete=models.CASCADE)
    fecha_presentacion=models.DateTimeField(auto_now_add=True)
    documento_fit=models.ImageField()
    documento_carta_compromiso=models.ImageField()
    documento_certificado_notarial=models.ImageField()
    documento_formulario_bcu=models.ImageField()
    documento_estados_contables=models.ImageField()
    documento_constancia_DINAPYME=models.ImageField()
    documento_dj_IRAE=models.ImageField()
    documento_constancia_CIIU=models.ImageField()
    documento_certificado_DINAMA=models.ImageField()
    documento_plan_uso_suelos_DGRN=models.ImageField()
    documento_formulario_ANII_IDi=models.ImageField()
    documento_catalogos_ANII_IDi=models.ImageField()
    documento_formulario_TL=models.ImageField()
    documento_catalogo_TL=models.ImageField()
    documento_formulario_sectorial_FCC=models.ImageField()
    documento_programa_sectorial_FCC=models.ImageField()
    documento_formulario_sectorial_MC=models.ImageField()
    documento_constancia_COMAP=models.ImageField()
    documento_certificado_unico_DGI=models.ImageField()
    documento_certificado_unico_BPS=models.ImageField()
    inversiones_documento_cuadro=models.ImageField()
    numero_inversiones_documento_cuadro=models.DecimalField(max_digits=10, decimal_places=0)
    inversiones_documento_cronograma=models.ImageField()
    numero_inversiones_documento_cronograma=models.DecimalField(max_digits=10, decimal_places=0)
    inversiones_documento_plan_implantacion=models.ImageField()
    inversiones_documento_memoria_constructiva=models.ImageField()
    inversiones_documento_rubrado_obra_imagen=models.ImageField()
    inversiones_documento_rubrado_obra_excel=models.ImageField()
    inversiones_documento_anteproyecto_arquitectura=models.ImageField()
    inversiones_documento_contrato_arrendamiento=models.ImageField()
    def __str__(self):
        return self.razon_social + '_' + self.num_expediente + '_' + self.fecha_presentacion
    
    
    

