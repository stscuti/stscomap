from django.forms import ModelForm
from django import forms
from Decreto_143_18.models import Empresa_Datos_Formales
from Decreto_143_18.models import Tipo_Contribuyente
from Decreto_143_18.models import Empresa_FIT
from Decreto_143_18.models import Tipo_Inversiones
from Decreto_143_18.models import Expediente_Dec_143_18
from Decreto_143_18.models import Localizacion_Proyecto, Cuadro_Inversiones_Empresa, Cuadro_Inversiones_Definitivo
from Decreto_143_18.models import Contacto
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
from PIL import Image
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Fieldset, ButtonHolder, HTML, Div

class Empresa_Datos_Formales_Form(ModelForm):
    class Meta:
        model=Empresa_Datos_Formales
        fields = '__all__'
        exclude = ('timestamp',)
        verbose_name='Formulario: Empresa Datos Formales'
        label='Formulario Emp Datos Formales'
        widgets = {
                'fecha_balance': forms.DateInput(attrs={
                'placeholder': 'Con dia y mes tambien ingrese ano actual',
                'class': 'form-control datepicker-input',
                'data-target': '#datepicker1', })
            }
        
    def __init__(self, *args, **kwargs):
        super(Empresa_Datos_Formales_Form,self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML('<p class="formtitulosintermedios">Datos Registrales de la Empresa</p>'),
            Row(
                Column('razon_social', css_class='form-group col-md-3 mb-0'),
                Column('nombre_comercial', css_class='form-group col-md-3 mb-0'),
                Column('rut', css_class='form-group col-md-2 mb-0'),
                Column('num_bps', css_class='form-group col-md-2 mb-0'),
                Column('num_mtss', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('domicilio_constituido', css_class='form-group col-md-3 mb-0'),
                Column('domicilio_fiscal', css_class='form-group col-md-3 mb-0'),
                Column('telefono', css_class='form-group col-md-2 mb-0'),
                Column('email', css_class='form-group col-md-2 mb-0'),
                Column('celular', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            HTML('<p class="formtitulosintermedios">Actividad y Tipo de Contribuyente</p>'),
            Row(
                Column('cod_giro_ciiu', css_class='form-group col-md-2 mb-0'),
                Column('nombre_giro', css_class='form-group col-md-4 mb-0'),
                Column('fecha_balance', css_class='form-group col-md-3 mb-0'),
                Column('tipo', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Cargar')
        )
        
class Tipo_Contribuyente_Form(ModelForm):
    class Meta:
        model=Tipo_Contribuyente
        fields = '__all__'
        verbose_name='Formulario: Tipo de Contribuyente'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('tipo', css_class='form-group col-md-6 mb-0'),

             ),
            Submit('submit', 'Cargar')
        )    
        
class Empresa_FIT_Form(ModelForm):
    class Meta:
        model=Empresa_FIT
        fields = '__all__'
        exclude = ('timestamp',)
        verbose_name='Formulario: Inicio de Tramite (FIT)'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.helper = FormHelper()
        self.helper.layout = Layout(
            
            HTML('<p class="formtitulosintermedios">Datos del Expediente </p>'),
            Row(
                Column('num_expediente', css_class='form-group col-md-2 mb-0'),
                Column('razon_social', css_class='form-group col-md-2 mb-0'),
                Column('documento_fit', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
                ),
            HTML('<p class="formtitulosintermedios">Condiciones MYPE </p>'),
            Row(
                Column('sin_facturacion_ult3ej', css_class='form-group col-md-1 mb-0 type="checkbox"'),
                Column('empresa_vinculada', css_class='form-group col-md-1 mb-0'),
                Column('empresa_vinculada_sfult3ej', css_class='form-group col-md-1 mb-0'),
                Column('beneficio_MYPE', css_class='form-group col-md-1 mb-0'),
                Column('empresa_controlada', css_class='form-group col-md-1 mb-0'),
                Column('empresa_controlada_supera_MYPE', css_class='form-group col-md-1 mb-0'),
                Column('pertenece_grupo_economico', css_class='form-group col-md-2 mb-0'),
                Column('grupo_economico_supera_MYPE', css_class='form-group col-md-2 mb-0'),
                Column('declaro_geco_controlantes_MYPE', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
                ),
            Row(
                Column('cantidad_empleados', css_class='form-group col-md-2 mb-0'),
                Column('ventas_netas_UI', css_class='form-group col-md-2 mb-0'),
                Column('ventas_netas_Pesos', css_class='form-group col-md-2 mb-0'),
                Column('proyeccion_empleos_siguiente_ejercicio', css_class='form-group col-md-3 mb-0'),
                Column('proyeccion_ventas_UI_siguiente_ejercicio', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
                ),
            HTML('<p class="formtitulosintermedios">Caracteristicas del Proyecto</p>'),
            Row( 
                Column('objetivo_proyecto', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
                ),
            Row(
                Column('descripcion_ampliada', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
                ),
            HTML('<p class="formtitulosintermedios">Montos de la Inversion</p>'),
            Row(
                Column('monto_inversion_UI', css_class='form-group col-md-3 mb-0'),
                Column('tc_Dolar', css_class='form-group col-md-2 mb-0'),
                Column('tc_Euro', css_class='form-group col-md-2 mb-0'),
                Column('tc_UI', css_class='form-group col-md-2 mb-0'),
                Column('anos_ejecucion_inversion', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
                ),
            HTML('<p class="formtitulosintermedios">Beneficios Solicitados</p>'),
            Row(
                Column('beneficio_IRAE', css_class='form-group col-md-2 mb-0'),
                Column('beneficio_IP', css_class='form-group col-md-2 mb-0'),
                Column('beneficio_IVA', css_class='form-group col-md-2 mb-0'),
                Column('beneficio_tributos_importacion', css_class='form-group col-md-2 mb-0'),
                Column('beneficio_transitorios', css_class='form-group col-md-2 mb-0'),
                Column('aportes_patronales_art28', css_class='form-group col-md-1 mb-0'),
                Column('usuario_parque_industrial', css_class='form-group col-md-1 mb-0'),
                css_class='form-row'
                ),
            HTML('<p class="formtitulosintermedios">Utilizacion de Indicadores Generales</p>'),
            Row(
                Column('indicadores_generales_empleo', css_class='form-group col-md-3 mb-0'),
                Column('indicadores_generales_exportaciones', css_class='form-group col-md-3 mb-0'),
                Column('indicadores_generales_descentralizacion', css_class='form-group col-md-3 mb-0'),
                Column('indicadores_generales_TL', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
                ),
            HTML('<p class="formtitulosintermedios">Utilizacion de Indicadores Sectoriales</p>'),
            Row(
                Column('indicadores_generales_IDi', css_class='form-group col-md-4 mb-0'),
                Column('indicadores_sectoriales_mef_formacion', css_class='form-group col-md-2 mb-0'),
                Column('indicadores_sectoriales_mef_diferenciacion', css_class='form-group col-md-2 mb-0'),
                Column('indicadores_sectoriales_mef_renovables', css_class='form-group col-md-2 mb-0'),
                Column('indicadores_sectoriales_mef_capitales', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Cargar')
        )
        
class Tipo_Inversiones_Form(ModelForm):
    class Meta:
        model=Tipo_Inversiones
        fields = '__all__'
        verbose_name='Formulario: Tipo de Inversiones'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('tipo', css_class='form-group col-md-4 mb-0'),
                Column('grupo1', css_class='form-group col-md-4 mb-0'),
                Column('grupo2', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Cargar')
        )    

class Expediente_Dec_143_18_Form(ModelForm):
    class Meta:
        model=Expediente_Dec_143_18
        fields = '__all__'
        exclude = ('timestamp',)
        verbose_name='Formulario: Expediente Decreto 143/18'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('num_expediente', css_class='form-group col-md-3 mb-0'),
                Column('fecha_presentacion', css_class='form-group col-md-3 mb-0'),
                Column('documento_carta_compromiso', css_class='form-group col-md-3 mb-0'),
                Column('documento_certificado_notarial', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('documento_formulario_bcu', css_class='form-group col-md-3 mb-0'),
                Column('documento_estados_contables', css_class='form-group col-md-3 mb-0'),
                Column('documento_constancia_DINAPYME', css_class='form-group col-md-3 mb-0'),
                Column('documento_dj_IRAE', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('documento_constancia_CIIU', css_class='form-group col-md-3 mb-0'),
                Column('documento_certificado_DINAMA', css_class='form-group col-md-3 mb-0'),
                Column('documento_plan_uso_suelos_DGRN', css_class='form-group col-md-3 mb-0'),
                Column('documento_formulario_ANII_IDi', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),

            Row(
                Column('documento_catalogos_ANII_IDi', css_class='form-group col-md-3 mb-0'),
                Column('documento_formulario_TL', css_class='form-group col-md-3 mb-0'),
                Column('documento_catalogo_TL', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('documento_formulario_sectorial_FCC', css_class='form-group col-md-6 mb-0'),
                Column('documento_programa_sectorial_FCC', css_class='form-group col-md-6 mb-0'),
                
                css_class='form-row'
            ),
            Row(
                Column('documento_formulario_sectorial_MC', css_class='form-group col-md-3 mb-0'),
                Column('documento_constancia_COMAP', css_class='form-group col-md-3 mb-0'),
                Column('documento_certificado_unico_DGI', css_class='form-group col-md-3 mb-0'),
                Column('documento_certificado_unico_BPS', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('inversiones_documento_cuadro', css_class='form-group col-md-4 mb-0'),
                Column('numero_inversiones_documento_cuadro', css_class='form-group col-md-2 mb-0'),
                Column('inversiones_documento_cronograma', css_class='form-group col-md-4 mb-0'),
                Column('numero_inversiones_documento_cronograma', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('inversiones_documento_plan_implantacion', css_class='form-group col-md-4 mb-0'),
                Column('inversiones_documento_memoria_constructiva', css_class='form-group col-md-4 mb-0'),
                Column('inversiones_documento_rubrado_obra_imagen', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('inversiones_documento_rubrado_obra_excel', css_class='form-group col-md-4 mb-0'),
                Column('inversiones_documento_anteproyecto_arquitectura', css_class='form-group col-md-4 mb-0'),
                Column('inversiones_documento_contrato_arrendamiento', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),

            Submit('submit', 'Cargar')
        )
            
class Localizacion_Proyecto_Form(ModelForm):
    class Meta:
        model=Localizacion_Proyecto
        fields = '__all__'
        exclude = ('timestamp',)
        verbose_name='Formulario: Localizacion del Proyecto'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('razon_social_num_exp', css_class='form-group col-md-4 mb-0'),
                Column('departamento', css_class='form-group col-md-4 mb-0'),
                Column('localidad', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('direccion', css_class='form-group col-md-6 mb-0'),
                Column('vinculo_juridico_inversor_predio', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Cargar')
        )    
        
class Cuadro_Inversiones_Empresa_Form(ModelForm):
    class Meta:
        model=Cuadro_Inversiones_Empresa
        fields = '__all__'
        verbose_name='Formulario: Cuadro Inversiones Empresa'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('proyecto', css_class='form-group col-md-3 mb-0'),
                Column('descripcion', css_class='form-group col-md-3 mb-0'),
                Column('tipo_inversion', css_class='form-group col-md-3 mb-0'),
                Column('ejecucion', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('numero_documento', css_class='form-group col-md-3 mb-0'),
                Column('indicador_relacionado', css_class='form-group col-md-2 mb-0'),
                Column('fecha', css_class='form-group col-md-1 mb-0'),
                Column('compra', css_class='form-group col-md-1 mb-0'),
                Column('nuevo_usado', css_class='form-group col-md-2 mb-0'),
                Column('cantidad', css_class='form-group col-md-1 mb-0'),
                Column('proveedor', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),

            Row(
                Column('moneda_origen', css_class='form-group col-md-2 mb-0'),
                Column('costo_moneda_origen', css_class='form-group col-md-2 mb-0'),
                Column('total_inversiones_UI', css_class='form-group col-md-2 mb-0'),
                Column('vida_util_anos', css_class='form-group col-md-2 mb-0'),
                Column('UI_utilizada', css_class='form-group col-md-2 mb-0'),
                Column('USD_utilizado', css_class='form-group col-md-1 mb-0'),
                Column('EUR_utilizado', css_class='form-group col-md-1 mb-0'),
                css_class='form-row'    
            ),
             Submit('submit', 'Cargar')
        )    
class Cuadro_Inversiones_Definitivo_Form(ModelForm):
    class Meta:
        model=Cuadro_Inversiones_Definitivo
        fields = '__all__'
        verbose_name='Formulario: Cuadro Inversiones Definitivo'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('tipo_inversion_descripcion', css_class='form-group col-md-3 mb-0'),
                Column('descripcion', css_class='form-group col-md-3 mb-0'),
                Column('tipo_inversion', css_class='form-group col-md-3 mb-0'),
                Column('ejecucion', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('numero_documento', css_class='form-group col-md-4 mb-0'),
                Column('indicador_relacionado', css_class='form-group col-md-4 mb-0'),
                Column('fecha', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('compra', css_class='form-group col-md-4 mb-0'),
                Column('nuevo_usado', css_class='form-group col-md-8 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('cantidad', css_class='form-group col-md-6 mb-0'),
                Column('proveedor', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),

            Row(
                Column('moneda_origen', css_class='form-group col-md-6 mb-0'),
                Column('costo_moneda_origen', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('total_inversiones_UI', css_class='form-group col-md-4 mb-0'),
                Column('vida_util_anos', css_class='form-group col-md-4 mb-0'),
                Column('UI_utilizada', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('USD_utilizado', css_class='form-group col-md-6 mb-0'),
                Column('EUR_utilizado', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('tipo_inversion_definitiva', css_class='form-group col-md-4 mb-0'),
                Column('concepto_recategorizacion', css_class='form-group col-md-4 mb-0'),
                Column('observaciones', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('UI_correspondiente', css_class='form-group col-md-4 mb-0'),
                Column('USD_correspondiente', css_class='form-group col-md-8 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('EUR_correspondiente', css_class='form-group col-md-4 mb-0'),
                Column('costo_moneda_origen_elegible', css_class='form-group col-md-4 mb-0'),
                Column('total_inversiones_UI_elegible', css_class='form-group col-md-4 mb-0'),
                css_class='form-row' 
            ),
            Submit('submit', 'Cargar')
        )    
class Contacto_Form(ModelForm):
    class Meta:
        model=Contacto
        fields = '__all__'
        verbose_name='Contacto'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('empresa', css_class='form-group col-md-6 mb-0'),
                Column('contacto', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('direccion', css_class='form-group col-md-4 mb-0'),
                Column('localidad', css_class='form-group col-md-4 mb-0'),
                Column('pais', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('telefono', css_class='form-group col-md-4 mb-0'),
                Column('email', css_class='form-group col-md-4 mb-0'),
                Column('consulta', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Cargar')
        )
            
class Cotizaciones_Interbancarias_Form(ModelForm):
    class Meta:
        model=Cotizaciones_Interbancarias
        fields = '__all__'
        verbose_name='Cotizaciones Interbancarias'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('emisor', css_class='form-group col-md-4 mb-0'),
                Column('denominacion', css_class='form-group col-md-2 mb-0'),
                Column('fecha', css_class='form-group col-md-2 mb-0'),
                Column('codigo', css_class='form-group col-md-2 mb-0'),
                Column('promedio', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Cargar')
        )
            
class Ind_Gral_Empleo_Form(ModelForm):
    class Meta:
        model=Ind_Gral_Empleo
        fields = '__all__'
        verbose_name='Formulario: Indicador General de Empleo'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('proyecto', css_class='form-group col-md-12 mb-0'),
                ),
            Row(
                Column('ano0_eq40hs', css_class='form-group col-md-4 mb-0'),
                Column('ano0_men25', css_class='form-group col-md-2 mb-0'),
                Column('ano0_muj', css_class='form-group col-md-2 mb-0'),
                Column('ano0_discap', css_class='form-group col-md-2 mb-0'),
                Column('ano0_rural', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
                ),
            Row(
                Column('ano1_eq40hs', css_class='form-group col-md-4 mb-0'),
                Column('ano1_men25', css_class='form-group col-md-2 mb-0'),
                Column('ano1_muj', css_class='form-group col-md-2 mb-0'),
                Column('ano1_discap', css_class='form-group col-md-2 mb-0'),
                Column('ano1_rural', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
                ),
            Row(
                Column('ano2_eq40hs', css_class='form-group col-md-4 mb-0'),
                Column('ano2_men25', css_class='form-group col-md-2 mb-0'),
                Column('ano2_muj', css_class='form-group col-md-2 mb-0'),
                Column('ano2_discap', css_class='form-group col-md-2 mb-0'),
                Column('ano2_rural', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
                ),
            Row(
                Column('ano3_eq40hs', css_class='form-group col-md-4 mb-0'),
                Column('ano3_men25', css_class='form-group col-md-2 mb-0'),
                Column('ano3_muj', css_class='form-group col-md-2 mb-0'),
                Column('ano3_discap', css_class='form-group col-md-2 mb-0'),
                Column('ano3_rural', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
                ),
            Row(
                Column('ano4_eq40hs', css_class='form-group col-md-4 mb-0'),
                Column('ano4_men25', css_class='form-group col-md-2 mb-0'),
                Column('ano4_muj', css_class='form-group col-md-2 mb-0'),
                Column('ano4_discap', css_class='form-group col-md-2 mb-0'),
                Column('ano4_rural', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
                ),
            Row(
                Column('ano5_eq40hs', css_class='form-group col-md-4 mb-0'),
                Column('ano5_men25', css_class='form-group col-md-2 mb-0'),
                Column('ano5_muj', css_class='form-group col-md-2 mb-0'),
                Column('ano5_discap', css_class='form-group col-md-2 mb-0'),
                Column('ano5_rural', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
                ),
            Submit('submit', 'Cargar')
        )
            
class Exp_Bienes_Servicios_Form(ModelForm):
    class Meta:
        model=Exp_Bienes_Servicios
        fields = '__all__'
        verbose_name='Formulario: Exportaciones de Bienes y Servicios'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('proyecto', css_class='form-group col-md-4 mb-0'),
                Column('tipo', css_class='form-group col-md-4 mb-0'),
                Column('descripcion', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Cargar')
        )
    
        
class Ind_Gral_Exportaciones_Form(ModelForm):
    class Meta:
        model=Ind_Gral_Exportaciones
        fields = '__all__'
        verbose_name='Formulario: Indicador General de Exportaciones'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('proyecto', css_class='form-group col-md-4 mb-0'),
                Column('tipo', css_class='form-group col-md-4 mb-0'),
                Column('descripcion', css_class='form-group col-md-4 mb-0'),
            ),
            Row(
                Column('ano0', css_class='form-group col-md-2 mb-0'),
                Column('ano1', css_class='form-group col-md-2 mb-0'),
                Column('ano2', css_class='form-group col-md-2 mb-0'),
                Column('ano3', css_class='form-group col-md-2 mb-0'),
                Column('ano4', css_class='form-group col-md-2 mb-0'),
                Column('ano5', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Cargar')
        )  
          
class Localizacion_Operaciones_Form(ModelForm):
    class Meta:
        model=Localizacion_Operaciones
        fields = '__all__'
        verbose_name='Formulario: Localizacion Operaciones'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('tipo', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
             ),
            Submit('submit', 'Cargar')
        )
            
class Listado_Departamentos_Form(ModelForm):
    class Meta:
        model=Listado_Departamentos
        fields = '__all__'
        verbose_name='Listado Departamentos'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('departamento', css_class='form-group col-md-4 mb-0'),
                Column('cap_int', css_class='form-group col-md-4 mb-0'),
                Column('puntaje', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Cargar')
        )
          
class Ind_Gral_Localizacion_Form(ModelForm):
    class Meta:
        model=Ind_Gral_Localizacion
        fields = '__all__'
        verbose_name='Formulario: Indicador General de Descentralizacion'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('proyecto', css_class='form-group col-md-2 mb-0'),
                Column('localizacion', css_class='form-group col-md-2 mb-0'),
                Column('operaciones', css_class='form-group col-md-2 mb-0'),
                Column('departamento', css_class='form-group col-md-2 mb-0'),
                Column('inversion_UI', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Cargar')
        )    
class Ind_Gral_TL_Form(ModelForm):
    class Meta:
        model=Ind_Gral_TL
        fields = '__all__'
        verbose_name='Formulario: Indicador General de Tecnologias Limpias'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('proyecto', css_class='form-group col-md-3 mb-0'),
                Column('detalle', css_class='form-group col-md-3 mb-0'),
                Column('ano1', css_class='form-group col-md-3 mb-0'),
                Column('ano2', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Cargar')
        )
           
class Ind_Gral_IDi_Form(ModelForm):
    class Meta:
        model=Ind_Gral_IDi
        fields = '__all__'
        verbose_name='Formulario: Indicador General de Tecnologias Limpias'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('proyecto', css_class='form-group col-md-3 mb-0'),
                Column('detalle', css_class='form-group col-md-3 mb-0'),
                Column('ano1', css_class='form-group col-md-3 mb-0'),
                Column('ano2', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Cargar')
        )
    
class Ind_Sect_Formacion_Continua_Form(ModelForm):
    class Meta:
        model=Ind_Sect_Formacion_Continua
        fields = '__all__'
        verbose_name='Formulario: Indicador Sectorial Formacion Continua y Capacitacion'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('proyecto', css_class='form-group col-md-3 mb-0'),
                Column('entidad', css_class='form-group col-md-3 mb-0'),
                Column('tema_capacitacion', css_class='form-group col-md-3 mb-0'),
                Column('cargahoraria', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('ano1', css_class='form-group col-md-2 mb-0'),
                Column('ano2', css_class='form-group col-md-2 mb-0'),
                Column('ano3', css_class='form-group col-md-2 mb-0'),
                Column('ano4', css_class='form-group col-md-2 mb-0'),
                Column('ano5', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Cargar')
        )
          
class Ind_Sect_Diferenciacion_Prod_Proc_Form(ModelForm):
    class Meta:
        model=Ind_Sect_Diferenciacion_Prod_Proc
        fields = '__all__'
        verbose_name='Formulario: Indicador Sectorial Diferenciacion de Productos y Produccion'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('proyecto', css_class='form-group col-md-4 mb-0'),
                Column('entidad', css_class='form-group col-md-4 mb-0'),
                Column('certificacion', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Cargar')
        )
          
class Ind_Sect_Energia_Renovable_Form(ModelForm):
    class Meta:
        model=Ind_Sect_Energia_Renovable
        fields = '__all__'
        verbose_name='Formulario: Indicador Sectorial Energias Renovables'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('proyecto', css_class='form-group col-md-3 mb-0'),
                Column('fuente', css_class='form-group col-md-3 mb-0'),
                Column('ano1', css_class='form-group col-md-3 mb-0'),
                Column('ano2', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Cargar')
        )
        
class Ind_Sect_Mercado_Capitales_Form(ModelForm):
    class Meta:
        model=Ind_Sect_Mercado_Capitales
        fields = '__all__'
        verbose_name='Formulario: Indicador Sectorial Mercado de Capitales'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
          Row(
                Column('proyecto', css_class='form-group col-md-4 mb-0'),
                Column('acciones', css_class='form-group col-md-4 mb-0'),
                Column('titulos_deuda', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Cargar')
        )
            
class Propietarios_Directores_Representantes_Form(ModelForm):
    class Meta:
        model=Propietarios_Directores_Representantes
        fields = '__all__'
        verbose_name='Formulario: Propietarios, Directores y Representantes'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('proyecto', css_class='form-group col-md-3 mb-0'),
                Column('nombre', css_class='form-group col-md-3 mb-0'),
                Column('direccion', css_class='form-group col-md-3 mb-0'),
                Column('ci', css_class='form-group col-md-3 mb-0'),
                 css_class='form-row'
            ),
            Submit('submit', 'Cargar')    
        )
         
class Contactos_Proyecto_Form(ModelForm):
    class Meta:
        model=Contactos_Proyecto
        fields = '__all__'
        verbose_name='Formulario: Contactos y Responsables por el Proyecto'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('proyecto', css_class='form-group col-md-2 mb-0'),
                Column('nombre', css_class='form-group col-md-2 mb-0'),
                Column('direccion', css_class='form-group col-md-2 mb-0'),
                Column('ci', css_class='form-group col-md-2 mb-0'),
                Column('telefono', css_class='form-group col-md-2 mb-0'),
                Column('mail', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'

            ),
            Submit('submit', 'Cargar')    
        )

























