from PIL import Image
from django.db import models
from django.utils import timezone
from model_utils import Choices
from unittest.util import _MAX_LENGTH
import os
from django.utils.deconstruct import deconstructible
import uuid
# Create your models here.


class Tipo_Inversiones(models.Model):
    lista=(('Maquinaria','Maquinaria'),('Equipos','Equipos'),('Instalaciones','Instalaciones'),('Materiales','Materiales'),('Mano de Obra','Mano de Obra'),('Leyes Sociales','Leyes Sociales'),('Honorarios','Honorarios'))
    #tipo = models.CharField(choices=lista, max_length=100)
    tipo = models.CharField(choices=lista, max_length=100, default='Maquinaria',unique=True,verbose_name='Tipo de Inversion')
    grupo1 = models.CharField(max_length=100, default='Maquinaria y Equipos',verbose_name='Grupo de Tipo de Inversion 1')
    grupo2 = models.CharField(max_length=100, default='Maquinaria, Equipos e Instalaciones',verbose_name='Grupo de Tipo de Inversion 2')
    def __str__(self):
        return self.tipo
    class Meta:
        unique_together = ('tipo', 'grupo1','grupo2')
        verbose_name = "Tipo de Inversiones"
        verbose_name_plural = "Tipo de Inversiones"

class Tipo_Contribuyente(models.Model):
    tipo = models.CharField(max_length=100, unique=True, default='Con contabilidad Suficiente',verbose_name='Tipo de Contribuyente')
    def __str__(self):
        return self.tipo
    class Meta:
        verbose_name = "Tipo de Contribuyente"
        verbose_name_plural = "Tipo de Contribuyente"
        
class Empresa_Datos_Formales(models.Model):
    razon_social = models.CharField(max_length=100,verbose_name='Razon Social',primary_key=True)
    nombre_comercial = models.CharField(max_length=100,verbose_name='Nombre Comercial')
    rut = models.DecimalField(max_digits=12, decimal_places=0,verbose_name='Numero de RUT', unique=True)
    num_bps = models.DecimalField(max_digits=10, decimal_places=0,verbose_name='Numero de BPS')
    num_mtss = models.DecimalField(max_digits=15, decimal_places=0,verbose_name='Numero de MTSS')
    domicilio_constituido = models.CharField(max_length=200,verbose_name='Domicilio Constituido')
    domicilio_fiscal = models.CharField(max_length=200,verbose_name='Domicilio Fiscal')
    telefono = models.DecimalField(max_digits=8, decimal_places=0,verbose_name='Telefono')
    email = models.EmailField(max_length=200,verbose_name='Direccion de Email')
    celular = models.DecimalField(max_digits=9, decimal_places=0,verbose_name='Numero de Celular')
    cod_giro_ciiu = models.DecimalField(max_digits=10, decimal_places=0,verbose_name='Codigo del Giro CIIU')
    nombre_giro = models.CharField(max_length=200,verbose_name='Descripcion del Giro CIIU')
    fecha_balance = models.DateField(auto_now=False, auto_now_add=False,verbose_name='Fecha de Balance de la Empresa')
    tipo = models.ForeignKey(Tipo_Contribuyente, on_delete=models.CASCADE,verbose_name='Tipo')
    timestamp = models.DateField(default=timezone.now)
    def __str__(self):
        return self.razon_social
    class Meta:
        
        verbose_name = "Datos Formales de la Empresa"
        verbose_name_plural = "Datos Formales de la Empresa"
        


