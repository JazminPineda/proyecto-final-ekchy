# import pandas as pd
import openpyxl #ediciones
from core.models import Extraccion
from dataextraction.argentina_extraccion import ExtraccionArgentina
from collections import defaultdict

 # celdas = hoja['A1':'I13']
    # hoja.max_column
    # hoja.max_row
    # hoja.min_column
    # hoja.min_row



campos = ["periodo_fiscal", 'nombreFormulario', 'Fecha_vencimiento', 'Fecha_envio_cliente', 'Fecha_revisado', 'Revisor', 'año', 'numeroFormulario', ' n_verificacion', 'saldoPagado', 'saldoFavor', 'fecha_procesado']

class ProcesamientoExcel():

    @classmethod
    def lectura_xls(cls, ruta):
        lectura_excel = openpyxl.load_workbook(filename=ruta, data_only=True)
        hoja = lectura_excel.active
        lista=[]
        for fila in hoja.rows:
            lista.append(ProcesamientoExcelTest.fila_dicc([celda.value  for celda in fila]))
        return lista

    @classmethod
    def comparo(cls, fila_dic, extrccion_pdf):
        return fila_dic['id_razonsocial'] == extrccion_pdf.id_razonsocial

    @classmethod
    def validar_datos(cls, dato_xls, extraccion_pdf):
        for fila_dic in dato_xls:
            if ProcesamientoExcel.comparo(fila_dic, extraccion_pdf):
                fila_dic['proceso'] = 'ok procesado'
            else:
                fila_dic['proceso'] = 'pendiente'
        return dato_xls

class ProcesamientoExcelTest():

    @classmethod
    def fila_dicc(cls, fila):
        return {
            "pais":fila[0],
            "id_razonsocial":fila[1],
            "nombre_empresa":fila[2],
            "periodo_fiscal": fila[3],
            'nombreFormulario':fila[4],
            'Fecha_vencimiento':fila[5],
            'Fecha_envio_cliente':fila[6],
            'Fecha_revisado':fila[7],
            'Revisor':fila[8],
        }

    @classmethod
    def datos_procesado(cls, rutapdf):
        ex_arg = ExtraccionArgentina()
        texto = ex_arg.lectura(ruta_archivo=rutapdf)
        lineas = ex_arg.procesamiento(texto)
        datos = ex_arg.extraccion(texto, lineas)
        return datos


if __name__ == "django.core.management.commands.shell":
    ruta = "dataextraction/Recibos/Fechas_Clientes.xlsx"
    rutapdf = "dataextraction/Recibos/ARG/AR02 BSF AR02_IVA_02.2022_F 731 DDJJ .pdf"
    datos_excel = ProcesamientoExcel.lectura_xls(ruta) #lista de diccionarios

    datos = ProcesamientoExcelTest.datos_procesado(rutapdf)
    resultado = ProcesamientoExcel.validar_datos(datos_excel, datos)
    for i in resultado:
            print(i['id_razonsocial'],i['proceso'])
