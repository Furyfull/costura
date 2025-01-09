from django.db import models

# Create your models here.
class Costureira(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    comissao = models.FloatField()

    def __str__(self) :
        return self.nome