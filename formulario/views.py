from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Pedido
from .forms import PedidoForm, EditarForm
import datetime
from subir_datos.models import Dato


# Create your views here.
def index(request):
    tittle = 'Django Course!!'
    return render(request, 'index.html', {'tittle': tittle})

def formulario(request):
    form = Dato.object.all()
    return render(request, 'formulario.html',{'Pedido':form})

def listar_direcciones(request):
    if request.method == 'POST':
        direccion_new = request.POST.get('direccion',False)
        pedido = get_object_or_404(Dato,direccion=direccion_new)
        form = PedidoForm(request.POST, instance=pedido)
        print(request.POST)

        if form.is_valid():
            form.save()
            print(request.POST)
            return HttpResponseRedirect('/')
    else:
        form = PedidoForm
    return render(request, "formulario.html", {'form':form})

def tabla_pedidos(request):
    results =Dato.objects.filter(dia_cita__date=datetime.date.today())
    return render(request, "ver_pedidos.html",{"todos_pedidos":results})

def editar_pedido(request,id):
    if request.method == 'POST':
        pedido = get_object_or_404(Dato,pk=id)
        edit_form = EditarForm(request.POST, instance=pedido)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect('/')
    else:
        edit_form = EditarForm
    return render(request, "editar_pedidos.html", {'form':edit_form})