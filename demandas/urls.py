from django.urls import path
from . import views

urlpatterns  = [
    path('', views.lista_demandas, name='lista_demandas')
]