from django.urls import path
from .views import *

urlpatterns=[
    path('', inicio, name='inicio'),
    path('buscar/', buscar, name='buscar'),
    path('registro/', register, name='register'),
    path('tus-productos/', productos, name='productos'),
    path('eliminar_producto/<id>/', eliminar_producto, name='eliminar_producto'),
    path('agregar-anuncio/', agregar_producto, name='agregar'),
    path('modificar-anuncio/<id>/', modificar_producto, name='modificar'),
    path('categorias/<id>/', categorias, name='categorias'),
]