class Empresa_FIT(models.Model):
    
    def Incrementar():
        #ultimo = Empresa_FIT.objects.all().order_by('id').last()
        ultimo = Empresa_FIT.objects.all().order_by('num_expediente').last()
        start = 80000
        if not ultimo:
            return int(start)
        registro = ultimo.num_expediente
        registro_int = ultimo.num_expediente
        nuevo_registro_int = registro_int + 1
        return nuevo_registro_int
    
    num_expediente=models.BigIntegerField(default=Incrementar, verbose_name='Numero de Expediente',primary_key=True)
    razon_social= models.ForeignKey(Empresa_Datos_Formales, on_delete=models.CASCADE,verbose_name='Razon Social')
    def get_expediente_url(self, filename):
        
        return "media/Expedientes/%(numero_expediente)s/%(filename)s" % {
            'numero_expediente': self.num_expediente,
            'filename': filename,
        }
    
    
    documento_fit=models.FileField(verbose_name='Documento del Formulario de Inicio de Tramite',upload_to=get_expediente_url)
    sin_facturacion_ult3ej=models.BooleanField(verbose_name='Empresa sin facturacion los ultimos 3 ejercicios')
    empresa_vinculada=models.BooleanField(verbose_name='Tiene Empresas Vinculadas')
    empresa_vinculada_sfult3ej=models.BooleanField(verbose_name='Tiene Empresas Vinculadas sin facturacion los ultimos 3 ejercicios')
    beneficio_MYPE =models.BooleanField(verbose_name='Solicita Beneficio PYME')
    cantidad_empleados=models.DecimalField(max_digits=10, decimal_places=4,verbose_name='Cantidad de Empleados')
    ventas_netas_UI=models.DecimalField(max_digits=14, decimal_places=4, verbose_name='Ventas Netas Anuales en UI')
    ventas_netas_Pesos=models.DecimalField(max_digits=14, decimal_places=4, verbose_name='Ventas Netas Anuales en Pesos')
    empresa_controlada=models.BooleanField(verbose_name='Tiene Empresas Controladas')
    empresa_controlada_supera_MYPE=models.BooleanField(verbose_name='Alguna Empresa Controlada supera el limite de MYPE')
    pertenece_grupo_economico=models.BooleanField(verbose_name='Pertenece a un Grupo Economico')
    grupo_economico_supera_MYPE=models.BooleanField(verbose_name='Alguna Empresa del Grupo Economico supera el limite de MYPE')
    proyeccion_empleos_siguiente_ejercicio=models.DecimalField(max_digits=10, decimal_places=4, verbose_name='Proyeccion de Empleos del siguiente Ejercicio')
    proyeccion_ventas_UI_siguiente_ejercicio=models.DecimalField(max_digits=14, decimal_places=4, verbose_name='Proyeccion de Ventas Anuales en UI al siguiente Ejercicio')
    declaro_geco_controlantes_MYPE=models.BooleanField(verbose_name='Declaro que Grupo Economico/Controlantes cumplen condiciones MYPE')
    aportes_patronales_art28=models.BooleanField(verbose_name='Aplica credito fiscal por aportes patronales de articulo 28')
    usuario_parque_industrial=models.BooleanField(verbose_name='Usuario de Parque Industrial')
    objetivo_proyecto=models.CharField(max_length=150, verbose_name='Objetivo del Proyecto')
    descripcion_ampliada=models.TextField(verbose_name='Descripcion ampliada del Objetivo del Proyecto')
    monto_inversion_UI=models.DecimalField(max_digits=14, decimal_places=4, verbose_name='Monto de la Inversion en UI')
    tc_Dolar=models.DecimalField(max_digits=8, decimal_places=4,verbose_name='Tipo de Cambio: Dolar utilizado')
    tc_Euro=models.DecimalField(max_digits=8, decimal_places=4,verbose_name='Tipo de Cambio: EURO utilizado')
    tc_UI=models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Tipo de Cambio: UI utilizada')
    anos_ejecucion_inversion=models.DecimalField(max_digits=2, decimal_places=0,verbose_name='Plazo de Anos de Ejecucion de la Inversion')
    beneficio_IRAE=models.BooleanField(verbose_name='Solicita Beneficio IRAE')
    beneficio_IP=models.BooleanField(verbose_name='Solicita Beneficio IP')
    beneficio_IVA=models.BooleanField(verbose_name='Solicita Beneficio IVA')
    beneficio_tributos_importacion=models.BooleanField(verbose_name='Solicita Beneficios Tributarios a la Importacion')
    beneficio_transitorios=models.BooleanField(verbose_name='Solicita Beneficios Transitorios')
    indicadores_generales_empleo=models.BooleanField(verbose_name='Utiliza Indicador General de Empleo')
    indicadores_generales_exportaciones=models.BooleanField(verbose_name='Utiliza Indicador General de Exportaciones')
    indicadores_generales_descentralizacion=models.BooleanField(verbose_name='Utiliza Indicador General de Descentralizacion')
    indicadores_generales_TL=models.BooleanField(verbose_name='Utiliza Indicador General de Tecnologias Limpias')
    indicadores_generales_IDi=models.BooleanField(verbose_name='Utiliza Indicador General de Investigacion, Desarrollo e innovacion')
    indicadores_sectoriales_mef_formacion=models.BooleanField(verbose_name='Utiliza Indicador Sectorial de Formacion Continua y Capacitacion')
    indicadores_sectoriales_mef_diferenciacion=models.BooleanField(verbose_name='Utiliza Indicador Sectorial de Diferenciacion de Productos y Procesos')
    indicadores_sectoriales_mef_renovables=models.BooleanField(verbose_name='Utiliza Indicador Sectorial de Energias Renovables')
    indicadores_sectoriales_mef_capitales=models.BooleanField(verbose_name='Utiliza Indicador Sectorial de Mercado de Capitales')
    timestamp = models.DateField(default=timezone.now)
    def __str__(self):
        return self.razon_social.razon_social + '_' + str(self.num_expediente) 
    class Meta:
        unique_together = ('razon_social', 'num_expediente')
        verbose_name = 'Empresa: Datos del Formulario Inicio de Tramite'
        verbose_name_plural = 'Empresa: Datos del Formulario Inicio de Tramite'
        
    
    
