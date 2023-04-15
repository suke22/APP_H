from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Pedido
from .forms import PedidoForm, EditarForm
import datetime
from subir_datos.models import Dato
import csv
import xlwt


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
        pedido = get_object_or_404(Dato,direccion=direccion_new, dia_cita__date=datetime.date.today())
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


def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename= pedidos' + str(datetime.datetime.now())+ '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Datos')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['CITA', 'CÓDIGO POSTAL', 'DIRECCIÓN', 'NHC', 'MÓVIL', 'AGENDA', 'ESTADO', 'DNI', 'INCIDENCIAS']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Dato.objects.filter(dia_cita__date=datetime.date.today()).values_list('dia_cita', 'cp', 'direccion', 'nhc', 'movil', 'agenda', 'estado', 'DNI', 'incidencias')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response