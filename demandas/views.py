from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Demanda, Categoria
from django.db.models import Q

# Create your views here.


@login_required
def lista_demandas(request):

    if request.user.groups.filter(name='Suporte').exists():
        demandas = Demanda.objects.all()
    else:
        demandas = Demanda.objects.filter(solicitante=request.user)

    busca = request.GET.get('busca')
    categoria = request.GET.get('categoria')
    status = request.GET.get('status')

    if busca:
        demandas = demandas.filter(
            Q(cliente__icontains=busca) |
            Q(telefone__icontains=busca)
        )
    if categoria:
        demandas = demandas.filter(categoria_id=categoria)

    if status:
        demandas = demandas.filter(status=status)

    categorias = Categoria.objects.all()

    return render(
        request,
        'demandas/listar_demandas.html',
        context={
            'demandas': demandas,
            'busca': busca,
            'categorias': categorias,
            'categoria_selecionada': categoria,
            'status_selecionado': status,
            'status_choices': Demanda.STATUS_CHOICES,
        }
    )