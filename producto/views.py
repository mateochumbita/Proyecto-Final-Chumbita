from django.shortcuts import render


from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from producto.models import *

from producto.forms import *

@login_required
def celular(request):
    contexto = {
        'celulares': Celular.objects.all()
    }
    return render(request=request, template_name='producto/celulares.html',
     context=contexto )

@login_required
def notebook(request):
    contexto = {
        'notebooks': Notebook.objects.all()
    }
    return render(request=request, template_name='producto/notebooks.html',
     context=contexto )


@login_required
def televisor(request):
    contexto = {
        'televisores': Televisor.objects.all()
    }
    return render(request=request, template_name='producto/televisores.html',
     context=contexto )


@login_required
def heladera(request):
    contexto = {
        'heladeras': Heladera.objects.all()
    }
    return render(request=request, template_name='producto/heladeras.html',
     context=contexto )


@login_required
def lavarropa(request):
    contexto = {
        'lavarropas': Lavarropa.objects.all()
    }
    return render(request=request, template_name='producto/lavarropas.html',
     context=contexto )





#CREAR OBJETOS :=)

class CelularCreateView(LoginRequiredMixin, CreateView):
    model = Celular
    fields = ['usuario', 'titulo', 'marca', 'modelo', 'descripcion', 'year', 'precio', 'telefonoContacto', 'emailContacto', 'imagen']
    success_url = reverse_lazy('celulares')
    template_name = "producto/formulario_celular.html"



class NotebookCreateView(LoginRequiredMixin, CreateView):
    model = Notebook
    fields = ['usuario', 'titulo', 'marca', 'modelo', 'descripcion', 'year', 'precio', 'telefonoContacto', 'emailContacto', 'imagen']
    success_url = reverse_lazy('notebooks')
    template_name = "producto/formulario_notebook.html"


class TelevisorCreateView(LoginRequiredMixin, CreateView):
    model = Televisor
    fields = ['usuario', 'titulo', 'marca', 'modelo', 'descripcion', 'year', 'precio', 'telefonoContacto', 'emailContacto', 'imagen']
    success_url = reverse_lazy('televisores')
    template_name = "producto/formulario_televisor.html"

class HeladeraCreateView(LoginRequiredMixin, CreateView):
    model = Heladera
    fields = ['usuario', 'titulo', 'marca', 'modelo', 'descripcion', 'year', 'precio', 'telefonoContacto', 'emailContacto', 'imagen']
    success_url = reverse_lazy('heladeras')
    template_name = "producto/formulario_heladera.html"




class LavarropaCreateView(LoginRequiredMixin, CreateView):
    model = Lavarropa
    fields = ['usuario', 'titulo', 'marca', 'modelo', 'descripcion', 'year', 'precio', 'telefonoContacto', 'emailContacto', 'imagen']
    success_url = reverse_lazy('lavarropas')
    template_name = "producto/formulario_lavarropa.html"


