from django.db import models

# Create your models here.

class TipoCliente(models.Model):
    idTipoCliente = models.IntegerField(primary_key=True, verbose_name='Id Tipo Cliente') 
    nombreTipoCliente=models.CharField(max_length=30, verbose_name='Tipo de Cliente')

    def __str__(self):
        return self.nombreTipoCliente


class Datos(models.Model):
    rut=models.CharField(max_length=10, primary_key=True, verbose_name='Rut')
    nombre=models.CharField(max_length=20, verbose_name='Nombre')
    apellidoPat=models.CharField(max_length=20, verbose_name='Apellido paterno')
    apellidoMat=models.CharField(max_length=20, verbose_name='Apellido materno')
    contato=models.CharField(max_length=15, verbose_name='Número de contacto')
    correo=models.CharField(max_length=50, verbose_name='Correo Eletrónico')
    categoria=models.ForeignKey(TipoCliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.rut

class Tipo(models.Model):
    idTipo = models.IntegerField(primary_key=True, verbose_name="ID Tipo Producto")
    nombreTipo = models.CharField(max_length=30, blank=True, verbose_name='Nombre Tipo Producto')

    def __str__(self):
        return self.nombreTipo


class Producto(models.Model):
    idproducto=models.CharField(primary_key=True, max_length=8, verbose_name='ID Producto')
    nombre=models.CharField(max_length=50, blank=True, verbose_name='Nombre producto')
    tamaño=models.CharField(max_length=50, blank=True, verbose_name='Tamaño en cm')
    imagen=models.ImageField(upload_to="imagenes", null=True, verbose_name='Imagen')
    categoria=models.ForeignKey(Tipo, default=1, on_delete=models.CASCADE, verbose_name='Categoria')

    def __str__(self):
        return self.idproducto