class Localizacion_Proyecto(models.Model):
    razon_social_num_exp= models.ForeignKey(Empresa_FIT, on_delete=models.CASCADE, verbose_name='Razon Social + Numero de Expediente')
    departamento=models.CharField(max_length=50, verbose_name='Departamento')
    localidad=models.CharField(max_length=100, verbose_name='Localidad')
    direccion=models.CharField(max_length=150, verbose_name='Direccion')
    vinculo_juridico_inversor_predio=models.CharField(max_length=50, verbose_name='Con mejoras fijas - vinculacion juridica entre inversor y predio:')
    timestamp = models.DateField(default=timezone.now)
    def __str__(self):
        return self.direccion
    class Meta:
        unique_together = ('razon_social_num_exp', 'direccion')
        verbose_name = 'Localizacion del Proyecto'
        verbose_name_plural = 'Localizacion del Proyecto'
        
class Expediente_Dec_143_18(models.Model):
    #razon_social= models.ForeignKey(Empresa_Datos_Formales, on_delete=models.CASCADE, verbose_name='Razon Social')
    num_expediente=models.ForeignKey(Empresa_FIT, on_delete=models.CASCADE, verbose_name='Numero de Expediente', primary_key=True)
    def get_expediente_url(self, filename):
        
        return "media/Expedientes/%(numero_expediente)s/%(filename)s" % {
            'numero_expediente': self.num_expediente.num_expediente,
            'filename': filename,
        }
    
    fecha_presentacion=models.DateField(default=timezone.now, verbose_name='Fecha de Presentacion del Proyecto en V.U.')
    #documento_fit=models.FileField(verbose_name='Documento de Formulario de Inicio de Tramite',upload_to=get_expediente_url)
    documento_carta_compromiso=models.FileField(verbose_name='Documento Carta de Compromiso',upload_to=get_expediente_url)
    documento_certificado_notarial=models.FileField(verbose_name='Documento Certificado Notarial',upload_to=get_expediente_url)
    documento_formulario_bcu=models.FileField(verbose_name='Documento Formulario BCU',upload_to=get_expediente_url)
    documento_estados_contables=models.FileField(verbose_name='Documento Estados Contables',upload_to=get_expediente_url)
    documento_constancia_DINAPYME=models.FileField(verbose_name='Documento Constancia DINAPYME', null=True, blank=True, upload_to=get_expediente_url)
    documento_dj_IRAE=models.FileField(verbose_name='Documento Declaracion Jurada de IRAE',null=True, blank=True,upload_to=get_expediente_url)
    documento_constancia_CIIU=models.FileField(verbose_name='Documento Constancia CIIU',null=True, blank=True,upload_to=get_expediente_url)
    documento_certificado_DINAMA=models.FileField(verbose_name='Documento Certificado DINAMA',null=True, blank=True,upload_to=get_expediente_url)
    documento_plan_uso_suelos_DGRN=models.FileField(verbose_name='Documento Plan de Uso de Suelos',null=True, blank=True,upload_to=get_expediente_url)
    documento_formulario_ANII_IDi=models.FileField(verbose_name='Documento Formulario ANII',null=True, blank=True,upload_to=get_expediente_url)
    documento_catalogos_ANII_IDi=models.FileField(verbose_name='Documento Catalgos de ANII',null=True, blank=True,upload_to=get_expediente_url)
    documento_formulario_TL=models.FileField(verbose_name='Documento Formulario de Tecnologias Limpias',null=True, blank=True,upload_to=get_expediente_url)
    documento_catalogo_TL=models.FileField(verbose_name='Documento Catalogo de Tecnologias Limpias',null=True, blank=True,upload_to=get_expediente_url)
    documento_formulario_sectorial_FCC=models.FileField(verbose_name='Documento Formulario de Indicador Sectorial de Formacion Continua y Capacitacion',null=True, blank=True,upload_to=get_expediente_url)
    documento_programa_sectorial_FCC=models.FileField(verbose_name='Documento Programa de Indicador Sectorial de Formacion Continua y Capacitacion',null=True, blank=True,upload_to=get_expediente_url)
    documento_formulario_sectorial_MC=models.FileField(verbose_name='Documento Formulario Sectorial Mercado de Capitales',null=True, blank=True,upload_to=get_expediente_url)
    documento_constancia_COMAP=models.FileField(verbose_name='Documento Constancia COMAP',upload_to=get_expediente_url)
    documento_certificado_unico_DGI=models.FileField(verbose_name='Documento Certificado Unico DGI',upload_to=get_expediente_url)
    documento_certificado_unico_BPS=models.FileField(verbose_name='Documento Certificado Unico BPS',upload_to=get_expediente_url)
    inversiones_documento_cuadro=models.FileField(verbose_name='Documento Cuadro de Inversiones',upload_to=get_expediente_url)
    numero_inversiones_documento_cuadro=models.DecimalField(max_digits=10, decimal_places=0)
    inversiones_documento_cronograma=models.FileField(verbose_name='Documento Cronograma de Inversiones',upload_to=get_expediente_url)
    numero_inversiones_documento_cronograma=models.DecimalField(max_digits=10, decimal_places=0)
    inversiones_documento_plan_implantacion=models.FileField(verbose_name='Documento Plan Implantacion',null=True, blank=True, upload_to=get_expediente_url)
    inversiones_documento_memoria_constructiva=models.FileField(verbose_name='Documento Memoria Constructiva', null=True, blank=True, upload_to=get_expediente_url)
    inversiones_documento_rubrado_obra_imagen=models.FileField(verbose_name='Documento Rubrado de Obra',null=True, blank=True, upload_to=get_expediente_url)
    inversiones_documento_rubrado_obra_excel=models.FileField(verbose_name='Excel Rubrado de Obra',null=True, blank=True ,upload_to=get_expediente_url)
    inversiones_documento_anteproyecto_arquitectura=models.FileField(verbose_name='Documento Anteproyecto de Arquitectura',null=True, blank=True ,upload_to=get_expediente_url)
    inversiones_documento_contrato_arrendamiento=models.FileField(verbose_name='Documento Contrato de Arrendamiento',null=True, blank=True,upload_to=get_expediente_url)
    timestamp = models.DateField(default=timezone.now)
    def __str__(self):
        #return self.razon_social + '_' + self.num_expediente + '_' + self.fecha_presentacion
        return str(self.num_expediente.num_expediente) + '_' + str(self.fecha_presentacion)
    class Meta:
        #unique_together = ('num_expediente','fecha_presentacion')
        verbose_name = 'Empresa: Documentos del Formulario Inicio de Tramite'
        verbose_name_plural = 'Empresa: Documentos del Formulario Inicio de Tramite'
        
