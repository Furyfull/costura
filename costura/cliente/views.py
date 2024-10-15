from django.shortcuts import render,redirect,get_object_or_404
from . import forms,models
from ordens.models import Ordem

# Create your views here.
def clientes(request):
    clients = models.Cliente.objects.all()
    return render(request, 'cliente/clientes.html', {'clientes': clients})

def cadastro_cliente(request):
    if request.method == 'POST':
        form = forms.CadastroCliente(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ordens:new_order')
    else:
        form = forms.CadastroCliente()
    return render(request, 'cliente/cadastro_cliente.html', {'form': form})

def ordens_cliente(request, id):
    cliente = get_object_or_404(models.Cliente, pk=id)
    return render(request, 'cliente/ordens_cliente.html',{
        'cliente':cliente,
    })

def vis_ordem_cliente(request, id):
    ordem = get_object_or_404(Ordem, pk=id)
    objs = ordem.itens.all()
    return render(request, 'cliente/vis_ordem_cliente.html', {'itens':objs, 'ordem':ordem})