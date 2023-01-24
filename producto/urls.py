from django.contrib import admin
from django.urls import path

from producto.views import *
from producto.forms import *

urlpatterns = [
#PRODUCTOS
path('celulares/', celular, name='celulares'),
path('notebooks/', notebook, name='notebooks'),
path('televisores/', televisor, name='televisores'),
path('heladeras/', heladera, name='heladeras'),
path('lavarropas/', lavarropa, name='lavarropas'),





#CREAR PRODUCTOS
path('publicar-celular/', CelularCreateView.as_view(), name="publicar_celular"),
path('publicar-notebook/', NotebookCreateView.as_view(), name="publicar_notebook"),
path('publicar-televisor/', TelevisorCreateView.as_view(), name="publicar_televisor"),
path('publicar-heladera/', HeladeraCreateView.as_view(), name="publicar_heladera"),

    
]



