from django.shortcuts import render,redirect
from . import forms,models
from servicos.models import servicos

# Create your views here.
def ordens(request):
    orders= models.Ordem.objects.all()
    return render(request, 'ordens/orders.html',{'orders':orders})

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
    form = forms.OrdemItemForm()
    return render(request, 'ordens/edit_order.html', {'form': form})