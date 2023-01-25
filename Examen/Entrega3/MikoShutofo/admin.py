from django.contrib import admin
from .models import TipoCliente, Datos, Tipo, Producto

# Register your models here.
admin.site.register(TipoCliente)
admin.site.register(Datos)

admin.site.register(Tipo)
admin.site.register(Producto)