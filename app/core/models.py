from email.policy import default
import os
import uuid
from statistics import mode
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

class Pais(models.Choices):
    ARGENTINA = "ARG"
    COLOMBIA = "COL"
    MEXICO = "MEX"


OPCIONES_RESPOSABILIDADES = [
    ("REV", "Revisor"),
    ("PREP", "Preparador"),
    ("GER", "Gerente"),
]


OPCIONES_AÑO = [
    ("2021", "2021"),
    ("2022", "2021"),
    ("2023", "2021"),
]


def document_pdf_file_path(instance, filename):
    """Generate file path for new pdf file."""
    ext = os.path.splitext(filename)[1]
    filename = f"{uuid.uuid4()}{ext}"

    return os.path.join('uploads', 'pdf', filename)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError("User must have an email address.")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"


class Empleado(models.Model):
    legajo = models.IntegerField(null=False)
    dni = models.CharField(max_length=10)
    nombre = models.CharField(max_length=60)
    responsabilidad = models.CharField(
        max_length=10, choices=OPCIONES_RESPOSABILIDADES, blank=False
    )
    pais = models.CharField(max_length=3, choices=Pais.choices, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


# class Pais(models.Model):
#     codigo_iso = models.CharField(max_length=2)
#     nombre = models.CharField(max_length=60)

# class Mes(models.Model):
#     nombre = models.CharField(max_length=20)
#     numero = models.IntegerField(default=1)


class VencimientoImpuesto(models.Model):
    class EstadoVencimiento(models.Choices):
        PROCESADO= "Procesado"
        NO_PROCESADO= "No Procesado"


    class Mes(models.IntegerChoices):
        ENERO = 1
        FEBRERO = 2
        MARZO = 3
        ABRIL = 4
        MAYO = 5
        JUNIo = 6
        JULIO = 7
        AGOSTO = 8
        SEPTIEMBRE = 9
        OCTUBRE = 10
        NOVIEMBRE = 11
        DICIEMBRE = 12

    pais = models.CharField(max_length=3, choices=Pais.choices, blank=False)
    mes = models.IntegerField(choices=Mes.choices, blank=True)  # Relación clase mes
    año = models.IntegerField(choices=OPCIONES_AÑO, blank=False)
    #nombre = models.CharField(max_length=20)
    id_razonsocial = models.CharField(max_length=30)  # se añade
    nombre_empresa = models.CharField(max_length=50, default="")  # se añade
    periodo_fiscal = models.CharField(max_length=20)  # se añade
    #cliente = models.CharField(max_length=50)
    #taxId = models.CharField(max_length=5, null=False)
    nombre_formulario = models.CharField(max_length=20)
    fecha_vencimiento = models.DateTimeField(null=True)
    fecha_entrega = models.DateTimeField(null=True)
    fecha_revisado = models.DateTimeField(null=True)
    review = models.CharField(max_length=60)
    proceso = models.CharField(max_length=50, choices=EstadoVencimiento.choices, blank=False)

    def __str__(self):
        return f'{self.pais} | {self.id_razonsocial} | {self.nombre_empresa} | {self.periodo_fiscal} | {self.año} |{self.nombre_formulario} | {self.fecha_vencimiento} | {self.proceso}'
# class Responsabilidad(models.Model):
#     cargo = models.CharField(max_length=10, choices=OPCIONES_RESPOSABILIDADES, blank=False)


class Impuesto(models.Model):
    class NumeroFormulario(models.Choices):
        ARGENTINA_731 = "731"
        COLOMBIA_300 = "300"
        MEXICO_001 = "001"

    nombre_impuesto = models.CharField(max_length=10)
    numero_fomulario = models.CharField(max_length=3, choices=NumeroFormulario.choices, default="", blank=True)
    pais = models.CharField(max_length=3, choices=Pais.choices, blank=False)

    def __str__(self) -> str:
        return self.nombre_impuesto


# class RelEmpresaImpuesto:
#     empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING)
#     impuesto = models.ForeignKey(Impuesto, on_delete=models.DO_NOTHING)
#     pais = models.CharField(max_length=3, choices=OPCIONES_PAIS, blank=False)
#     class Meta:
#         unique_together = ({'empresa', 'impuesto', 'pais'})


class Extraccion(models.Model):
    id_razonsocial = models.CharField(max_length=20)
    nombre_empresa = models.CharField(max_length=50)
    numero_formulario = models.CharField(max_length=6)
    nombre_formulario = models.CharField(max_length=15)
    n_verificacion = models.CharField(max_length=40, null=False)
    periodo_fiscal = models.IntegerField(null=False)
    año = models.IntegerField(choices=OPCIONES_AÑO)
    saldo_pagado = models.DecimalField(null=False, decimal_places=2, max_digits=20)
    saldo_favor = models.DecimalField(null=False, decimal_places=2, max_digits=20)
    pais = models.CharField(max_length=3, choices=Pais.choices, blank=False)
    fecha_procesado = models.DateField(auto_now=True)
    # documento_pdf = models.FileField(up)

    def __str__(self) -> str:
        return f'{self.id_razonsocial} {self.nombre_empresa} {self.n_verificacion}' + super().__str__()

## Tablas de procesos


class Proceso(models.Model):
    class Estados(models.Choices):
        INICIADO = 'Iniciado' # Sube el pdf
        PROCESADO = 'Procesado' # Extraccion BD PDF
        FINALIZADO = 'Finalizado' # se compara con el excel y se guarda BD
        FAllIDO = 'Fallido' # Falla en cualquier etapa


    id_extraccion = models.OneToOneField(Extraccion, on_delete=models.DO_NOTHING, null=True)
    estado = models.CharField(max_length=20, choices=Estados.choices)

    def __str__(self) -> str:
        return f'{self.id}, {self.estado}'

class Empresa(models.Model):
    razonSocial = models.CharField(max_length=50)
    id_razonSocial = models.CharField(max_length=20)
    impuestos = models.ManyToManyField(Impuesto)  ##relacion
    pais = models.CharField(max_length=3, choices=Pais.choices, blank=False)
    empleado = models.ManyToManyField(Empleado)

    def __str__(self) -> str:
        return self.razonSocial


class Documento(models.Model):
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True)
    id_proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=100, default='')
    documento_pdf = models.FileField(upload_to=document_pdf_file_path)

    def delete(self,*args, **kargs):
        self.documento_pdf.delete()
        return super().delete(*args, **kargs)

    def __str__(self) -> str:
        return f'{self.nombre}, {self.documento_pdf}'
