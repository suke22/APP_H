from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formulario/', views.listar_direcciones, name='listar_direcciones'),
    path('pedidos/', views.tabla_pedidos, name='tabla_pedidos'),
    path('pedidos/editar_pedidos/<int:id>', views.editar_pedido, name='editar_pedidos')
    ]

