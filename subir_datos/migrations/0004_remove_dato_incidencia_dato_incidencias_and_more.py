# Generated by Django 4.1.7 on 2023-04-12 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subir_datos', '0003_dato_dni_dato_incidencia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dato',
            name='incidencia',
        ),
        migrations.AddField(
            model_name='dato',
            name='incidencias',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='INCIDENCIAS'),
        ),
        migrations.AlterField(
            model_name='dato',
            name='DNI',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='DNI'),
        ),
    ]
