from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import new_service,update_service
from . import models
from django.contrib import messages

# Create your views here.
def services(request):
    #Le servicos cadastrados
    servicos = models.servicos.objects.all()
    #Para cadastrar novos servicos
    if request.method == 'POST':
        form = new_service(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Serviço Cadastrado !!!")
            return redirect('servicos:servicos')
    else:
        form = new_service()
    return render(request, 'servicos/services.html', {'form': form, 'servicos':servicos})

# def resposta_views(request):
#     return HttpResponse('salvo com sucesso')

def update_services(request, pk):
    

    obj_id=models.servicos.objects.get(id=32)
    form = update_service(instance=obj_id)
    if request.method == 'POST':
        
        form = update_service(request.POST, instance=obj_id)
        if form.is_valid():
            # models.servicos.filter(id=29).update(nome='teste')
            # form.save(update_fields=True)
            return redirect('servicos:servicos')

    return render(request, 'servicos/alterar.html', {'form': form})

