from django.http import HttpResponse
from django.shortcuts import render
import json
from core.models import Empresa, Documento, Proceso, Pais, Extraccion
from dataextraction.argentina_extraccion import ExtraccionArgentina
from dataextraction.cololombia_extraccion import ExtraccionColombia
from dataextraction.mexico_extraccion import ExtraccionMexico
import os
from datetime import date


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
        document = Documento.objects.create(id_empresa=empresa, id_proceso=proceso, nombre=file.name, documento_pdf=file)
        document.save()

        process_pdf(proceso=proceso, document=document, empresa=empresa)

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
        pais = Pais.ARGENTINA,
        fecha_procesado = date.today(),
    )
    print(extraccion)
    extraccion.save()


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
                        'label': 'Procesamiento de Impuestos por mes',
                        'data': {'3': 14, '2': 19, '1': 11},
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
        'grafico2':{
            'data':{
                    'datasets': [{
                        'label': 'Estado de documentos por mes',
                        'data': {'OK Procesado': 26, 'Pendiente': 11, 'Corrección': 3, 'No procesado': 4},
                 }]
            }
        },
        'grafico3':{
            'data':{
                    'datasets': [
                            {
                                'label': 'OK Procesado',
                                'data': {'3': 3, '2': 16, '1': 7},
                                'backgroundColor': '#dc3545',

                            },
                            {
                                'label': 'Pendiente',
                                'data': {'3': 11},
                                'backgroundColor': '#0d6efd',
                            },

                            {
                                'label': 'Corrección',
                                'data': {'2': 3},
                                'backgroundColor': '#20c997',
                            },

                            {
                                'label': 'No procesado',
                                'data': {'1': 4},
                                'backgroundColor': '#ffc107',
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
                             'backgroundColor': '#0d6efd',
                        },
                        {
                            # 'axis': 'y',
                            'label': 'Pendiente',
                            'data': [ 3, 3, 3, 2],
                            'backgroundColor': '#20c997',
                        },
                        {
                            # 'axis': 'y',
                            'label': 'No procesado',
                            'data': [ 1,1,6,1 ],
                            'backgroundColor': '#ffc107',
                        },

                    ]

                    }
                    }}

