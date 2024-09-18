from django.shortcuts import render,redirect
from .forms import new_service

# Create your views here.
def services(request):
    if request.method == 'POST':
        form = new_service(request.POST)
        if form.is_valid():
            novo = form.save(commit=False)
            novo.save()
            return redirect('servicos:servicos')
    else:
        form=new_service()
    return render(request, 'servicos/services.html', {'form': form})
