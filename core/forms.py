from django import forms
from core.models import Celula
from core.choices import SEXO_CHOICES
from django.core.exceptions import ValidationError

class CelulaForm(forms.ModelForm):
    class Meta:
        model = Celula
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'leader': forms.Select(attrs={'class':'selectpicker','data-style':'select-with-transition','data-size':7, 'required':'true'}),
            'coleader': forms.TextInput(attrs={'class': 'form-control','required':'true'}),
            'cell_type': forms.Select(attrs={'class':'selectpicker','data-style':'select-with-transition','data-size':7,'required':'true'}),
            'created_at':forms.DateInput(attrs={'class':'form-control','required':'true'}),
            'meeting_day':forms.Select(attrs={'class':'selectpicker','data-style':'select-with-transition','data-size':7}),
            'uf': forms.Select(attrs={'class':'selectpicker',
                'data-style':'select-with-transition','data-size':7,'data-live-search':'true','required':'true'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control','required':'true'}),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'neighborhood': forms.TextInput(attrs={'class': 'form-control','required':'true'}),
        }
