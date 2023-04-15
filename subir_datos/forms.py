from django import forms
from .models import Dato


class DatoForm(forms.Form):
    class Meta:
        model = Dato
        fields = '__all__'