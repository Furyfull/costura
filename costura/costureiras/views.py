from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from . import forms,models
from ordens.models import OrdemItem
from costura.services import gerar_servicos_relatorio_pdf

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

def relatorio_pdf(request, ordem_id, costureira_id):
    ordem_itens = OrdemItem.objects.filter(ordem_id=ordem_id, costureira_id=costureira_id)
  
    pdf = gerar_servicos_relatorio_pdf(ordem_itens,filtro=False)

    # Configuração do response
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio_servicos.pdf"'

    return response

def relatorio_nconc_pdf(request, costureira_id):
    ordem_itens = OrdemItem.objects.filter(costureira_id=costureira_id)
  
    pdf = gerar_servicos_relatorio_pdf(ordem_itens,filtro=True)

    # Configuração do response
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio_servicos.pdf"'

    return response

