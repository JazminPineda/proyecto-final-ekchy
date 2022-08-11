from cgi import test
from posixpath import split
import pdfplumber
import re
#  Es para la notación de cadena raw de Python para los patrones de Unicode (str)
import locale # separador de mil en US O UK

ruta_arg = "app/dataextraction/Recibos/ARG/AR02 BSF AR02_IVA_02.2022_F 731 DDJJ .pdf"


with pdfplumber.open(ruta_arg ) as pdf:
    pag = pdf.pages[0]
    text = pag.extract_text()
    lineas = text.split("\n")


dic_renglones = {}
categorias = [] # Descripcion


#print(text)
for linea in  lineas:
    if(re.search(r'[\d|\.]+,\d{2}$', linea)):
        valor = re.findall(r'[\d|\.]+,\d{2}$', linea)
        clave = re.sub(r'[\d|\.]+,\d{2}$',"",linea).strip()

        dic_renglones[clave] = valor

#print(dic_renglones)


id_empresa = re.findall(r'\d{2}\-\d{8}\-\d{1}', text)#1
id_output = id_empresa[0]

nombre_output =  lineas[6].split(":")[1]

anio = lineas[2]
periodo_regex = re.search(r'\d{2}\-\d{4}\s\d{0}', anio)
periodo_output = periodo_regex.group(0).split("-")[0]

anio_regex = re.search(r'\d{2}\-\d{4}\s\d{0}', anio)
anio_output = anio_regex.group(0).split("-")[1]

n_formulario_output = lineas[5].split(".")[1]

print(id_output, nombre_output, periodo_output, anio_output, n_formulario_output)
# apagar_output = int(dic_renglones['Total saldo a pagar'].replace(",", ""))
# afavor_output = int(dic_renglones['o Total saldo a favor'].replace(",", ""))
