
from posixpath import split
import pdfplumber
import re
#  Es para la notación de cadena raw de Python para los patrones de Unicode (str)
import locale # separador de mil en US O UK


ruta_mex = "app/dataextraction/Recibos/MEX/MEX_VAT_Feb2022_Detail.pdf"


#extra texto pero me daña lo demas
with pdfplumber.open(ruta_mex, laparams = { "word_margin": 0.01 }) as pdf:
    pag = pdf.pages[0]
    #Se incluye esta funcionalidad porque aparecia todo junto por lo tanto
    text = pag.extract_text(x_tolerance=1, y_tolerance=1)
    lineas =text.split('\n')
#rint(lineas)


id_empresa = lineas[1]
id_output = id_empresa.split(" ")[1]


nombre_razon =  lineas[2]
nombre_limpia = nombre_razon.split(":")[1]
nombre_output = nombre_limpia[:-11]


periodo =lineas[4].split(" ")
periodo_validar = periodo[4]


diccion_mes_palabras = {"Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4, "Mayo": 5, "Junio": 6, "Julio": 7,  "Agosto": 8, "Septiembre": 9, "Octubre": 10, "Noviembre": 11,
"Diciembre": 12 }
for valor in diccion_mes_palabras:
    if periodo_validar == valor:
        period_outuput = diccion_mes_palabras[valor]


ano_output = periodo[6]

fecha_pres = periodo =lineas[5].split(" ")
fecha_present_output = fecha_pres[5]


#CREAR METODO PARA VALIDAR FORMULARIOS#
nomb_formulario = lineas[8]

if nomb_formulario == "IMPUESTO AL VALOR AGREGADO POR LA PRESTACIÓN DE SERVICIOS DIGITALES":
    n_formulario_output = "001"
    nomb_output = "IVA DIGITALES"
else:
    print("No es un recibo de pago valido ")

#print(nomb_formulario)
n_formulario = lineas[6].split(" ")
n_verificacion_output= n_formulario[3]


apagar_output = lineas[14]
afavor_output = "0"



print(id_output, nombre_output, period_outuput, ano_output, n_formulario_output, n_verificacion_output, apagar_output, afavor_output, fecha_present_output, nomb_output)









