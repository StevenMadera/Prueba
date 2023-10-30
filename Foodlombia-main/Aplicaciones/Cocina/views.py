import uuid
from django.shortcuts import render, redirect
from .models import Receta
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db.models import Q


# Create your views here.

def home(request):
    recetasListadas = Receta.objects.all()
    return render(request, "gestionRecetas.html", {"recetas": recetasListadas})

def index(request):
    index = Receta.objects.all()
    return render(request, "index.html", {"recetas": index})

def receta(request, codigo):
    receta = Receta.objects.get(codigo=codigo)
    return render(request, "receta.html", {"receta": receta})

def gestionRecetas(request):
    gestionRecetas = Receta.objects.all()
    return render(request, "gestionRecetas.html", {"recetas": gestionRecetas})

def base(request):
    base = Receta.objects.all()
    return render(request, "base.html", {"base": base})

def registrarReceta(request):
    codigo = str(uuid.uuid1().int)[:6]
    nombre = request.POST['txtNombre']
    dificultad = request.POST['numDificultad']
    imagen = request.FILES.get('txtImagen')
    
    receta = Receta.objects.create(codigo=codigo, nombre=nombre, dificultad=dificultad, imagen=imagen)
    messages.success(request, 'Receta agregada')
    return redirect('/')

def editarReceta(request, codigo):
    receta = Receta.objects.get(codigo=codigo)
    return render(request, "editarReceta.html", {"receta": receta})

def edicionReceta(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    dificultad = request.POST['numDificultad']
    imagen = request.FILES.get('txtImagen')

    receta = Receta.objects.get(codigo=codigo)
    receta.codigo = codigo
    receta.nombre = nombre
    receta.dificultad = dificultad
    if imagen:
     receta.imagen = imagen
    receta.save()
    messages.info(request, 'Receta editada')

    return redirect('/')

def eliminarReceta(request, codigo):
    receta = Receta.objects.get(codigo=codigo)
    receta.delete()
    messages.error(request, 'Receta eliminada')

    return redirect('/')
    
def buscarReceta(request):
    if request.method == 'GET':
        textoBusqueda = request.GET['txtBuscar']
        recetas = Receta.objects.filter(Q(nombre__icontains=textoBusqueda))
        return render(request, 'gestionRecetas.html', {'recetas': recetas})
    else:
        return render(request, 'gestionRecetas.html')