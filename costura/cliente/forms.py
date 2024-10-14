from django import forms
from . import models

class CadastroCliente(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = ['nome']