class Cuadro_Inversiones_Empresa(models.Model):
    lista_ej=(('Ejecutado','Ejecutado'),('Presupuesto','Presupuesto'))
    lista_imp=(('Importado','Importado'),('Plaza','Plaza'))
    lista_nuevo=(('Nuevo','Nuevo'),('Usado','Usado'))
    proyecto=models.ForeignKey(Expediente_Dec_143_18, on_delete=models.CASCADE, verbose_name='Proyecto')
    descripcion=models.CharField(max_length=200, verbose_name='Descripcion Inversion')
    tipo_inversion=models.ForeignKey(Tipo_Inversiones, on_delete=models.CASCADE, verbose_name='Tipo de Inversion')
    ejecucion=models.CharField(choices=lista_ej, max_length=30, default='Presupuesto', verbose_name='Ejecutado/Presupuesto')
    numero_documento=models.CharField(max_length=100, verbose_name='Numero de Documento de Comprobante',null=True, blank=True)
    indicador_relacionado=models.CharField(max_length=100, verbose_name='Indicador Relacionado',null=True, blank=True) #Poner Listado y clave foranea
    fecha=models.DateField(default=timezone.now, verbose_name='Fecha')
    compra=models.CharField(choices=lista_imp, max_length=30, default='Plaza', verbose_name='Plaza/Importado')
    nuevo_usado=models.CharField(choices=lista_nuevo, max_length=30, default='Nuevo', verbose_name='Nuevo/Usado')
    cantidad=models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Cantidad', default=1)
    proveedor=models.CharField(max_length=200, verbose_name='Proveedor')
    moneda_origen=models.CharField(max_length=200, verbose_name='Moneda Origen') #Poner Lista y asociar a cotizaciones
    costo_moneda_origen=models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Costo Moneda Origen')
    total_inversiones_UI=models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Total de Inversion en UI')
    vida_util_anos=models.PositiveIntegerField(verbose_name='Vida Util en Anos',null=True, blank=True)
    UI_utilizada=models.DecimalField(max_digits=8, decimal_places=4, verbose_name='UI utilizada')
    USD_utilizado=models.DecimalField(max_digits=8, decimal_places=4, verbose_name='USD utilizado')
    EUR_utilizado=models.DecimalField(max_digits=8, decimal_places=4, verbose_name='EURO utilizado',null=True, blank=True)
    def __str__(self):
        return self.tipo_inversion + '_' + self.descripcion
# Pueden haber varios del mismo
    class Meta:
        unique_together = ('proyecto', 'tipo_inversion','descripcion','numero_documento')
        verbose_name = 'Cuadro de Inversiones Empresa'
        verbose_name_plural = 'Cuadro de Inversiones Empresa'
        
