from django.shortcuts import render,redirect,redirect,get_object_or_404
from . import forms
from . import models
from django.contrib import messages

# Create your views here.
def services(request):
    #Le servicos cadastrados
    servicos = models.servicos.objects.all()
    #Para cadastrar novos servicos
    if request.method == 'POST':
        form = forms.new_service(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Serviço Cadastrado !!!")
            return redirect('servicos:servicos')
    else:
        form = forms.new_service()
    return render(request, 'servicos/services.html', {'form': form, 'servicos':servicos})


def update_services(request, id):
    
    post=get_object_or_404(models.servicos, pk=id)
    form = forms.new_service(instance=post)

    if request.method == 'POST':
        form = forms.new_service(request.POST, instance=post)
        if form.is_valid():
            post.save()
            return redirect('servicos:servicos')

    return render(request, 'servicos/alterar.html', {'form': form,'post':post})

