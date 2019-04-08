#!/usr/bin/env python
# coding=utf-8

__licence__ = "GNU/GPLv3"
__author__ = "Marcelo Zunino (InfoPrimo SL) 2017"

# ##################################################################################
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by the
#  Free Software Foundation; either version 3, or (at your option) any later
#  version.
#
#  This program is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
#  or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
#  for more details. <https://www.gnu.org/licenses/>
# ##################################################################################
# coding=utf-8
#!/usr/bin/python

import sys
try:
    from suds.client import Client
    from suds.sudsobject import asdict
    from dateutil.parser import parse
    from datetime import datetime, date
except Exception as ex:
    print("\n\tVerificar dependecia de módulos:\n `suds` ")
    sys.exit(1)

def ayudin():
    print("\n\tAyuda\n")
    print("\n\tuso: cotizaciones [<desdefecha> <hastafecha>]")
    print("\t     Sin opciones: valores al último cierre ")
    print("\t     Rangos > 5 a días. Final del rango < hoy")
    print("\t Formato de fechas: aaaa-mm-dd ")
    print("\t\t\taaaa: año 4 dígitos\n\t\t\t  mes y día en 2 dígitos\n")
    sys.exit(1)

def parametros(pars_in):
    """
        Verificación de parámetros de entrada
    :param pars_in: string: -h
                            dd-mm-yyyy
                            dd-mm-yyyy dd-mm-yyyy
                            nada
    :return: tupla  <(fecha_desde, fecha_hasta)> ó <(None,None)> o string: <muestra ayuda>

    """
    _desde = _hasta = None
    if  len(pars_in) == 2 and pars_in[1] == '-h':
        ayudin()

    if len(pars_in) == 1:
        # devolver ultima cotización
        #  _desde = _hasta = None
        pass

    elif len(pars_in) == 3:

        if len(pars_in[1]) == 10 and len(pars_in[2]) == 10:
            try:
                parse(pars_in[1])
                parse(pars_in[2])
                _desde, _hasta = (pars_in[1],pars_in[2])
                #TODO:  verificar formatos de valores para `parse`
                #       parse acepta diferentes tipos de separadores y fechas!
                #       analizar si vale la pena mejorar esto.
            except:
                print("\n\t[ERROR]  %s no parece ser una fecha válida\n" % (pars_in[2],))
                ayudin()
        else:
            print("\n\t[ERROR]  %s, %s o ambas no parecen ser fechas válidas\n" % (pars_in[1], pars_in[2]))
            ayudin()
        if not (_desde <= _hasta):
            print("\n\t[ERROR]  %s debe ser mayor o igual a %s \n" % (pars_in[2], pars_in[1],))
            ayudin()
    else:
        print("\n\t[ERROR] Verificar parámetros !! %s \n" % (pars_in[1:],))
        ayudin()
    return _desde, _hasta

if __name__ == '__main__':
    #import ipdb; ipdb.set_trace()
    #print sys.argv, len(sys.argv)
    fdesde, fhasta = parametros(sys.argv)
    if fdesde and fhasta:
        d_fdesde = datetime.strptime(fdesde,"%Y-%m-%d").date()
        d_fhasta = datetime.strptime(fhasta,"%Y-%m-%d").date()
        if (d_fhasta - d_fdesde).days < 6 or d_fhasta > date.today():
            print("\n\t[ERROR] El rango no es válido! ")
            print("\t        El rango debe tener una extención mayor a 5 días")
            print("\t        La fecha final del rango debe ser menor que la fecha de hoy")
            ayudin()

    if fdesde and fhasta:
        client = Client("https://cotizaciones.bcu.gub.uy/wscotizaciones/servlet/awsbcucotizaciones?wsdl")
        cotiza_obj = client.factory.create("wsbcucotizacionesin")
        cotiza_obj.FechaDesde = fdesde
        cotiza_obj.FechaHasta = fhasta
        cotiza_obj.Grupo  = 2      
        cotiza_obj.Moneda = {'item' : [2225,9800,9900]}
        ret = client.service.Execute(cotiza_obj)
        #print ret
        cotizacion = asdict(ret.datoscotizaciones).items()[0][1]
        print("\t Moneda \t\t Compra \t Venta")
        for moneda in cotizacion:
            print("\t %s \t %s \t %s \n" % (moneda.Nombre, moneda.TCC, moneda.TCV))
    elif fdesde == None and fhasta == None:
        client = Client("https://cotizaciones.bcu.gub.uy/wscotizaciones/servlet/awsultimocierre?wsdl")
        ultimo_obj = client.factory.create("wsultimocierreout")
        ret = client.service.Execute(ultimo_obj)
        client = Client("https://cotizaciones.bcu.gub.uy/wscotizaciones/servlet/awsbcucotizaciones?wsdl")
        cotiza_obj = client.factory.create("wsbcucotizacionesin")
        cotiza_obj.FechaDesde = ret.Fecha
        cotiza_obj.FechaHasta = ret.Fecha
        cotiza_obj.Grupo  = 2      
        cotiza_obj.Moneda = {'item' : [2225,9800,9900]}
        ret = client.service.Execute(cotiza_obj)
        #print ret
        cotizacion = asdict(ret.datoscotizaciones).items()[0][1]
        print("\t Moneda \t\t Compra \t Venta")
        for moneda in cotizacion:
            print("\t %s \t %s \t %s \n" % (moneda.Nombre, moneda.TCC, moneda.TCV))
    else:
        print("\n\t%s\n" % ("Algo salió mal... :( ",))    