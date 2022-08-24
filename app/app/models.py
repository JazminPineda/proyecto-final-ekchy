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



class Usuarios(models.Model):
    nombreUsuario = models.IntegerField(max_length=15)
    correo = models.CharField(null=False) #revisar
    contraseña = models.CharField(null=False)


class Impuesto(models.Model):
    nombreimpuesto = models.CharField(max_length=10)
    numero_fomr = models.CharField(max_length=6)
    pais = models.ManyToManyField(Pais)


class Empresa(models.Model):
    razonSocial =  models.CharField(max_length=50)
    id_razonSocia = models.CharField(max_length=20)
    paises = models.ManyToManyField(Pais, through="RelEmpresaImpuesto", related_name="pais")  ##relacion pais
    impuestos = models.ManyToManyField(Impuesto, through="RelEmpresaImpuesto", related_name="impuesto") ##relacion
    pais = models.ForeignKey(Pais)


class Empleado(models.Model):
    legajo = models.IntegerField(null=False)
    dni =  models.CharField(max_length=10)
    nombre = models.CharField(max_length=60)
    responsabilidad = models.ForeignKey(Responsabilidad)
    pais = models.OneToOneField(Pais)
    nombreUsuario = models.OneToOneField(Usuarios) #Relación 1 a 1
    empresa = models.ManyToManyField(Empresa) #Relación 1 a muchoes


class RelEmpresaImpuesto:
    empresa = models.ForeignKey(Empresa)
    impuesto = models.ForeignKey(Impuesto)
    pais = models.ForeignKey(Pais)
    class Meta:
        unique_together = ({'empresa', 'impuesto', 'pais'})


class Extraccion(models.Model):
    id_razonsocial = models.CharField(max_length=10)
    nombre_empresa = models.CharField(max_length=50)
    numeroFormulario = models.CharField(max_length=6)
    nombreFormulario = models.CharField(max_length=15)
    n_verificacion = models.IntegerField(null=False)
    periodo_fiscal = models.IntegerField(null=False)
    año = models.IntegerField(null=False)
    saldoPagado = models.IntegerField(null=False)
    saldoFavor = models.IntegerField(null=False)
    grupo = models.ManyToManyField(Grupo) #no estoy segura de la relación uno a muchos


## Tablas de procesos

class DocumentoProceso(models.Model):
    idExtraccion = models.OneToOneField(Extraccion)
    estado = models.CharField(max_length=20) #cuando se inicializa no se abria problema?

class Documento(models.Model):
    idGrupo = models.ManyToManyField(Grupo) #relacion uno a muchos
    url = models.CharField(null=False)
    idEstadoDoc = models.OneToOneField(DocumentoProceso) #relacion 1a1
