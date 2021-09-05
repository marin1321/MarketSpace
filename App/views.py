from django.contrib import auth
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import login
from django.core.paginator import Paginator
from django.contrib.auth.models import User


# Create your views here.

 

def inicio(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    data = {
        'productos':productos,
        'categorias':categorias
    }
    return render(request, 'app/inicio.html', data)

def buscar(request):
    if request.GET["buscar"]:
        dato=request.GET["buscar"]
        productos = Producto.objects.filter(nombre__icontains=dato) 

        return render(request, 'app/busqueda.html', {'productos':productos, 'query':dato})
    else:
        return redirect(to="inicio")

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = username.strip()
        email = email.strip()  # Eliminar espacios y líneas nuevas
        password = password.strip()
        if User.objects.filter(username=username).exists():
            messages.success(request, "este nombre de usuario ya ha sido registrado")
            return redirect(to="login")
        user = User.objects.create_user(username, email, password)
        login(request, user)
        request.session['id'] = user.id   # Registrar que el usuario ha iniciado sesión
        messages.success(request, "Te has registrado exitosamente")
        return redirect(to="inicio")

def productos(request):
    global user_id 
    user_id = request.user.id
    usuarioo = User.objects.get(id=user_id)
    
    productos = Producto.objects.filter(usuario=usuarioo)
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 3)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity':productos,
        'paginator':paginator
    }
    return render(request, 'app/productos.html', data)

def eliminar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="productos")

def agregar_producto(request):
    data = {
        'Form': ProductoForm(),
    }

    if request.method=='POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            foto=request.FILES.get('foto')
            nombre = request.POST.get('nombre')
            precio = request.POST.get('precio')
            categoria = request.POST.get('categoria')
            estado = request.POST.get('estado')
            descripcion = request.POST.get('descripcion')
            fecha_Expiracion = request.POST.get('fecha_Expiracion')
            nombre = nombre.strip()  # Eliminar espacios y líneas nuevas
            precio = precio.strip()
            categoria = categoria.strip()
            estado = estado.strip()  # Eliminar espacios y líneas nuevas
            descripcion = descripcion.strip()
            fecha_Expiracion = fecha_Expiracion.strip()
            producto = Producto()
            producto.foto = foto
            producto.nombre = nombre
            producto.precio = precio
            categoria = Categoria.objects.get(id=categoria)
            producto.categoria = categoria = categoria
            estado = Estado.objects.get(id=estado)
            producto.estado = estado
            producto.descripcion = descripcion
            producto.fecha_Expiracion = fecha_Expiracion
            global user_id 
            user_id = request.user.id
            user = User.objects.get(id=user_id)
            producto.usuario = user
            producto.save()
            messages.success(request, "Producto Registrado")
            return redirect(to="productos")
        else:
            data["Form"] = formulario

    return render(request, 'app/agregar.html', data)

def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    data = {
        'Form': ProductoForm(instance=producto),
    }
    if request.method=='POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="productos")
        else:
            data["form"] = formulario
    return render(request, 'app/modificar.html', data)
