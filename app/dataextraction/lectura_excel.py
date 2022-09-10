# import pandas as pd
import openpyxl #ediciones
from core.models import Extraccion
from dataextraction.argentina_extraccion import ExtraccionArgentina

rutapdf = "dataextraction/Recibos/ARG/AR02 BSF AR02_IVA_02.2022_F 731 DDJJ .pdf"

ex_arg = ExtraccionArgentina()
texto = ex_arg.lectura(ruta_archivo=rutapdf)

lineas = ex_arg.procesamiento(texto)
datos = ex_arg.extraccion(texto, lineas)
print(datos)

ruta = "dataextraction/Recibos/Fechas_Clientes.xlsx"
campos = ['Pais', 'Identificador', 'Nombre', 'Periodo', 'Impuesto', 'Fecha_vencimiento', 'Fecha_envio_cliente', 'Fecha_revisado', 'Revisor']


def lectura_xls(ruta):
    lectura_excel = openpyxl.load_workbook(filename=ruta)
    return lectura_excel
    #print(lectura_excel)

print(lectura_xls(ruta))

# def procesamiento(lectura_excel, campos):
#     procesamiento_excel = pd.concat([lectura_excel,])

ex = Extraccion()