class Cuadro_Inversiones_Definitivo(models.Model):
    lista_ej=(('Ejecutado','Ejecutado'),('Presupuesto','Presupuesto'))
    lista_imp=(('Importado','Importado'),('Plaza','Plaza'))
    lista_nuevo=(('Nuevo','Nuevo'),('Usado','Usado'))
    tipo_inversion_descripcion=models.ForeignKey(Cuadro_Inversiones_Empresa, on_delete=models.CASCADE, verbose_name='Descripcion de Tipo de Inversion')
    descripcion=models.CharField(max_length=200, verbose_name='Aclaracion Descripcion',null=True, blank=True)
    tipo_inversion=models.CharField(max_length=200, verbose_name='Tipo de Inversion')
    ejecucion=models.CharField(choices=lista_ej, max_length=30, default='Presupuesto', verbose_name='Ejecutado/Presupuesto')
    numero_documento=models.CharField(max_length=100, verbose_name='Numero de Documento')
    indicador_relacionado=models.CharField(max_length=100, verbose_name='Indicador Relacionado',null=True, blank=True) #Poner Listado y clave foranea
    fecha=models.DateField(default=timezone.now, verbose_name='Fecha')
    compra=models.CharField(choices=lista_imp, max_length=30, default='Plaza', verbose_name='Plaza/Importado')
    nuevo_usado=models.CharField(choices=lista_nuevo, max_length=30, default='Nuevo', verbose_name='Nuevo/Usado')
    cantidad=models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Cantidad')
    proveedor=models.CharField(max_length=200, verbose_name='Proveedor')
    moneda_origen=models.CharField(max_length=200, verbose_name='Moneda Origen') #Poner Lista y asociar a cotizaciones
    costo_moneda_origen=models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Costo Moneda Origen')
    total_inversiones_UI=models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Total Inversiones en UI')
    vida_util_anos=models.PositiveIntegerField(verbose_name='Vida Util en Anos',null=True, blank=True)
    UI_utilizada=models.DecimalField(max_digits=8, decimal_places=4, verbose_name='UI utilizada')
    USD_utilizado=models.DecimalField(max_digits=8, decimal_places=4, verbose_name='USD utilizado')
    EUR_utilizado=models.DecimalField(max_digits=8, decimal_places=4, verbose_name='EURO utilizado')
    tipo_inversion_definitiva=models.ForeignKey(Tipo_Inversiones, on_delete=models.CASCADE, verbose_name='Tipo de Inversion Definitiva')
    concepto_recategorizacion=models.CharField(max_length=100, verbose_name='Concepto Recategorizacion',null=True, blank=True) #Poner Listado y clave foranea
    observaciones=models.CharField(max_length=500, verbose_name='Observaciones',null=True, blank=True)
    UI_correspondiente=models.DecimalField(max_digits=8, decimal_places=4, verbose_name='UI correspondiente')
    USD_correspondiente=models.DecimalField(max_digits=8, decimal_places=4, verbose_name='USD correspondiente')
    EUR_correspondiente=models.DecimalField(max_digits=8, decimal_places=4, verbose_name='EURO correspondiente')
    costo_moneda_origen_elegible=models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Costo Moneda Origen Elegible')
    total_inversiones_UI_elegible=models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Total Inversiones en UI Elegible')
    def __str__(self):
        return self.tipo_inversion + '_' + self.descripcion    
    class Meta:
        unique_together = ('tipo_inversion_descripcion','descripcion','numero_documento','concepto_recategorizacion')
        verbose_name = 'Cuadro de Inversiones Evaluacion'
        verbose_name_plural = 'Cuadro de Inversiones Evaluacion'
        
class Cotizaciones_Interbancarias(models.Model):
    emisor=models.CharField(max_length=30, verbose_name='Pais Emisor')
    denominacion=models.CharField(max_length=30, verbose_name='Denominacion')
    fecha=models.DateField(verbose_name='Fecha')
    codigo=models.CharField(max_length=10, verbose_name='Codigo Moneda BCU')
    promedio=models.DecimalField(max_digits=10, decimal_places=4, verbose_name='Promedio Cotizacion')
    def __str__(self):
        return self.emisor + '_' + self.denominacion + '_' + self.fecha + '_' + self.codigo + '_' + self.promedio
    class Meta:
        unique_together = ('emisor', 'denominacion','fecha','codigo')
        verbose_name = 'Tabla de Cotizaciones Interbancarias'
        verbose_name_plural = 'Tabla de Cotizaciones Interbancarias'
        
class Contacto(models.Model):
    empresa=models.CharField(max_length=100, verbose_name='Empresa')
    contacto=models.CharField(max_length=100, verbose_name='Con quien Contactarse:')
    direccion=models.CharField(max_length=200, verbose_name='Direccion')
    localidad=models.CharField(max_length=100, verbose_name='Localidad')
    pais=models.CharField(max_length=100, verbose_name='Pais')
    telefono=models.CharField(max_length=50, verbose_name='Telefono')
    email=models.EmailField(max_length=50, verbose_name='Direccion de Email')
    consulta=models.TextField(verbose_name='Realice su Consulta')
    def __str__(self):
        return self.empresa + '_' + self.contacto
    class Meta:
        verbose_name = 'Comunicaciones Generales'
        verbose_name_plural = 'Comunicaciones Generales'
        
