from django import forms
from . import models

class CriaOrdem(forms.ModelForm):
    class Meta:
        model = models.Ordem
        fields = ['cliente']
        
        # widgets = {
        #     # 'data_pedido':forms.DateTimeInput(attrs={'type':'datetime-local'}),
        #     # 'data_entrega':forms.DateTimeInput(attrs={'type':'datetime-local'}),
        # }

class OrdemItemForm(forms.ModelForm):
    class Meta:
        model = models.OrdemItem
        fields = ['servico', 'quantidade','descricao','costureira']
        widgets = {
            'servico': forms.Select(),
            'descricao': forms.Textarea(attrs={'rows': 4, 'cols': 40, 'placeholder': 'Descrição opcional'}),
        }
        labels = {
            'servico': 'Serviço',
            'quantidade': 'Quantidade',
            'descricao': 'Descrição',
        }