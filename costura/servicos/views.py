from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import new_service
from django.contrib import messages

# Create your views here.
def services(request):
    if request.method == 'POST':
        form = new_service(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Serviço Cadastrado !!!")
            return redirect('servicos:servicos')
    else:
        form = new_service()
    return render(request, 'servicos/services.html', {'form': form})

def resposta_views(request):
    return HttpResponse('salvo com sucesso')
