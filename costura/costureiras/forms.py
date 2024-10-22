from django import forms
from . import models

class CadsCostureira(forms.ModelForm):
    class Meta:
        model = models.Costureira
        fields = '__all__'
        