class Ind_Gral_Empleo(models.Model):
    proyecto=models.ForeignKey(Expediente_Dec_143_18, on_delete=models.CASCADE, verbose_name='Proyecto')
    ano0_eq40hs = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Cantidad de Personas equivalente a 40hs en la situacion inicial', default=0)
    ano0_men25 = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Menores de 25 anos en la situacion inicial', default=0)
    ano0_muj = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Mujeres en la situacion inicial', default=0)
    ano0_discap = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Discapacitados en la situacion inicial', default=0)
    ano0_rural = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Trabajadores Rurales en la situacion inicial', default=0)
    ano1_eq40hs = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Cantidad de Personas equivalente a 40hs en el ano 1', default=0)
    ano1_men25 = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Menores de 25 anos en al ano 1', default=0)
    ano1_muj = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Mujeres en el ano 1', default=0)
    ano1_discap = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Discapacitados en el ano 1', default=0)
    ano1_rural = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Trabajadores Rurales en el ano 1', default=0)
    ano2_eq40hs = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Cantidad de Personas equivalente a 40hs en el ano 2', default=0)
    ano2_men25 = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Menores de 25 anos en al ano 2', default=0)
    ano2_muj = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Mujeres en el ano 2', default=0)
    ano2_discap = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Discapacitados en el ano 2', default=0)
    ano2_rural = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Trabajadores Rurales en el ano 2', default=0)
    ano3_eq40hs = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Cantidad de Personas equivalente a 40hs en el ano 3', default=0)
    ano3_men25 = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Menores de 25 anos en al ano 3', default=0)
    ano3_muj = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Mujeres en el ano 3', default=0)
    ano3_discap = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Discapacitados en el ano 3', default=0)
    ano3_rural = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Trabajadores Rurales en el ano 3', default=0)
    ano4_eq40hs = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Cantidad de Personas equivalente a 40hs en el ano 4', default=0)
    ano4_men25 = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Menores de 25 anos en al ano 4', default=0)
    ano4_muj = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Mujeres en el ano 4', default=0)
    ano4_discap = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Discapacitados en el ano 4', default=0)
    ano4_rural = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Trabajadores Rurales en el ano 4', default=0)
    ano5_eq40hs = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Cantidad de Personas equivalente a 40hs en el ano 5', default=0)
    ano5_men25 = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Menores de 25 anos en al ano 5', default=0)
    ano5_muj = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Mujeres en el ano 5', default=0)
    ano5_discap = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Discapacitados en el ano 5', default=0)
    ano5_rural = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Trabajadores Rurales en el ano 5', default=0)
    def __str__(self):
        return self.proyecto
    class Meta:
        verbose_name = 'Indicador General de Empleo'
        verbose_name_plural = 'Indicador General de Empleo'
        
        
class Exp_Bienes_Servicios(models.Model):
    lista_BsScios=(('Bienes','Bienes'),('Servicios','Servicios'))
    proyecto=models.ForeignKey(Expediente_Dec_143_18, on_delete=models.CASCADE, verbose_name='Proyecto')
    tipo=models.CharField(choices=lista_BsScios, max_length=100, default='Bienes', verbose_name='Bienes/Servicios')
    descripcion=models.CharField(max_length=200, verbose_name='Descripcion de Exportacion')
    def __str__(self):
        return self.proyecto + '_' + self.tipo
    class Meta:
        unique_together = ('proyecto', 'tipo','descripcion')
        verbose_name = 'Tipo de Exportaciones de Bienes y Servicios'
        verbose_name_plural = 'Tipo de Exportaciones de Bienes y Servicios'
        
class Ind_Gral_Exportaciones(models.Model):
    proyecto=models.ForeignKey(Expediente_Dec_143_18, on_delete=models.CASCADE, verbose_name='Proyecto')
    tipo=models.ForeignKey(Exp_Bienes_Servicios, on_delete=models.CASCADE, verbose_name='Tipo de Exportacion')
    descripcion=models.CharField(max_length=200, verbose_name='Descripcion de Exportacion')
    ano0 = models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Exportaciones Ano 0')
    ano1 = models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Exportaciones Ano 1')
    ano2 = models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Exportaciones Ano 2')
    ano3 = models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Exportaciones Ano 3')
    ano4 = models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Exportaciones Ano 4')
    ano5 = models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Exportaciones Ano 5')
    def __str__(self):
        return self.proyecto + '_' + self.tipo + '_' + self.descripcion
    class Meta:
        unique_together = ('proyecto', 'tipo','descripcion')
        verbose_name = "Indicador General de Exportaciones"
        verbose_name_plural = "Indicador General de Exportaciones"
        
