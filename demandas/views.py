from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Demanda

# Create your views here.


@login_required
def lista_demandas(request):
    print(request)
    print(request.user)
    print(type(request.user))
    if request.user.groups.filter(name='Suporte').exists():
        demandas = Demanda.objects.all()
    else:
        demandas = Demanda.objects.filter(solicitante=request.user)
    

    return render(request, 'demandas/listar_demandas.html', context={'demandas': demandas})
