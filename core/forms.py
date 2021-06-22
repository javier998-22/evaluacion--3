from django import forms
from django.forms import ModelForm
from .models import Libro



class LibroForm(forms.ModelForm):
    
    class Meta:
        model = Libro
        fields = ['ISBN','nombreLibro','autor','Descripcion','categoria']

