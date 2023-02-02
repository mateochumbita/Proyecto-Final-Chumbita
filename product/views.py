from django.shortcuts import render

from django.shortcuts import render


from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from product.models import *
from django.contrib.messages.views import SuccessMessageMixin
from product.forms import *


def aboutme(request):
    return render(
        request=request,
        template_name='product/acerca_de_mi.html',
    )
    


def celular(request):
    contexto = {
        'celulares': Celular.objects.all()
    }
    return render(request=request, template_name='product/celulares.html',
     context=contexto )


def notebook(request):
    contexto = {
        'notebooks': Notebook.objects.all()
    }
    return render(request=request, template_name='product/notebooks.html',
     context=contexto )



def televisor(request):
    contexto = {
        'televisores': Televisor.objects.all()
    }
    return render(request=request, template_name='product/televisores.html',
     context=contexto )



def heladera(request):
    contexto = {
        'heladeras': Heladera.objects.all()
    }
    return render(request=request, template_name='product/heladeras.html',
     context=contexto )









#CREAR OBJETOS :=)

class CelularCreateView(LoginRequiredMixin, CreateView):
    model = Celular
    form_class= NuevoCelularForm
    success_url = reverse_lazy('celulares')
    template_name = "product/formulario_celular.html"
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(CelularCreateView, self).form_valid(form)


class NotebookCreateView(LoginRequiredMixin, CreateView):
    model = Notebook
    form_class = NuevaNotebookForm
    success_url = reverse_lazy('notebooks')
    template_name = "product/formulario_notebook.html"
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(NotebookCreateView, self).form_valid(form)


class TelevisorCreateView(LoginRequiredMixin, CreateView, SuccessMessageMixin):
        model = Televisor
        form_class= NuevoTelevisorForm
        success_url = reverse_lazy('televisores')
        template_name = "product/formulario_televisor.html"
        def form_valid(self, form):
            form.instance.usuario = self.request.user
            return super(TelevisorCreateView, self).form_valid(form)
        
class HeladeraCreateView(LoginRequiredMixin, CreateView):
    model = Heladera
    form_class = NuevaHeladeraForm
    success_url = reverse_lazy('heladeras')
    template_name = "product/formulario_heladera.html"
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(HeladeraCreateView, self).form_valid(form)







#DETALLE


class CelularDetailView(LoginRequiredMixin, DetailView):
    model = Celular
    success_url = reverse_lazy('celulares')
    template_name = "product/detalle_celular.html"
    
class NotebookDetailView(LoginRequiredMixin, DetailView):
    model = Notebook
    success_url = reverse_lazy('notebooks')
    template_name = "product/detalle_notebook.html"


class TelevisorDetailView(LoginRequiredMixin, DetailView):
    model = Televisor
    success_url = reverse_lazy('televisores')
    template_name = "product/detalle_televisor.html"



class HeladeraDetailView(LoginRequiredMixin, DetailView):
    model = Heladera
    
    success_url = reverse_lazy('heladeras')
    template_name = "product/detalle_heladera.html"
    
    

    


#EDITAR
class CelularUpdateView(LoginRequiredMixin, UpdateView):
    model = Celular
    form_class= EdicionCelularForm
    success_url = reverse_lazy('celulares')
    template_name = "product/editar_celular.html"


class NotebookUpdateView(LoginRequiredMixin, UpdateView):
    model = Notebook
    form_class =  EdicionNotebookForm
    success_url = reverse_lazy('notebooks')
    template_name = "product/editar_notebook.html"

class TelevisorUpdateView(LoginRequiredMixin, UpdateView):
    model = Televisor
    form_class = EdicionTelevisorForm
    success_url = reverse_lazy('televisores')
    template_name = "product/editar_televisor.html"


class HeladeraUpdateView(LoginRequiredMixin, UpdateView):
    model = Heladera
    form_class = EdicionHeladeraForm
    success_url = reverse_lazy('heladeras')
    template_name = "product/editar_heladera.html"









#ELIMINAR
class CelularDeleteView(LoginRequiredMixin, DeleteView):
    model = Celular
    success_url = reverse_lazy('celulares')
    template_name = "product/confirmar_eliminacion_celular.html"
    
    
class NotebookDeleteView(LoginRequiredMixin, DeleteView):
    model = Notebook
    success_url = reverse_lazy('notebooks')
    template_name = "product/confirmar_eliminacion_notebook.html"
    
    
class TelevisorDeleteView(LoginRequiredMixin, DeleteView):
    model = Televisor
    success_url = reverse_lazy('televisores')
    template_name = "product/confirmar_eliminacion_televisor.html"

class HeladeraDeleteView(LoginRequiredMixin, DeleteView):
    model = Heladera
    success_url = reverse_lazy('heladeras')
    template_name = "product/confirmar_eliminacion_heladera.html"


    
    
#BUSCAR


def buscar_celular(request):
    if request.method == "POST":
        data = request.POST
        celulares = Celular.objects.filter(
            Q(marca__contains=data['busqueda']) |Q(modelo__contains=data['busqueda']) )
        
        contexto = {
            'celulares': celulares
        }
        return render(
            request=request,
            template_name='product/celulares.html',
            context=contexto,
        )
        

def buscar_notebook(request):
    if request.method == "POST":
        data = request.POST
        notebooks = Notebook.objects.filter(
            Q(marca__contains=data['busqueda']) |Q(modelo__contains=data['busqueda']) )
        
        contexto = {
            'notebooks': notebooks
        }
        return render(
            request=request,
            template_name='product/notebooks.html',
            context=contexto,
        )
        
        
def buscar_televisor(request):
    if request.method == "POST":
        data = request.POST
        televisores = Televisor.objects.filter(
            Q(marca__contains=data['busqueda']) |Q(modelo__contains=data['busqueda']) )
        
        contexto = {
            'televisores': televisores
        }
        return render(
            request=request,
            template_name='product/televisores.html',
            context=contexto,
        )
        
        
        
def buscar_heladera(request):
    if request.method == "POST":
        data = request.POST
        heladeras = Heladera.objects.filter(
            Q(marca__contains=data['busqueda']) |Q(modelo__contains=data['busqueda']) )
        
        contexto = {
            'heladeras': heladeras
        }
        return render(
            request=request,
            template_name='product/heladeras.html',
            context=contexto,
        )



#COMENTARIOS




