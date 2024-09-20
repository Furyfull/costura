from django import forms
from . import models

class new_service(forms.ModelForm):
    class Meta:
        model = models.servicos
        fields = ['nome','valor']

        widgets = {
                'valor':forms.NumberInput(attrs={'min':'0', 'value': '0.00'}),
            }
        