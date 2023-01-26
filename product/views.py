from django.shortcuts import render

from django.shortcuts import render


from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from product.models import *

from product.forms import *

@login_required
def celular(request):
    contexto = {
        'celulares': Celular.objects.all()
    }
    return render(request=request, template_name='product/celulares.html',
     context=contexto )

@login_required
def notebook(request):
    contexto = {
        'notebooks': Notebook.objects.all()
    }
    return render(request=request, template_name='product/notebooks.html',
     context=contexto )


@login_required
def televisor(request):
    contexto = {
        'televisores': Televisor.objects.all()
    }
    return render(request=request, template_name='product/televisores.html',
     context=contexto )


@login_required
def heladera(request):
    contexto = {
        'heladeras': Heladera.objects.all()
    }
    return render(request=request, template_name='product/heladeras.html',
     context=contexto )


@login_required
def lavarropa(request):
    contexto = {
        'lavarropas': Lavarropa.objects.all()
    }
    return render(request=request, template_name='product/lavarropas.html',
     context=contexto )





#CREAR OBJETOS :=)

class CelularCreateView(LoginRequiredMixin, CreateView):
    model = Celular
    fields = ['usuario', 'titulo', 'marca', 'modelo', 'descripcion', 'year', 'precio', 'telefonoContacto', 'emailContacto', 'imagen']
    success_url = reverse_lazy('celulares')
    template_name = "product/formulario_celular.html"



class NotebookCreateView(LoginRequiredMixin, CreateView):
    model = Notebook
    fields = ['usuario', 'titulo', 'marca', 'modelo', 'descripcion', 'year', 'precio', 'telefonoContacto', 'emailContacto', 'imagen']
    success_url = reverse_lazy('notebooks')
    template_name = "product/formulario_notebook.html"


class TelevisorCreateView(LoginRequiredMixin, CreateView):
    model = Televisor
    fields = ['usuario', 'titulo', 'marca', 'modelo', 'descripcion', 'year', 'precio', 'telefonoContacto', 'emailContacto', 'imagen']
    success_url = reverse_lazy('televisores')
    template_name = "product/formulario_televisor.html"

class HeladeraCreateView(LoginRequiredMixin, CreateView):
    model = Heladera
    fields = ['usuario', 'titulo', 'marca', 'modelo', 'descripcion', 'year', 'precio', 'telefonoContacto', 'emailContacto', 'imagen']
    success_url = reverse_lazy('heladeras')
    template_name = "product/formulario_heladera.html"




class LavarropaCreateView(LoginRequiredMixin, CreateView):
    model = Lavarropa
    fields = ['usuario', 'titulo', 'marca', 'modelo', 'descripcion', 'year', 'precio', 'telefonoContacto', 'emailContacto', 'imagen']
    success_url = reverse_lazy('lavarropas')
    template_name = "producto/formulario_lavarropas.html"



#DETALLE


class CelularDetailView(LoginRequiredMixin, DetailView):
    model = Celular
    success_url = reverse_lazy('celulares')
    template_name = "product/detalle_celular.html"

#EDITAR
class CelularUpdateView(LoginRequiredMixin, UpdateView):
    model = Celular
    fields = ['usuario', 'titulo', 'marca', 'modelo', 'descripcion', 'year', 'precio', 'telefonoContacto', 'emailContacto', 'imagen']
    success_url = reverse_lazy('celulares')
    template_name = "product/editar_celular.html"


#ELIMINAR
class CelularDeleteView(LoginRequiredMixin, DeleteView):
    model = Celular
    success_url = reverse_lazy('celulares')
    template_name = "product/confirmar_eliminacion_celular.html"

