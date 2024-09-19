from django.urls import path
from . import views

app_name= 'servicos'

urlpatterns = [
    path('', views.services, name='servicos'),
    path('alterar/<str:pk>/', views.update_services, name='alterar'),
]
 