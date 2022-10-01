from django.http import HttpResponse
from django.shortcuts import render
import json
from core.models import Empresa, Documento, Proceso, Pais, Extraccion, VencimientoImpuesto
from dataextraction.argentina_extraccion import ExtraccionArgentina
from dataextraction.cololombia_extraccion import ExtraccionColombia
from dataextraction.mexico_extraccion import ExtraccionMexico
import os
from datetime import date
from dataextraction.lectura_excel import ProcesamientoExcel #jaz
from io import BytesIO
import openpyxl #ediciones


def index_view(request):
    # return HttpResponse('Hello World!')
    template = 'index.html'
    context = {
        "paragraph": 'Awesome test'
    }
    return render(request, template, context)


def pdf_upload_view(request):
    # return HttpResponse('Hello World!')
    empresas = Empresa.objects.all()
    template = 'pdfupload.html'
    context = {
        "empresas": empresas
    }
    return render(request, template, context)

def pdf_upload(request):
    empresa_id = request.POST.getlist('empresa')[0]
    files = request.FILES.getlist('files')
    empresa = Empresa.objects.get(id=empresa_id)

    for file in files:
        proceso = Proceso.objects.create(estado=Proceso.Estados.INICIADO)
        proceso.save()
        proceso.refresh_from_db()
        document = Documento.objects.create(id_empresa=empresa, id_proceso=proceso, nombre=file.name, documento_pdf=file)
        document.save()

        resultado  = process_pdf(proceso=proceso, document=document, empresa=empresa)
        proceso.id_extraccion = resultado
        proceso.estado = Proceso.Estados.PROCESADO
        proceso.save()

    empresas = Empresa.objects.all()
    template = 'pdfupload.html'
    context = {
        "empresas": empresas,
        "mensaje": "Se subieron y se procesaron los pdf correctamente"
    }
    return render(request, template, context)



def get_extractor(empresa:Empresa):
    if empresa.pais == str(Pais.ARGENTINA):
        return ExtraccionArgentina()
    elif empresa.pais == str(Pais.COLOMBIA):
        return ExtraccionColombia()
    elif empresa.pais == str(Pais.MEXICO):
        return ExtraccionMexico()

def process_pdf(proceso:Proceso, document:Documento, empresa:Empresa):
    extractor = get_extractor(empresa=empresa)
    texto = extractor.lectura(os.path.join('.',document.documento_pdf.path))
    lineas = extractor.procesamiento(text=texto)
    datos = extractor.extraccion(text=texto, lineas=lineas)
    extraccion = Extraccion(
        id_razonsocial = datos[0],
        nombre_empresa = datos[1],
        periodo_fiscal = datos[2],
        año = datos[3],
        numero_formulario = datos[4],
        n_verificacion = datos[5],
        saldo_pagado = datos[6],
        saldo_favor= datos[7],
        nombre_formulario = datos[8],
        pais = empresa.pais,
        fecha_procesado = date.today(),
    )

    extraccion.save()
    extraccion.refresh_from_db()
    return extraccion


## Subida xml fecha de vencimientos

def xml_upload_view(request):
    template = 'xml_upload.html'
    context = {
        "empresas": []
    }
    return render(request, template, context)


def xml_upload(request):
    # empresa_id = request.POST.getlist('empresa')[0]
    files = request.FILES.getlist('files')[0]
    # print(dir(files))
    lista = ProcesamientoExcel.lectura_xls(files)
    # print(lista)
    procesos = Proceso.objects.all().filter(estado= Proceso.Estados.PROCESADO)
    resultados = ProcesamientoExcel.validar_datos(procesos, lista)
    for resultado in resultados:
        # print(resultado)
        resultado.save()


    empresas = Empresa.objects.all()
    template = 'xml_upload.html'
    context = {
        "empresas": empresas,
        "mensaje": "Se subieron y se procesaron los pdf correctamente"
    }
    return render(request, template, context)



## Subida xml de "Pdfs periodos anteriores"
def xml_upload_period_view(request):
    template = 'xml-upload-periodos.html'
    context = {
        "carga": []
    }
    return render(request, template, context)


def xml_upload_period(request):
    files = request.FILES.getlist('files')[0]
    lectura_excel = openpyxl.load_workbook(filename=BytesIO(files.read()))
    hoja = lectura_excel.active

    for fila in hoja.iter_rows(min_row=2, max_row = hoja.max_row):
            proceso = Proceso.objects.create()
            proceso.estado = Proceso.Estados.INICIADO
            proceso.save()
            proceso.refresh_from_db()
            extraccion = Extraccion(
                id_razonsocial = fila[0].value,
                nombre_empresa = fila[1].value,
                periodo_fiscal = fila[2].value,
                año = fila[3].value,
                numero_formulario = fila[4].value,
                n_verificacion = fila[5].value,
                saldo_pagado = fila[6].value,
                saldo_favor= fila[7].value,
                nombre_formulario = fila[8].value,
                pais = fila[9].value,
                fecha_procesado = fila[10].value,
                proceso = proceso,
            )

            extraccion.save()
            extraccion.refresh_from_db()
            proceso.id_extraccion = extraccion
            proceso.estado = Proceso.Estados.FINALIZADO
            proceso.save()
    template = 'xml-upload-periodos.html'
    context = {
        "carga": []
    }
    return render(request, template, context)


