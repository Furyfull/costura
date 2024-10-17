from django.shortcuts import render,get_object_or_404
from ordens.models import Ordem


def dashboard(request):
    ordens = Ordem.objects.all()
    return render(request, 'dashboard.html',{'ordens':ordens} )
