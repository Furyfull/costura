from django import forms
from . import models


class CriaOrdem(forms.ModelForm):
    class Meta:
        model = models.Ordem
        fields = '__all__'
        
        widgets = {
            'data_entrega':forms.DateInput(format="%d/%m/%Y",attrs={'type': 'date'}),
        }

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