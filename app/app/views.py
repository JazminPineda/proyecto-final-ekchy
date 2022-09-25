from django.http import HttpResponse
from django.shortcuts import render
from core.models import Empresa, Documento, Proceso, Pais, Extraccion
from dataextraction.argentina_extraccion import ExtraccionArgentina
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
    import logging
    empresa_id = request.POST.getlist('empresa')[0]
    files = request.FILES.getlist('files')
    empresa = Empresa.objects.get(id=empresa_id)

    for file in files:
        proceso = Proceso.objects.create(estado=Proceso.Estados.INICIADO)
        proceso.save()
        document = Documento.objects.create(id_empresa=empresa, id_proceso=proceso, nombre=file.name, documento_pdf=file)
        document.save()
        extractor = ExtraccionArgentina()
        # os.path.join('.',document.documento_pdf)
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
    return HttpResponse('Hello World!')


# def process_pdf(proceso:Proceso, document:Documento, empresa:Empresa):
#     extractor = None
#     if empresa.pais == Pais.ARGENTINA:

#     elif empresa.pais == Pais.ARGENTINA:
#     elif empresa.pais == Pais.ARGENTINA:
