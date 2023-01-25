from django.shortcuts import render, redirect
from .models import Datos, Producto, Tipo, TipoCliente
from .forms import DatosForm, ProductoForm

# Create your views here.
def home(request):
    return render(request, 'Principal.html')

def fotos(request):
    return render(request, 'Fotos.html')

def somos(request):
    return render(request, 'QuienesSomos.html')

def taller(request):
    return render(request, 'Talleres.html')

def ayaka(request):
    return render(request, 'PelucheAyaka.html')

def kazuha(request):
    return render(request, 'PelucheKazuha.html')

def cerdo(request):
    return render(request, 'PelucheCerdo.html')

def zenit(request):
    return render(request, 'Zenitzu.html')

def nezu(request):
    return render(request, 'Nezuko.html')

def drak(request):
    return render(request, 'Draken.html')

def rana(request):
    return render(request, 'Ranaverde.html')

def koro(request):
    return render(request, 'KoroneWof.html')

def lu(request):
    return render(request, 'Luffyy.html')

def colors(request):
    return render(request, 'ApiColores.html')

def clientes(request):
    datos = Datos.objects.all()
    datos={
        'gente':datos
    }
    return render(request, 'Clientes.html', datos)

def eliminar(request, id):
    datos = Datos.objects.get(rut=id)
    datos.delete()
    return redirect('clientes')
    
def crear(request):
    if request.method=='POST': 
        datosform = DatosForm(request.POST)
        if datosform.is_valid():
            datosform.save()     
            return redirect('clientes')
    else:
        datosform=DatosForm()
    return render(request, 'CrearCliente.html', {'datosform': datosform})

def modificar(request, id):
    dato = Datos.objects.get(rut=id) 
    datos ={
        'form': DatosForm(instance=dato) 
    }
    if request.method=='POST':
        formulario = DatosForm(data=request.POST, instance=dato)
        if formulario.is_valid:
            formulario.save()
            return redirect('clientes')
    
    return render(request, 'modificar.html', datos)

def pro(request):
    producto = Producto.objects.all()
    producto = {
        'producto' : producto
    }    
    return render(request, 'ProductosMostrar.html', producto)

def addpro(request):
    if request.method=='POST': 
        productoform = ProductoForm(request.POST)
        if productoform.is_valid():
            productoform.save()     
            return redirect('pro')
    else:
        productoform=ProductoForm()
    return render(request, 'CrearProducto.html', {'productoform': productoform})