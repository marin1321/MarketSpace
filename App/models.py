from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Estado(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    foto = models.ImageField(upload_to="productos", null=True)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    descripcion = models.TextField()
    numero_telefonico = models.IntegerField()
    fecha_Publicacion = models.DateField(auto_now_add=True ,blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.SET, blank=True, null=True)
    
    def __str__(self):
        return self.nombre

opciones_consulta = [
    
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felitaciones"],
    [4, "Otro asunto"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consulta)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
