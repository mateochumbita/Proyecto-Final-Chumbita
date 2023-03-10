from django.db import models



from django.contrib.auth.models import User
from usuario.views import *

class Celular(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    descripcion = models.TextField(null=True, blank=True)
    year = models.IntegerField() 
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    telefono = models.IntegerField()
    email = models.EmailField()
    imagen = models.ImageField(
        null=True, blank=True, upload_to="imagen_celular/")
    

    def __str__(self):
        return f" {self.titulo}, {self.modelo},  {self.precio}, {self.imagen}"



class Notebook(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    descripcion = models.TextField(null=True, blank=True)
    year = models.IntegerField() 
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    telefono = models.IntegerField()
    email= models.EmailField()
    imagen = models.ImageField(null=True, blank=True, upload_to="imagen_notebook/")

    def __str__(self):
        return f" {self.titulo}, {self.modelo},  {self.precio}, {self.imagen}"


class Televisor(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    descripcion = models.TextField(null=True, blank=True)
    year = models.IntegerField() 
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    telefono = models.IntegerField()
    email = models.EmailField()
    imagen = models.ImageField(null=True, blank=True, upload_to="imagen_televisor/")

    def __str__(self):
        return f" {self.titulo}, {self.modelo},  {self.precio}, {self.imagen}"


class Heladera(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    descripcion = models.TextField(null=True, blank=True)
    year = models.IntegerField() 
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    telefono = models.IntegerField()
    email = models.EmailField()
    imagen = models.ImageField(null=True, blank=True, upload_to='imagen_heladera')

    def __str__(self):
        return f" {self.titulo}, {self.modelo},  {self.precio}, {self.imagen}"


