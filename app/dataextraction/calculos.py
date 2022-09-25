from dataextraction.lectura_excel import ProcesamientoExcel, ProcesamientoExcelTest
from datetime import datetime
# from core.models import Extraccion,VencimientoImpuesto




class GraficoPeriodoImpuesto():
     # {2:1,1:1} #Grafica cantidad de impuestos procesados por periodo
    def cantidadImpuesto(self, lista_extraccExcel):
        grafico1={}
        for dicc in lista_extraccExcel:#lista diccionarios
            # lista de tipo diccionario
            periodo =  datetime.strptime(dicc['Fecha_vencimiento'], "%d/%m/%Y").month
            if periodo in grafico1.keys():#esta en el dicc

                grafico1[periodo] = grafico1[periodo] + 1
            else:
                grafico1[periodo] = 1
        return grafico1

    def formato_data(self, grafico1):
        imagen_uno = {}
        for periodo, cantidad in grafico1.items():
            imagen_uno[str(periodo)] = cantidad
        return imagen_uno

    def grafica_uno(self, imagen_uno):
        data ={
                'datasets': [{
                    'label': 'Procesamiento de Impuestos por mes',
                    'data': imagen_uno,
                    }]
            }
        return data

class GraficoEstadoImpuesto():
    def cantidadDocumentosProcesados(self, lista_procesadopdf):
        #Estado de documentos en el Procesamiento del Impuesto
        grafico2={} # {"Correccion":3, "No Procesado":4, "Ok Procesado":26}

        for dicc1 in lista_procesadopdf:
            procesado = dicc1['Procesado']
            if procesado in grafico2.keys():
                grafico2[procesado] = grafico2[procesado] + 1
            else:
                grafico2[procesado] = 1
        return grafico2

    def grafica_dos(self, grafico2):
        data ={
                'datasets': [{
                    'label': 'Procesamiento de Impuestos por mes',
                    'data': grafico2
                }]
                }
        return data

class GraficoEstadoMes():
    # Grafico 3
    # Se muestra por cada mes la cantidad de impuestos según Estado de Proceso.

    def datos_xls(self, lista_extraccExcel):
        datos = {}
        for dicc in lista_extraccExcel:#lista diccionarios

            # lista de tipo diccionario
            periodo = dicc['periodo_fiscal']
            id = dicc['id_razonsocial']
            mes =  datetime.strptime(dicc['Fecha_vencimiento'], "%d/%m/%Y").month
            year =  datetime.strptime(dicc['Fecha_vencimiento'], "%d/%m/%Y").year
            if (id,periodo, year) not in datos.keys():
                datos[(id,periodo,year)] = {} #se crea clave para ambas listas
            if mes in datos[(id,periodo,year)].keys():#esta en el dicc
                datos[(id,periodo, year)][mes] = datos[(id,periodo, year)][mes] + 1
            else:
                datos[(id,periodo, year)][mes] = 1
        return datos


    def datos_pdf(self, lista_procesadopdf): ##revisar como se guarda año
        datos_pdf = {}
        for dicc_pdf in lista_procesadopdf:
            periodo = dicc_pdf['periodo_fiscal']
            id = dicc_pdf['id_razonsocial']
            year = dicc_pdf['a–o'] #ojo toca ver como leer "ñ"
            estado = dicc_pdf['Procesado']
            if estado not in datos_pdf:
                datos_pdf[estado] = [(id,periodo,year)] #se crea clave para ambas listas
            elif (id,periodo,year) not in datos_pdf[estado]:
                datos_pdf[estado].append((id,periodo,year))
        return datos_pdf


    def union_datos(self, datos, datos_pdf):
        datos_grafico3 = []
        for c, v in datos_pdf.items():

            data = {'label': c} # dicionarior por estdo de proceso.
            data['data'] = {} # diccionario que contiene los meses.
            for clave_excel in v:
                if clave_excel in datos.keys():

                    mes, cantidad = list(zip(datos[clave_excel].keys(), datos[clave_excel].values()))[0]
                    # print(datos[clave_excel], mes, cantidad)
                    if mes not in data['data'].keys():
                        data['data'][mes] = cantidad
                    elif mes in data['data'].keys():
                        data['data'][mes] += cantidad
            datos_grafico3.append(data)

        return datos_grafico3

    def formato_data(self, datos_grafico3):
        lista_grafica_tres =[]

        for dicc in datos_grafico3: # recorro lista datasets

            dataset = {}
            for c, v  in dicc.items(): # recorre el dataset

                if c == 'label':
                    dataset[c] = v
                if c == 'data': # partición
                    dataset['data'] = v
                    imagen_tres={}
                    for periodo, cantidad in dicc[c].items():
                        imagen_tres[str(periodo)] = cantidad
                    dataset['data'] = imagen_tres

            lista_grafica_tres.append(dataset)
        return lista_grafica_tres

    def grafica_tres(self, lista_grafica_tres):
        data ={
                'datasets': lista_grafica_tres
                }
        return data

