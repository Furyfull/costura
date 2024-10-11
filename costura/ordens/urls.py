from django.urls import path
from . import views

app_name='ordens'

urlpatterns = [
    path('', views.ordens, name= 'ordens'),
    path('nova_ordem', views.new_order, name= 'new_order'),
    path('edit_ordem/<str:id>', views.edit_order, name= 'edit_order'),
]
