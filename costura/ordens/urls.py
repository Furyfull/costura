from django.urls import path
from . import views

app_name='ordens'

urlpatterns = [
    path('', views.ordens, name= 'ordens'),
    path('nova_ordem', views.new_order, name= 'new_order'),
    path('edit_ordem_<str:id>', views.edit_order, name= 'edit_order'),
    # Excluidores
    path('excluir-item_<int:id>/', views.delete_order_item, name='delete_order_item'),
    path('excluir-ordem_<int:id>/', views.delete_order, name='delete_order'),
    # Editar modal
    path('update_status/<int:id>/', views.update_status, name='update_status'),
]
