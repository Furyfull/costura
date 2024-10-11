from django.db import models
from django.core.validators import MinValueValidator
from servicos.models import servicos
from decimal import Decimal

COSTUREIRA={
    'Maria':'MARIA',
    'Julia':'JULIA',
    'Carlinha':'CARLINHA',
}


# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Ordem(models.Model):
    # cliente = models.ForeignKey(Cliente, related_name='ordens', on_delete=models.CASCADE)
    cliente = models.CharField(max_length=100)
    data_pedido = models.DateTimeField(auto_now_add=True)
    # data_entrega = models.DateTimeField(auto_now_add=False)

    def total(self):
        return sum(item.quantidade * item.servico.valor for item in self.itens.all())

    def __str__(self):
        return f"Ordem de {self.cliente} - {self.data_pedido}"
    
class OrdemItem(models.Model):
    ordem = models.ForeignKey(Ordem, related_name='itens', on_delete=models.CASCADE)
    servico = models.ForeignKey(servicos, on_delete=models.CASCADE)
    costureira = models.CharField(max_length=10, choices=COSTUREIRA)
    quantidade = models.PositiveIntegerField()
    descricao = models.TextField(blank=True, null=True)  # Comentário opcional

    def __str__(self):
        return f"{self.quantidade} x {self.servico.nome}"
    