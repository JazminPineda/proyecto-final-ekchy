from models import Empresa, Documento
from rest_framework import serializers


class EmpresaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empresa


class FileUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Documento
        fields = "__all__"



