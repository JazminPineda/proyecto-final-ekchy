import pdfplumber
import re


def inicio():
    ruta_col = 'IVAIIB2022 - CO10.pdf'
    with pdfplumber.open(ruta_col) as pdf:
        pag = pdf.pages[0]
        text = pag.extract_text()

    lineas = text.split('\n')
    
    form= lineas[0]
    form_n= lineas[3]
    nombre = lineas[8]
    resul_nombre = re.search(r'([A-Z]|\s)+', nombre)
    id_e = lineas[6].replace(" ", "")
    nombre = resul_nombre.group(0)
    print(form, form_n, nombre)


if __name__ == '__main__':
    inicio()

        
