from django.contrib import admin
from .models import *

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "categoria", "estado", "fecha_Publicacion", "fecha_Expiracion", "usuario"]
    list_per_page = 10
    search_fields = ["nombre"]
    list_filter = ["categoria", "estado"]

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria)
admin.site.register(Estado)