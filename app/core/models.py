from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


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



class Pais(models.Model):
    codigo_iso = models.CharField(max_length=2)
    nombre = models.CharField(max_length=60)

class Mes(models.Model):
    nombre = models.CharField(max_length=20)
    numero = models.IntegerField(default=1)

class Año(models.Model):
    año = models.IntegerField(default=2021)


class VencimientoImpuesto(models.Model):
    mes = models.ForeignKey( Mes, on_delete=models.DO_NOTHING) #Relación clase mes
    año = models.ForeignKey(Año, on_delete=models.DO_NOTHING)
    nombre = models.CharField(max_length=20)
    razonSocial = ""
    cliente = models.CharField(max_length=50)
    taxId = models.CharField(max_length=5, null=False)
    tipo_presentacion = models.CharField(max_length=20)
    fechaVencimiento = models.DateTimeField('fecha_vencimiento', null=False)
    fechaEntrega = models.DateTimeField('fecha_entrega', null=False)
    review = models.CharField(max_length=60)


class Responsabilidad(models.Model):
    cargo = models.CharField(max_length=30)


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
    pais = models.ForeignKey(Pais, on_delete=models.DO_NOTHING)


class Empleado(models.Model):
    legajo = models.IntegerField(null=False)
    dni =  models.CharField(max_length=10)
    nombre = models.CharField(max_length=60)
    responsabilidad = models.ForeignKey(Responsabilidad, on_delete=models.DO_NOTHING)
    pais = models.OneToOneField(Pais, on_delete=models.DO_NOTHING)
    nombreUsuario = models.OneToOneField(Usuarios, on_delete=models.DO_NOTHING) #Relación 1 a 1
    empresa = models.ManyToManyField(Empresa) #Relación 1 a muchoes


class RelEmpresaImpuesto:
    empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING)
    impuesto = models.ForeignKey(Impuesto, on_delete=models.DO_NOTHING)
    pais = models.ForeignKey(Pais, on_delete=models.DO_NOTHING)
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
    pais = models.ForeignKey(Pais, on_delete=models.DO_NOTHING) #no estoy segura de la relación uno a muchos
    fecha_procesado = models.DateField(auto_now=True)

## Tablas de procesos

class DocumentoProceso(models.Model):
    idExtraccion = models.OneToOneField(Extraccion, on_delete=models.DO_NOTHING)
    estado = models.CharField(max_length=20) #cuando se inicializa no se abria problema?

class Documento(models.Model):
    idEmpresa = models.ManyToManyField(Empresa) #relacion uno a muchos
    url = models.CharField(null=False)
    idEstadoDoc = models.OneToOneField(DocumentoProceso, on_delete=models.DO_NOTHING) #relacion 1a1
