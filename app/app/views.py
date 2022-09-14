from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse('Hello World!')
    template = 'index.html'
    context = {
        "paragraph": 'Awesome test'
    }
    return render(request, template, context)


def pdf_upload(request):
    # return HttpResponse('Hello World!')
    template = 'pdfupload.html'
    context = {
        "paragraph": 'Awesome test'
    }
    return render(request, template, context)
