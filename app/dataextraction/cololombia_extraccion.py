# Formulario 300 IVA Colombia

from posixpath import split
import pdfplumber
import re
#  Es para la notación de cadena raw de Python para los patrones de Unicode (str)
import locale # separador de mil en US O UK

ruta_col = "app/dataextraction/Recibos/COL/Decla. IVA II BIM 2022 - CO10.pdf"

with pdfplumber.open(ruta_col) as pdf:
    pag = pdf.pages[0]
    text = pag.extract_text()


# Lectura de formulario descripción, renglon y valor
# for m in re.finditer(r'.+?\s\d{2}\s(\d{1,3}[,]?){1,}', text):
#     print(m.group(0))
nombres_form=[]
dic_renglones = {}
categorias = [] # Descripcion
for m in re.finditer(r'.+?\s\d{2}\s(\d{1,3}[,]?){1,}', text):
    renglon = m.group(0)
    categoria, valor = (re.split(r'\s\d{2}\s', renglon)) #desempaquetado Unpacking de datos(tupla/lista)
    categorias.append(categoria)
    dic_renglones[categoria.strip()] = valor

#print(categorias)


id_empresa =  text.split('\n')[6]
id_output = id_empresa.replace(" ", "")

nombre_empresa =  text.split('\n')[8]
nombre_output = nombre_empresa[:-3]

anio = re.search(r'Año\s([0-9]\s){4}', text)
periodo_regex = re.search(r'([1-6]\s){1}',anio.group(0))
periodo_output = periodo_regex.group(0).replace(" ", "")


anio_regex = re.search(r'([0-9]\s){4}', anio.group(0))
anio_output = anio_regex.group(0).replace(" ", "")

n_formulario = text.split('\n')[3]
n_formulario_output = n_formulario[:3]
n_verificacion_output = text.split('\n')[3]

apagar_output = int(dic_renglones['Total saldo a pagar'].replace(",", ""))
afavor_output = int(dic_renglones['o Total saldo a favor'].replace(",", ""))
print(apagar_output, afavor_output)
