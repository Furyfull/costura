from django.shortcuts import render
from .forms import new_ordem

# Create your views here.
def new_order(request):
    form = new_ordem()
    return render(request, 'ordens/new_order.html', {'form': form})

def ordens(request):
    return render(request, 'ordens/orders.html')
