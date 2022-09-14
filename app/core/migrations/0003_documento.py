# Generated by Django 3.2.15 on 2022-09-14 20:35

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_empleado_empresa_extraccion_impuesto_proceso_vencimientoimpuesto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento_pdf', models.FileField(upload_to=core.models.document_pdf_file_path)),
                ('id_empresa', models.ManyToManyField(to='core.Empresa')),
                ('id_proceso', models.ManyToManyField(to='core.Proceso')),
            ],
        ),
    ]
