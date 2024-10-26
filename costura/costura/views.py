from django.shortcuts import render,get_object_or_404
from ordens.models import Ordem


def dashboard(request):
    ordens = Ordem.objects.all()

    # Captura os parâmetros de data do formulário (se eles existirem)
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        # Se ambos os campos de data foram preenchidos, filtra pelo intervalo de datas
        ordens = ordens.filter(data_entrega__range=[start_date, end_date])

    return render(request, 'dashboard.html',{'ordens':ordens} )
