from django import forms
from .models import servicos

class new_service(forms.ModelForm):
    class Meta:
        model = servicos
        fields = '__all__'

        widgets = {
                'valor':forms.NumberInput(attrs={'min':'0', 'value': '0.00'}),
            }