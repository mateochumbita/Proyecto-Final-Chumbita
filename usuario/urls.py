from django.contrib import admin
from django.urls import path
from usuario.forms import *

from usuario.views import *
urlpatterns = [

path('inicio/', inicio, name='inicio'),
path('registro/', registro, name='registro'),  
path('login/', login_view, name='login'),
path('logout/', CustomLogoutView.as_view(), name="logout"),
#AVATAR
path('agregar-avatar/', agregar_avatar, name="agregar_avatar"),
path('editar-perfil/', ProfileUpdateView.as_view(), name="editar_perfil"),
]

