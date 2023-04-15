from django.shortcuts import render
from .forms import DatoForm
from tablib import Dataset
from .resources import DatoResource
from .models import Dato
from django.http import HttpResponse
from django.views.generic import ListView, FormView

# Create your views here.

def subir_datos(request):
    if request.method == 'POST':
        dato_resource = DatoResource()
        dataset = Dataset()
        new_dato = request.FILES['archivo']

        imported_data = dataset.load(new_dato.read())
        for data in imported_data:
            value = Dato(
                dia_cita = data[0],
                cp = data[1],
                direccion = data[2],
                nhc = data[3],
                movil = data[4],
                agenda = data[5],
                estado = data[6],
            )
            value.save()

    return render(request, 'subir_datos.html')



def export(request):
    dato_resource = DatoResource()
    dataset = dato_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response