class Localizacion_Operaciones(models.Model):
    lista_operaciones=(('Nueva Localidad','Nueva Localidad'),('Localidad donde ya se realizan operaciones','Localidad donde ya se realizan operaciones'))
    tipo = models.CharField(choices=lista_operaciones, max_length=100, unique=True, default='Nueva Localidad', verbose_name='Localidad Nueva/Anterior')
    def __str__(self):
        return self.tipo
    class Meta:
        verbose_name = "Opciones Localizacion"
        verbose_name_plural = "Opciones Localizacion"
        
class Listado_Departamentos(models.Model):
    lista_departamentos=sorted((('Montevideo','Montevideo'),('Canelones','Canelones'),('Artigas','Artigas'),('Cerro Largo','Cerro Largo'),('Salto','Salto'),('Durazno','Durazno'),('Tacuarembo','Tacuarembo'),('Rivera','Rivera'),('Treinta y Tres','Treinta y Tres'),('Paysandu','Paysandu'),('Lavalleja','Lavalleja'),('Soriano','Soriano'),('Rocha','Rocha'),('Florida','Florida'),('Rio Negro','Rio Negro'),('San Jose','San Jose'),('Flores','Flores'),('Colonia','Colonia'),('Maldonado','Maldonado')))
    lista_capital_resto=(('Capital','Capital'),('Resto','Resto'))
    departamento = models.CharField(choices=lista_departamentos, max_length=100, default='Montevideo', verbose_name='Departamentos de Uruguay')
    cap_int = models.CharField(choices=lista_capital_resto, max_length=100, default='Capital', verbose_name='Capital/Interior')
    puntaje = models.PositiveIntegerField(verbose_name='Puntaje Asignado')
    def __str__(self):
        return self.departamento + '_' + self.cap_int
    class Meta:
        unique_together = ('departamento', 'cap_int')
        verbose_name = "Listado de Departamentos y Puntajes"
        verbose_name_plural = "Listado de Departamentos y Puntajes"
        
class Ind_Gral_Localizacion(models.Model):
    proyecto=models.ForeignKey(Expediente_Dec_143_18, on_delete=models.CASCADE, verbose_name='Proyecto')
    localizacion=models.OneToOneField(Localizacion_Proyecto, on_delete=models.CASCADE, verbose_name='Localizacion')
    operaciones=models.ForeignKey(Localizacion_Operaciones, on_delete=models.CASCADE, verbose_name='Ya tenia Operaciones:')
    departamento=models.ForeignKey(Listado_Departamentos, on_delete=models.CASCADE, verbose_name='Departamento')
    inversion_UI=models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Inversion Total en UI')
    
    def _get_empleo_requerido(self):
        if self.operaciones == "Nueva Localidad":
            return 0
        else:
            return 1
    empleo_requerido = property(_get_empleo_requerido)
    def __str__(self):
        return self.proyecto + '_' + self.localizacion
    class Meta:
        unique_together = ('proyecto', 'localizacion')
        verbose_name = "Indicador General de Descentralizacion"
        verbose_name_plural = "Indicador General de Descentralizacion"
    
class Ind_Gral_TL(models.Model):
    proyecto=models.ForeignKey(Expediente_Dec_143_18, on_delete=models.CASCADE, verbose_name='Proyecto')
    detalle=models.CharField(max_length=100, verbose_name='Descripcion de Inversion en Tecnologias Limpias')
    ano1 = models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Inversiones en Tecnologias Limpias Ano 1 en UI')
    ano2 = models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Inversiones en Tecnologias Limpias Ano 2 en UI')  
    def __str__(self):
        return self.proyecto + '_' + self.detalle
    class Meta:
        unique_together = ('proyecto', 'detalle')
        verbose_name = "Indicador General de Tecnologias Limpias"
        verbose_name_plural = "Indicador General de Tecnologias Limpias"
        
class Ind_Gral_IDi(models.Model):
    proyecto=models.ForeignKey(Expediente_Dec_143_18, on_delete=models.CASCADE, verbose_name='Proyecto')
    detalle=models.CharField(max_length=100, verbose_name='Descripcion de Inversion en Investigacion, Desarrollo e innovacion')
    ano1 = models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Inversiones en Investigacion, Desarrollo e innovacion Ano 1 en UI')
    ano2 = models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Inversiones en Investigacion, Desarrollo e innovacion Ano 2 en UI')  
    def __str__(self):
        return self.proyecto + '_' + self.detalle    
    class Meta:
        unique_together = ('proyecto', 'detalle')
        verbose_name = "Indicador General de Investigacion, Desarrollo e innovacion"
        verbose_name_plural = "Indicador General de Investigacion, Desarrollo e innovacion"
        
