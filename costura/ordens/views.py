from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from . import forms,models
from servicos.models import servicos
from cliente.models import Cliente
from django.contrib import messages


# Create your views here.
def ordens(request):
    orders= models.Ordem.objects.all()
    return render(request, 'ordens/orders.html',{'orders':orders})

#cria uma ordem para o cliente
def new_order(request):
    if request.method == 'POST':
        form = forms.CriaOrdem(request.POST)
        if form.is_valid():
            ordem = form.save(commit=False)
            ordem.save()
        return redirect('ordens:edit_order', id=ordem.id)
    else:
        form = forms.CriaOrdem()
    return render(request, 'ordens/new_order.html', {'form': form})

def edit_order(request, id):
    order = get_object_or_404(models.Ordem, pk=id)
    services = servicos.objects.all()
    client = order.cliente
    #adicionando 1 item/servico a ordem de cada vez
    if request.method == "POST":
        form = forms.OrdemItemForm(request.POST)
        if form.is_valid():
            ordem_item = form.save(commit=False)
            ordem_item.ordem = order
            # Isso é oq vai ser salvo no db
            ordem_item.save()
            messages.success(request, "Serviço Adicionado !!!")
            return HttpResponseRedirect(request.path)
    else:
        form = forms.OrdemItemForm()

    # usa d def total() criada no models
    total = order.total()
    # comando .itens vem do models (related_name='itens')
    ordem_itens = order.itens.all()
    # notar q aqui é "ordem_itens" e no if é "ordem_item"
    # fazendo calculos
    ordem_itens_com_totais = []
    for item in ordem_itens:
        preco_total = item.quantidade * item.servico.valor
        # Isso é oq vai ser mostrado no html
        ordem_itens_com_totais.append({
            'id': item.id,
            'nome': item.servico.nome,
            'preco': item.servico.valor,
            'preco_total': preco_total,
            'costureira': item.costureira,
            'quantidade': item.quantidade,
            'descricao' : item.descricao,
            'excluir':item.get_delete_item,
        })

    
    return render(request, 'ordens/edit_order.html', {
        'form': form,
        'cliente':client,
        'total':total,
        'ordem_itens': ordem_itens_com_totais,
        'servicos':services,

        })

def delete_order_item(request, id):
    item = get_object_or_404(models.OrdemItem, pk=id)
    item.delete()
    # Redireciona de volta à página da ordem
    return redirect('ordens:edit_order', id=item.ordem.id)  

def delete_order(request, id):
    ordem = get_object_or_404(models.Ordem, pk=id)
    ordem.delete()
    return redirect('ordens:ordens')

