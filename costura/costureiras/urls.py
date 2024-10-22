from django.urls import path
from . import views

app_name='costureiras'

urlpatterns=[
        path('', views.costureiras, name= 'main'),
        path('cadastro_nova_costureira/', views.cadastro_costureira, name= 'cadastro'),
        path('trabalhos/<int:id>/<str:nome>/', views.trabalhos, name= 'trabalhos'),
]