from email.policy import default
from pyexpat import model
from django.db import models


class Pais(models.Model):
    codigo_iso = models.CharField(max_length=2)
    nombre = models.CharField(max_length=60)

class Mes(models.Model):
    nombre = models.CharField(max_length=20)
    numero = models.IntegerField(default=1)

class Año(models.Model):
    año = models.IntergerField(default=2021)


class VencimientoImpuesto(models.Model):
    mes = models.ForeignKey(Mes) #Relación clase mes
    año = models.ForeignKey(Año)
    nombre = models.CharField(max_length=20)
    razonSocial = ""
    cliente = models.CharField(max_length=50)
    taxId = models.CharField(max_length=5, null=False)
    tipo_presentacion = models.CharField(max_length=20)
    fechaVencimiento = models.DateTimeField('fecha_vencimiento' null=False)
    fechaEntrega = models.DateTimeField('fecha_entrega', null=False)
    review = models.CharField(max_length=60)
   
class Responsabilidad(models.Model):
    cargo = models.CharField(max_length=30)

class Grupo(models.Model):
    nombre = models.CharField(max_length=10)

class Impuesto(models.Model):
    nombreimpuesto = models.CharField(max_length=10)
    numero_fomr = models.CharField(max_length=6)

class Empresa(models.Model):
    razonSocial =  models.CharField(max_length=50)
    id_razonSocia = models.CharField(max_length=20)
    paises = models.ManyToManyField(Pais)
    pais = models.ForeignKey(Pais)
   
class RelEmpresaImpuesto:
    empresa = models.ForeignKey(Empresa)
    impuesto = models.ForeignKey(Impuesto)
    pais = models.ForeignKey(Pais)
    class Meta:
        unique_together = ({'empresa', 'impuesto', 'pais'})

class Empleado(models.Model):
    legajo = models.IntegerField(null=False)
    dni =  models.CharField(max_length=10)
    nombre = models.CharField(max_length=60)
    cargo = models.ForeignKey(Responsabilidad)
    

class Extraccion(models.Model):
    id_razonsocial = models.CharField(max_length=10)
    nombre_empresa = models.CharField(max_length=50)
    noForm = models.CharField(max_length=6)
    periodo_fiscal = models.IntegerField(null=False)
    año = models.IntegerField(null=False)
    n_verificacion = mmodels.IntegerField(null=False)eignKey(Grupo)


