# Generated by Django 3.2.15 on 2022-09-17 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20220917_2307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documento',
            name='id_empresa',
        ),
        migrations.AddField(
            model_name='documento',
            name='id_empresa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.empresa'),
        ),
        migrations.RemoveField(
            model_name='documento',
            name='id_proceso',
        ),
        migrations.AddField(
            model_name='documento',
            name='id_proceso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.proceso'),
        ),
    ]
