# Generated by Django 4.1.5 on 2023-01-20 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoCliente',
            fields=[
                ('idTipoCliente', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Tipo Cliente')),
                ('nombreTipoCliente', models.CharField(max_length=30, verbose_name='Tipo de Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Rut')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('apellidoPat', models.CharField(max_length=20, verbose_name='Apellido paterno')),
                ('apellidoMat', models.CharField(max_length=20, verbose_name='Apellido materno')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MikoShutofo.tipocliente')),
            ],
        ),
    ]
