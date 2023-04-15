from django.urls import path
from . import views

urlpatterns = [
    path('subir_datos/', views.subir_datos, name='subir_datos'),
]