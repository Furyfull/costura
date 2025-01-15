from django.db import models 
from servicos.models import servicos
from cliente.models import Cliente
from costureiras.models import Costureira
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


STATUS=[
    (0, 'Não Iniciado'),
    (1, 'Em Andamento'),
    (2, 'Concluido'),
    (3, 'Entregue'),]

# Create your models here.
class Ordem(models.Model):
    cliente = models.ForeignKey(Cliente, related_name='ordens', on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateField(verbose_name='Data de entrega')
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"Ordem de {self.cliente} - {self.data_pedido}"
    
    def total(self):
        return sum(item.preco_total for item in self.itens.all())

    def get_delete_order(self):
        return reverse('ordens:delete_order', kwargs={'id': self.id})
    
class OrdemItem(models.Model):
    ordem = models.ForeignKey(Ordem, related_name='itens', on_delete=models.CASCADE)
    servico = models.ForeignKey(servicos, on_delete=models.CASCADE)
    costureira = models.ForeignKey(Costureira, on_delete=models.CASCADE)
    comissao = models.PositiveIntegerField(
        default=5,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ])
    quantidade = models.PositiveIntegerField()
    descricao = models.TextField(blank=True, null=True)  # Comentário opcional
    valor_unit = models.DecimalField(max_digits=10, decimal_places=2,
                                     blank=True, null=True, 
                                     validators=[MinValueValidator(0)])
    preco_total = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self):
        return f"{self.quantidade} x {self.servico.nome}"
    
    def get_delete_item(self):
        return reverse('ordens:delete_order_item', kwargs={'id': self.id})
    
    # Se o preco_total não foi preenchido manualmente, calcula automaticamente
    def save(self, *args, **kwargs):
        if not self.preco_total:
            self.preco_total = self.quantidade * self.valor_unit
        super().save(*args, **kwargs)