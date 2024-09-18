from django import forms
from .models import Ordem

class new_ordem(forms.ModelForm):
    class Meta:
        model = Ordem
        fields = '__all__'

        widgets = {
            'data_pedido':forms.DateTimeInput(attrs={'type':'datetime-local'}),
            'data_entrega':forms.DateTimeInput(attrs={'type':'datetime-local'}),
            'quantidade':forms.NumberInput(attrs={'min':'1','value':'1'}),
            'valor':forms.NumberInput(attrs={'min':'0', 'value': '0.00'}),
        }