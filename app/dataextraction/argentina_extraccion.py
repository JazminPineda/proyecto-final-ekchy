from cgi import test
from posixpath import split
import pdfplumber
import re
#  Es para la notación de cadena raw de Python para los patrones de Unicode (str)
import locale # separador de mil en US O UK

class ExtraccionArgentina:
    ruta_archivo = "app/dataextraction/Recibos/ARG/AR02 BSF AR02_IVA_02.2022_F 731 DDJJ .pdf"
    #Atributos
    proceso_regex = r'[\d|\.]+,\d{2}$' #0
    id_tax_regex = r'\d{2}\-\d{8}\-\d{1}' #1
    periodo_regex = r'\d{2}\-\d{4}\s\d{0}' #2
    anio_regex = r'\d{2}\-\d{4}\s\d{0}' #3
    n_reguex = r'\d{6}\s+\/\s+\d{6}$' #4

    """Defino comportamientos y metodos para la clase, defino la estructura"""

    def lectura(self, ruta_archivo):
        if len(ruta_archivo) < 1:
            raise Exception("ruta no valida")

        with pdfplumber.open(ruta_archivo ) as pdf:
            pag = pdf.pages[0]
            text = pag.extract_text()
        return text

    def procesamiento(self, text):
        dic_renglones = {}
        categorias = [] # Descripcion
        lineas = text.split("\n")
       
        for linea in  lineas:
            if(re.search(self.proceso_regex, linea)): #0
                valor = re.findall(self.proceso_regex, linea) #0
                clave = re.sub(self.proceso_regex,"",linea).strip() #0
                dic_renglones[clave] = valor
       
        return lineas

    def extraccion(self, text, lineas):
        id_empresa = re.findall(self.id_tax_regex, text) #1
        id_output = id_empresa[0]

        nombre_output =  lineas[6].split(":")[1]

        anio = lineas[2]
        periodo_encontrado = re.search(self.periodo_regex, anio) #2
        periodo_validar = periodo_encontrado.group(0).split("-")[0]

        diccion_numero_palabras = {"01": 1, "02": 2, "03": 3, "04": 4, "05": 5, "06": 6, "07": 7,  "08": 8, "09": 9 }
        for valor in diccion_numero_palabras:
            if periodo_validar == valor:
                period_outuput = diccion_numero_palabras[valor]



        anio_conver = re.search(self.anio_regex, anio) #3
        anio_output = anio_conver.group(0).split("-")[1]

        n_formulario_output = lineas[5].split(".")[1]
        if n_formulario_output == "731":
            nombre_formulario = "IVA"

        n_for_verfic = lineas[4].split(".")
        n_forconver =re.search(self.n_reguex, n_for_verfic[0]) #4
        n_for_verifc = n_forconver.group(0).replace(" ", "")


        apagar_output = lineas[43].split(' ')[7]
        afavor_output = lineas[44].split(' ')[5]

        #puede ser otra posibilidad/ el tema es que cambia la palabra final
        #dic_renglones['Saldo de impuesto a favor de AFIP'][0]

        return (id_output, nombre_output, period_outuput, anio_output, n_formulario_output,  n_for_verifc, apagar_output, afavor_output, nombre_formulario)
    
    def proces_BaseDatos(self):
        pass

    # print(id_output, nombre_output, period_outuput, anio_output, n_formulario_output,  n_for_verifc, apagar_output, afavor_output, nombre_formulario)



