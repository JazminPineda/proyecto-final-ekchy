# Generated by Django 3.2.15 on 2022-09-27 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20220927_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vencimientoimpuesto',
            name='nombre_empresa',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vencimientoimpuesto',
            name='proceso',
            field=models.CharField(choices=[('PROCESADO', 'Procesado'), ('NO PROCESADO', 'No Procesado')], max_length=20),
        ),
    ]