class Ind_Sect_Formacion_Continua(models.Model):
    proyecto=models.ForeignKey(Expediente_Dec_143_18, on_delete=models.CASCADE, verbose_name='Proyecto')
    entidad=models.CharField(max_length=100, verbose_name='Entidad Capacitadora')
    tema_capacitacion=models.CharField(max_length=500, verbose_name='Titulo/Tema de la Capacitacion')
    cargahoraria=models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Carga Horaria de la Capacitacion')
    ano1 = models.PositiveIntegerField(verbose_name='Personal Capacitado en el ano 1')
    ano2 = models.PositiveIntegerField(verbose_name='Personal Capacitado en el ano 2')
    ano3 = models.PositiveIntegerField(verbose_name='Personal Capacitado en el ano 3')
    ano4 = models.PositiveIntegerField(verbose_name='Personal Capacitado en el ano 4')
    ano5 = models.PositiveIntegerField(verbose_name='Personal Capacitado en el ano 5')
    def __str__(self):
        return self.proyecto + '_' + self.entidad + '_' + self.tema_capacitacion
    class Meta:
        unique_together = ('proyecto', 'entidad','tema_capacitacion')
        verbose_name = "Indicador Sectorial de Formacion Continua y Capacitacion"
        verbose_name_plural = "Indicador Sectorial de Formacion Continua y Capacitacion"
        
class Ind_Sect_Diferenciacion_Prod_Proc(models.Model):
    proyecto=models.ForeignKey(Expediente_Dec_143_18, on_delete=models.CASCADE, verbose_name='Proyecto')
    entidad=models.CharField(max_length=100, verbose_name='Entidad Certificadora')
    certificacion=models.CharField(max_length=100, verbose_name='Descripcion de Certificacion')
    def __str__(self):
        return self.proyecto + '_' + self.entidad + '_' + self.certificacion
    class Meta:
        unique_together = ('proyecto', 'entidad','certificacion')
        verbose_name = "Indicador Sectorial de Diferenciacion de Productos y Procesos"
        verbose_name_plural = "Indicador Sectorial de Diferenciacion de Productos y Procesos"
        
class Ind_Sect_Energia_Renovable(models.Model):
    proyecto=models.ForeignKey(Expediente_Dec_143_18, on_delete=models.CASCADE, verbose_name='Proyecto')
    fuente=models.CharField(max_length=100, verbose_name='Descripcion de Fuente de Energias Renovables')
    ano1 = models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Inversion en Energias Renovables Ano 1 expresado en UI')
    ano2 = models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Inversion en Energias Renovables Ano 2 expresado en UI')  
    def __str__(self):
        return self.proyecto + '_' + self.fuente    
    class Meta:
        unique_together = ('proyecto', 'fuente')
        verbose_name = "Indicador Sectorial de Energias Renovables"
        verbose_name_plural = "Indicador Sectorial de Energias Renovables"
        
class Ind_Sect_Mercado_Capitales(models.Model):
    proyecto=models.ForeignKey(Expediente_Dec_143_18, on_delete=models.CASCADE, verbose_name='Proyecto')
    acciones = models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Emision de Acciones en UI')
    titulos_deuda = models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Emision de Titulos de Deuda en UI')
    def __str__(self):
        return self.proyecto
    class Meta:
        unique_together = ('proyecto', 'acciones','titulos_deuda')
        verbose_name = "Indicador Sectorial del Mercado de Capitales"
        verbose_name_plural = "Indicador Sectorial del Mercado de Capitales"
        
class Propietarios_Directores_Representantes(models.Model):
    proyecto=models.ForeignKey(Expediente_Dec_143_18, on_delete=models.CASCADE, verbose_name='Proyecto')
    nombre=models.CharField(max_length=100, verbose_name='Nombre del Propietario/Director/Representante')
    direccion=models.CharField(max_length=200, verbose_name='Direccion')
    ci=models.DecimalField(max_digits=8, decimal_places=0, verbose_name='Cedula de Identidad')
    def __str__(self):
        return self.proyecto + '_' + self.nombre
    class Meta:
        unique_together = ('proyecto', 'nombre','direccion','ci')
        verbose_name = "Propietarios Directores y Representantes"
        verbose_name_plural = "Propietarios Directores y Representantes"
        
class Contactos_Proyecto(models.Model):
    proyecto=models.ForeignKey(Expediente_Dec_143_18, on_delete=models.CASCADE, verbose_name='Proyecto')
    nombre=models.CharField(max_length=100, verbose_name='Nombre del Contacto para el Proyecto')
    direccion=models.CharField(max_length=200, verbose_name='Direccion')
    ci=models.DecimalField(max_digits=8, decimal_places=0, verbose_name='Cedula de Identidad')
    telefono=models.DecimalField(max_digits=12, decimal_places=0, verbose_name='Telefono de Contacto')
    mail=models.EmailField(max_length=200, verbose_name='Email de Contacto')
    def __str__(self):
        return self.proyecto + '_' + self.nombre    
    class Meta:
        unique_together = ('proyecto', 'nombre','direccion','ci')
        verbose_name = "Contactos del Proyecto"
        verbose_name_plural = "Contactos del Proyecto"    
    

        