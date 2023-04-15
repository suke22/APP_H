from django import forms
from .models import Pedido
from subir_datos.models import Dato

from django import forms
from django.forms import ModelForm
from .models import Pedido
import datetime
from django.forms import ModelChoiceField

ESTADOS =(
    ("Blank", "---------"),
    ("Entregado", "Entregado"),
    ("No entregado: Direccion erronea", "No entregado: Direccion erronea"),
    ("No entregado: No hay nadie en casa", "No entregado: No hay nadie en casa"),

)

class PedidoForm(ModelForm):
    direccion = forms.ModelChoiceField (queryset= Dato.objects.filter(estado='Sin revisar',dia_cita__date=datetime.date.today()).values_list('direccion', flat=True), to_field_name='direccion',widget=forms.Select(attrs={'class':'form-control'}))
    estado = forms.ChoiceField(choices=ESTADOS, widget = forms.Select(attrs={'class':'form-control'}) )
    class Meta:
        model = Dato
        fields = ('direccion' ,'estado', 'DNI', 'incidencias')
        labels = {'direccion':'Dirección', 'estado':'Estado', 'DNI':'DNI del receptor', 'incidencias':'Incidencias'}
        widgets = {
            'direccion': forms.Select(attrs={'class':'form-control'}),
            'estado': forms.Select(attrs={'class':'form-control'}),
            'DNI': forms.TextInput(attrs={'class':'form-control'}),
            'incidencias': forms.Textarea(attrs={'class':'form-control'}),
            
        }

class EditarForm(ModelForm):
    estado = forms.ChoiceField(choices=ESTADOS, widget = forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = Pedido
        fields = ('estado', 'DNI', 'incidencias')

        widgets = {
            
            'estado': forms.Select(attrs={'class':'form-control'}),
            'DNI': forms.TextInput(attrs={'class':'form-control'}),
            'incidencias': forms.Textarea(attrs={'class':'form-control'}),
            }   