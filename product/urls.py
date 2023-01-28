from django.contrib import admin
from django.urls import path

from product.views import *
from product.forms import *

urlpatterns = [
#PRODUCTOS
path('celulares/', celular, name='celulares'),
path('notebooks/', notebook, name='notebooks'),
path('televisores/', televisor, name='televisores'),
path('heladeras/', heladera, name='heladeras'),
path('lavarropas/', lavarropa, name='lavarropas'),
path('acerca-de-mi/', aboutme, name='acerca_de_mi'),
#CREAR PRODUCTOS
path('publicar-celular/', CelularCreateView.as_view(), name="publicar_celular"),
path('publicar-notebook/', NotebookCreateView.as_view(), name="publicar_notebook"),
path('publicar-televisor/', TelevisorCreateView.as_view(), name="publicar_televisor"),
path('publicar-heladera/', HeladeraCreateView.as_view(), name="publicar_heladera"),
path('publicar-lavarropa/', LavarropaCreateView.as_view(), name="publicar_lavarropa"),
#DETALLE DE PRODUCTO
path('detalle-celular/<int:pk>/', CelularDetailView.as_view(), name='ver_celular'),
path('detalle-notebook/<int:pk>/', NotebookDetailView.as_view(), name='ver_notebook'),
path('detalle-televisor/<int:pk>/', TelevisorDetailView.as_view(), name='ver_televisor'),
path('detalle-heladera/<int:pk>/', HeladeraDetailView.as_view(), name='ver_heladera'),
path('detalle-lavarropa/<int:pk>/', LavarropaDetailView.as_view(), name='ver_lavarropa'),
#EDITAR PRODUCTO
path('editar-celular/<int:pk>/', CelularUpdateView.as_view(), name="editar_celular"),
path('editar-notebook/<int:pk>/', NotebookUpdateView.as_view(), name="editar_notebook"),
path('editar-televisor/<int:pk>/', TelevisorUpdateView.as_view(), name="editar_televisor"),
path('editar-heladera/<int:pk>/', HeladeraUpdateView.as_view(), name="editar_heladera"),
path('editar-lavarropa/<int:pk>/', LavarropaUpdateView.as_view(), name="editar_lavarropa"),
#ELIMINAR PRODUCTO
path('eliminar-celular/<int:pk>/', CelularDeleteView.as_view(), name="eliminar_celular"),
path('eliminar-notebook/<int:pk>/', NotebookDeleteView.as_view(), name="eliminar_notebook"),
path('eliminar-televisor/<int:pk>/', TelevisorDeleteView.as_view(), name="eliminar_televisor"),
path('eliminar-heladera/<int:pk>/', HeladeraDeleteView.as_view(), name="eliminar_heladera"),
path('eliminar-lavarropa/<int:pk>/', LavarropaDeleteView.as_view(), name="eliminar_lavarropa"),
#BUSCAR
path('buscar-celulares/', buscar_celular, name="buscar_celular"),
path('buscar-notebooks/', buscar_notebook, name="buscar_notebook"),
path('buscar-televisoress/', buscar_televisor, name="buscar_televisor"),
path('buscar-heladeras/', buscar_heladera, name="buscar_heladera"),


]



