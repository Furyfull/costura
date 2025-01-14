from django.urls import path
from . import views

app_name='costureiras'

urlpatterns=[
        path('', views.costureiras, name= 'main'),
        path('cadastro_nova_costureira/', views.cadastro_costureira, name= 'cadastro'),
        path('trabalhos/<int:id>/<str:nome>/', views.trabalhos, name= 'trabalhos'),
        path('relatorio/<int:ordem_id>/<int:costureira_id>/', views.relatorio_pdf, name='relatorio'),
        path('relatorio/nao-concluido/<int:costureira_id>/', views.relatorio_nconc_pdf, name='relatorio-nc'),
]