from django.shortcuts import render,get_object_or_404,HttpResponse
from ordens.models import Ordem
import subprocess
import json


def dashboard(request):
    ordens = Ordem.objects.all()

    # Captura os parâmetros de data do formulário (se eles existirem)
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        # Se ambos os campos de data foram preenchidos, filtra pelo intervalo de datas
        ordens = ordens.filter(data_entrega__range=[start_date, end_date])

    # api_path = "C:/xampp/htdocs/testphp/index.php"

    return render(request, 'dashboard.html',{'ordens':ordens,} )

