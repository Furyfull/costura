from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from . import forms,models
from ordens.models import OrdemItem

# Create your views here.
def costureiras(request):
    costureiras = models.Costureira.objects.all()
    return render(request, 'costureiras/costureiras.html', {'costureiras':costureiras})

def cadastro_costureira(request):
    if request.method == 'POST':
        form = forms.CadsCostureira(request.POST)
        if form.is_valid():
            form.save()
        return redirect('costureiras:main')
    else:
        form = forms.CadsCostureira()
    return render(request, 'costureiras/cadastro_cost.html', {'form':form})

def trabalhos(request,id,nome):
    costureira = get_object_or_404(models.Costureira, pk=id)
    itens = OrdemItem.objects.filter(costureira=costureira)
    return render(request, 'costureiras/trabalhos.html',{
        'servicos':itens,
        'costureira':costureira,
        })