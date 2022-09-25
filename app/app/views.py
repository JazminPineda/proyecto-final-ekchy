from django.http import HttpResponse
from django.shortcuts import render
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