class GraficoRevisor_Estadoimpuesto():

    def datos_excel(self, lista_extraccExcel):
        datos_revisor ={} ## Se utilizó para el grafico de revisores

        for fila in lista_extraccExcel:
            nombre_revisor = fila['Revisor']
            id = fila['id_razonsocial']
            periodo = fila['periodo_fiscal']
            year =  datetime.strptime(fila['Fecha_vencimiento'], "%d/%m/%Y").year

            if  nombre_revisor not in  datos_revisor.keys():
                datos_revisor[nombre_revisor] = [(id,periodo, year)]
            elif (id,periodo, year) not in datos_revisor[nombre_revisor]:
                datos_revisor[nombre_revisor].append((id,periodo, year))
        return datos_revisor

    def datos_pdf(self, lista_procesadopdf): ##revisar como se guarda año
        datos_pdf = {}
        for dicc_pdf in lista_procesadopdf:
            periodo = dicc_pdf['periodo_fiscal']
            id = dicc_pdf['id_razonsocial']
            year = dicc_pdf['a–o'] #ojo toca ver como leer "ñ"
            estado = dicc_pdf['Procesado']
            if estado not in datos_pdf:
                datos_pdf[estado] = [(id,periodo,year)] #se crea clave para ambas listas
            elif (id,periodo,year) not in datos_pdf[estado]:
                datos_pdf[estado].append((id,periodo,year))
        return datos_pdf

    def union_datos(self, datos_revisor, datos_pdf):

        grafico_revisor = []

        for clave_revisor, v in datos_revisor.items():
            data = {'label': clave_revisor} # dicionarior por estdo de proceso.
            data['data'] = {} # diccionario que contiene los meses.
            for clave_unica in v:
                for clave_estado, valores_clave in datos_pdf.items():
                    if clave_unica in valores_clave:
                        if clave_estado not in data['data'].keys():
                            data['data'][clave_estado] = 1
                        else:
                            data['data'][clave_estado] = data['data'][clave_estado] + 1
            grafico_revisor.append(data)


        return grafico_revisor

    def formato_data(self, grafico_revisor):

        labels =[]
        datasets =[]
        for dicc in grafico_revisor:
            for clave, valor in dicc.items():
                if clave == 'label':
                    labels.append(dicc[clave])
        estados = ['OK Procesado', 'Pendiente', 'No procesado']
        for estado in estados:
            data_chart = {'label': estado, 'data':[]}
            for indice in range(len(grafico_revisor)):
                data_chart['data'].append(grafico_revisor[indice]['data'][estado])
            datasets.append(data_chart)

        return (labels, datasets)

    def grafica_cuatrl(self, labels, datasets):
         data ={
            'labels': labels,
            'datasets': datasets
         }
         return data


if __name__ == "django.core.management.commands.shell":
    ruta = "dataextraction/Recibos/Fechas_Indicadores.xlsx"
    # lista_extracciones = Extraccion.objects.filter(procesado='')
    # lista_vencimientos = VencimientoImpuesto.objects.filter(procesado='')
    # lista_extracciones.values()
    # lista_vencimientos.values()
    ruta = "dataextraction/Recibos/Fechas_Clientes.xlsx"
    rutapdf = "dataextraction/Recibos/ARG/AR02 BSF AR02_IVA_02.2022_F 731 DDJJ .pdf"
    datos_excel = ProcesamientoExcel.lectura_xls(ruta) #lista de diccionarios

    datos = ProcesamientoExcelTest.datos_procesado(rutapdf)
    resultado = ProcesamientoExcel.validar_datos(datos_excel, datos)

    grafico = GraficoPeriodoImpuesto()
    grafico.cantidadImpuesto(resultado)

    lista_procesadopdf = "BD"
