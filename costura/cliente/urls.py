from django.urls import path
from . import views

app_name='cliente'

urlpatterns = [
    path('', views.clientes, name= 'clientes'),
    path('cadastro_cliente', views.cadastro_cliente, name= 'cadastro_cliente'),
    path('ordens_cliente_<int:id>', views.ordens_cliente, name= 'ordens_cliente'),
]
