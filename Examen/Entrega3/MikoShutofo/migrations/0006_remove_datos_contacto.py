# Generated by Django 4.1.5 on 2023-01-20 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MikoShutofo', '0005_remove_datos_correo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datos',
            name='contacto',
        ),
    ]
