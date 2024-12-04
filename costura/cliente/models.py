from django.db import models
from django_cpf_cnpj.fields import CPFField


# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = CPFField(masked=True,blank=True, null=True, verbose_name='CPF')
    endereco = models.CharField(max_length=100,blank=True, null=True)
    num =  models.IntegerField(blank=True, null=True)
    cidade = models.CharField(max_length=20,blank=True, null=True)
    estado = models.CharField(max_length=30,blank=True, null=True)
    telefone = models.CharField(max_length=15,blank=True, null=True)

    def __str__(self):
        return self.nome
