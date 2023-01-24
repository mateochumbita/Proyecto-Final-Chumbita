from django import forms
from django.contrib.auth.models import User 
from producto.models import *

class  CelularForm(forms.ModelForm):

    class Meta:
        model = Celular
        fields = ['usuario', 'titulo', 'marca', 'modelo', 'descripcion', 'year', 'precio',  'telefonoContacto', 'emailContacto', 'imagen']


class  NotebookForm(forms.ModelForm):

    class Meta:
        model = Notebook
        fields = ['usuario', 'titulo', 'marca', 'modelo', 'descripcion', 'year', 'precio',  'telefonoContacto', 'emailContacto', 'imagen']


class  TelevisorForm(forms.ModelForm):

    class Meta:
        model = Televisor
        fields = ['usuario', 'titulo', 'marca', 'modelo', 'descripcion', 'year', 'precio',  'telefonoContacto', 'emailContacto', 'imagen']



class  HeladerasForm(forms.ModelForm):

    class Meta:
        model = Heladera
        fields = ['usuario', 'titulo', 'marca', 'modelo', 'descripcion', 'year', 'precio',  'telefonoContacto', 'emailContacto', 'imagen']


class  LavarropaForm(forms.ModelForm):

    class Meta:
        model = Lavarropa
        fields = ['usuario', 'titulo', 'marca', 'modelo', 'descripcion', 'year', 'precio',  'telefonoContacto', 'emailContacto', 'imagen']
