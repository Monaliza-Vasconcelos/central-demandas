from django.urls import path
from . import views
from .views import lista_demandas, nova_demanda

urlpatterns = [
    path('', lista_demandas, name='lista_demandas'),
    path('nova/', nova_demanda, name='nova_demanda'),
]