## dashboard


def dashboard_view(request):
    template = 'dashboard.html'
    context = {}

    return render(request, template, context)


def dashboard_API(request):
    context = datos_graficos()
    return HttpResponse(json.dumps(context), content_type="application/json")

def datos_graficos():
    return {
        'grafico1':{
            'data':{
                    'datasets': [{
                        'label': 'Totales',
                        'data': {'3': 14, '2': 19, '1': 11},
                        'backgroundColor': [
                            'rgba(54, 162, 235, 0.2)',
                            # 'rgba(255, 206, 86, 0.2)',
                            # 'rgba(75, 192, 192, 0.2)',
                            # 'rgba(153, 102, 255, 0.2)',
                            # 'rgba(255, 159, 64, 0.2)'
                        ],
                        'borderColor': [

                            'rgba(54, 162, 235, 1)',
                            # 'rgba(255, 206, 86, 1)',
                            # 'rgba(75, 192, 192, 1)',
                            # 'rgba(153, 102, 255, 1)',
                            # 'rgba(255, 159, 64, 1)'
                        ],
                        'borderWidth': 1
                    }]
                }
        },
        'grafico2':{
            'data':{
                    'datasets': [{
                        'label': 'Estado de documentos por mes',
                        'data': {'OK Procesado': 26, 'Pendiente': 11, 'Corrección': 3, 'No procesado': 4},
                        'backgroundColor': [
                            'rgba(255, 99, 132, 0.2)',
                            'rgba(54, 162, 235, 0.2)',
                            'rgba(255, 206, 86, 0.2)',
                            'rgba(75, 192, 192, 0.2)',
                            'rgba(153, 102, 255, 0.2)',
                            'rgba(255, 159, 64, 0.2)'
                        ],
                        'borderColor': [
                            'rgba(255, 99, 132, 1)',
                            'rgba(54, 162, 235, 1)',
                            'rgba(255, 206, 86, 1)',
                            'rgba(75, 192, 192, 1)',
                            'rgba(153, 102, 255, 1)',
                            'rgba(255, 159, 64, 1)'
                        ],
                        'borderWidth': 1
                 }]
            }
        },
        'grafico3':{
            'data':{
                    'datasets': [
                            {
                                'label': 'OK Procesado',
                                'data': {'3': 3, '2': 16, '1': 7},
                                'backgroundColor': [
                                    'rgba(54, 162, 235, 0.2)',
                                ],
                                'borderColor': [
                                    'rgba(54, 162, 235, 1)',
                                ],
                                'borderWidth': 1

                            },
                            {
                                'label': 'Pendiente',
                                'data': {'3': 11},
                                'backgroundColor': [
                                    # 'rgba(54, 162, 235, 0.2)',
                                    'rgba(255, 99, 132, 0.2)',
                                ],
                                'borderColor': [
                                    # 'rgba(54, 162, 235, 1)',
                                    'rgba(255, 99, 132, 1)',
                                ],
                                'borderWidth': 1
                                    },

                            {
                                'label': 'Corrección',
                                'data': {'2': 3},
                                'backgroundColor': [
                                    'rgba(255, 206, 86, 0.2)',
                                ],
                                'borderColor': [
                                    'rgba(255, 206, 86, 1)',
                                ],
                                'borderWidth': 1
                            },

                            {
                                'label': 'No procesado',
                                'data': {'1': 4},
                                'backgroundColor': [
                                    'rgba(75, 192, 192, 0.2)',
                                ],
                                'borderColor': [
                                    'rgba(75, 192, 192, 1)',
                                ],
                                'borderWidth': 1
                            }
                        ]
                    }
        },
        'grafico4':{
            'data':{
                    'labels': ['Juan Espinosa','Camilo Sarmiento', 'Flor Cardenas', 'Maria Rivera'],
                    'datasets':
                    [
                        {
                            # 'axis': 'y',
                            'label': 'OK Procesado',
                             'data':  [6, 5, 6,3],
                                'backgroundColor': [
                                     'rgba(54, 162, 235, 0.2)',
                                ],
                                'borderColor': [
                                    'rgba(54, 162, 235, 1)',
                                ],
                                'borderWidth': 1
                        },
                        {
                            # 'axis': 'y',
                            'label': 'Pendiente',
                            'data': [ 3, 3, 3, 2],
                                'backgroundColor': [
                                    'rgba(255, 99, 132, 0.2)',
                                ],
                                'borderColor': [
                                    'rgba(255, 99, 132, 1)',
                                ],
                                'borderWidth': 1
                        },
                        {
                            # 'axis': 'y',
                            'label': 'No procesado',
                            'data': [ 1,1,6,1 ],
                                'backgroundColor': [
                                    'rgba(255, 206, 86, 0.2)',
                                ],
                                'borderColor': [
                                    'rgba(255, 206, 86, 1)',
                                ],
                                'borderWidth': 1
                        },

                    ]

                    }
                    }}

