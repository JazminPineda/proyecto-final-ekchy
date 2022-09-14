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
    """Generate file path for new recipe image."""
    ext = os.path.splitext(filename)[1]
    filename = f"{uuid.uuid4()}{ext}"


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
    OPCIONES_PROCESO = [
        ("PROCESADO", "Procesado"),
        ("NO PROCESADO", "No Procesado"),
    ]

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
    mes = models.IntegerField(choices=Mes.choices, blank=False)  # Relación clase mes
    año = models.IntegerField(choices=OPCIONES_AÑO, blank=False)
    nombre = models.CharField(max_length=20)
    id_razonsocial = models.CharField(max_length=20)  # se añade
    nombre_empresa = models.CharField(max_length=20)  # se añade
    periodo_fiscal = models.CharField(max_length=20)  # se añade
    cliente = models.CharField(max_length=50)
    taxId = models.CharField(max_length=5, null=False)
    nombre_formulario = models.CharField(max_length=20)
    fecha_vencimiento = models.DateTimeField(null=False)
    fecha_entrega = models.DateTimeField(null=False)
    fecha_revisado = models.DateTimeField(null=False)
    review = models.CharField(max_length=60)
    proceso = models.CharField(max_length=20, choices=OPCIONES_PROCESO, blank=False)


# class Responsabilidad(models.Model):
#     cargo = models.CharField(max_length=10, choices=OPCIONES_RESPOSABILIDADES, blank=False)


class Impuesto(models.Model):
    class NumeroFormulario(models.IntegerChoices):
        ARGENTINA = "731"
        COLOMBIA = "300"
        MEXICO = "001"

    nombre_impuesto = models.CharField(max_length=10)
    numero_fomulario = models.CharField(max_length=3, choices=NumeroFormulario.choices, default="", blank=True)
    pais = models.CharField(max_length=3, choices=Pais.choices, blank=False)


# class RelEmpresaImpuesto:
#     empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING)
#     impuesto = models.ForeignKey(Impuesto, on_delete=models.DO_NOTHING)
#     pais = models.CharField(max_length=3, choices=OPCIONES_PAIS, blank=False)
#     class Meta:
#         unique_together = ({'empresa', 'impuesto', 'pais'})


class Extraccion(models.Model):
    id_razonsocial = models.CharField(max_length=10)
    nombre_empresa = models.CharField(max_length=50)
    numero_formulario = models.CharField(max_length=6)
    nombre_formulario = models.CharField(max_length=15)
    n_verificacion = models.IntegerField(null=False)
    periodo_fiscal = models.IntegerField(null=False)
    año = models.IntegerField(choices=OPCIONES_AÑO)
    saldo_pagado = models.IntegerField(null=False)
    saldo_favor = models.IntegerField(null=False)
    pais = models.CharField(max_length=3, choices=Pais.choices, blank=False)
    fecha_procesado = models.DateField(auto_now=True)
    # documento_pdf = models.FileField(up)


## Tablas de procesos


class Proceso(models.Model):
    OPCIONES_ESTADO = [
        ("INICIADO", "Iniciado"),
        ("PROCESADO", "Procesado"),
        ("FINALIZADO", "Finalizado"),
    ]
    id_extraccion = models.OneToOneField(Extraccion, on_delete=models.DO_NOTHING)
    estado = models.CharField(max_length=20, choices=OPCIONES_ESTADO)


class Empresa(models.Model):
    razonSocial = models.CharField(max_length=50)
    id_razonSocia = models.CharField(max_length=20)
    impuestos = models.ManyToManyField(Impuesto)  ##relacion
    pais = models.CharField(max_length=3, choices=Pais.choices, blank=False)
    empleado = models.ManyToManyField(Empleado)


class Documento(models.Model):
    id_empresa = models.ManyToManyField(Empresa)
    id_proceso = models.ManyToManyField(Proceso)
    documento_pdf = models.FileField(upload_to=document_pdf_file_path)
