from django.db import models
from django.core.validators import MinValueValidator
from servicos.models import servicos



COSTUREIRA={
    'Maria':'MARIA',
    'Julia':'JULIA',
    'Carlinha':'CARLINHA',
}

# Create your models here.
class Ordem(models.Model):
    cliente = models.CharField(max_length=100)
    servico = models.ForeignKey(servicos, on_delete=models.CASCADE)
    costureira = models.CharField(max_length=10, choices=COSTUREIRA)
    descricao = models.TextField(max_length= 160)
    data_pedido = models.DateTimeField(auto_now_add=False)
    data_entrega = models.DateTimeField(auto_now_add=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField (validators=[MinValueValidator (1)])
    valor_total = models.DecimalField(max_digits=11, decimal_places=2)
    
    

    def __str__(self) -> str:
        return self.cliente