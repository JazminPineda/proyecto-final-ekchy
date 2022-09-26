# Formulario 300 IVA Colombia
from cgi import test
from posixpath import split
import pdfplumber
import re

#  Es para la notación de cadena raw de Python para los patrones de Unicode (str)
import locale

from dataextraction.clase_abstracta import Extraer  # separador de mil en US O UK

# from app.app.models import Extraccion # Modulo BD


class ExtraccionColombia(Extraer):  # a#

    ruta_archivo = "app/dataextraction/Recibos/COL/Decla. IVA II BIM 2022 - CO10.pdf"
    _laparams = {"detect_vertical": True, "word_margin": 1, "char_margin": 20}

    formato_texto = r".+?\s\d{2}\s(\d{1,3}[,]?){1,}"  # 1
    desempaq_regex = r"\s\d{2}\s"  # 2
    anio = r"Año\s([0-9]\s){4}"  # 3
    periodo_regex = r"([1-6]\s){1}"  # 4
    anio_regex = r"([0-9]\s){4}"  # 5


    def extract_text(self, pdf) -> str:
        pag = pdf.pages[0]
        return pag.extract_text(x_tolerance=3, y_tolerance=3)

    # print(text)
    # Lectura de formulario descripción, renglon y valor
    # for m in re.finditer(r'.+?\s\d{2}\s(\d{1,3}[,]?){1,}', text):
    #     print(m.group(0))

    def procesamiento(self, text):
        nombres_form = []
        dic_renglones = {}
        categorias = []  # Descripcion

        for m in re.finditer(self.formato_texto, text):  # 1
            renglon = m.group(0)
            categoria, valor = re.split(
                self.desempaq_regex, renglon
            )  # 2 desempaquetado Unpacking de datos(tupla/lista)
            categorias.append(categoria)
            dic_renglones[categoria.strip()] = valor

        return dic_renglones  # devuelve el dicc?

        # print(categorias)

    def extraccion(self, text, lineas):

        id_empresa = text.split("\n")[6]
        id_output = id_empresa.replace(" ", "")

        empresa = text.split("\n")[8]
        sociedad_output = empresa[:-3]

        annio = re.search(self.anio, text)  # 3
        perioddo = re.search(self.periodo_regex, annio.group(0))  # 4
        periodo_output = perioddo.group(0).replace(" ", "")

        anio_regex = re.search(self.anio_regex, annio.group(0))  # 5
        anio_output = anio_regex.group(0).replace(" ", "")

        n_formulario = text.split("\n")[3]
        n_formulario_output = n_formulario[:3]
        if n_formulario_output == "300":
            nombre_output = "IVA"
        n_verificacion_output = text.split("\n")[3]

        apagar_output = int(lineas["Total saldo a pagar"].replace(",", ""))
        afavor_output = int(lineas["o Total saldo a favor"].replace(",", ""))

        # fecha_present = dic_renglones['982. CódFiigrmo aC o'].replace(",", "")
        # fecha_present = pag.extract_text()

        datos = (
            id_output,
            sociedad_output,
            periodo_output,
            anio_output,
            n_formulario_output,
            n_verificacion_output,
            apagar_output,
            afavor_output,
            nombre_output,
        )
        return datos
