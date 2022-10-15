from core.models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.http import HttpResponse
from django.urls import path
from django.utils.translation import gettext_lazy as _
from app.views import xml_upload_period_view


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""

    ordering = ["id"]
    list_display = ["email", "name"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("name",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    readonly_fields = ["last_login"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "name",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )


# my dummy model
class PeriodosAnteriores(models.Model):

    class Meta:
        verbose_name_plural = 'Subir periodos anteriores'
        app_label = 'core'

# def my_custom_view(request):
#     return HttpResponse('Admin Custom View')

class PeriodosAnterioresAdmin(admin.ModelAdmin):
    model = PeriodosAnteriores

    def get_urls(self):
        view_name = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)
        return [
            path('', xml_upload_period_view, name=view_name),
        ]

admin.site.register(PeriodosAnteriores, PeriodosAnterioresAdmin)

admin.site.register(User, UserAdmin)
admin.site.register(Empresa,)
admin.site.register(Impuesto)
admin.site.register(Empleado)
admin.site.register(Proceso)
admin.site.register(Documento)
admin.site.register(Extraccion)
admin.site.register(VencimientoImpuesto)
