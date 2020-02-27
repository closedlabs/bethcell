from django import forms
from core.models import Celula
from core.choices import SEXO_CHOICES

class CelulaForm(forms.ModelForm):
    class Meta:
        model = Celula
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'lider': forms.Select(attrs={'class':'selectpicker','data-style':'select-with-transition','data-size':7}),
            'colider': forms.TextInput(attrs={'class': 'form-control'}),
            'celula_de': forms.Select(attrs={'class':'selectpicker','data-style':'select-with-transition','data-size':7}),
            'criado_em':forms.DateInput(attrs={'class':'form-control datetimepicker'}),
            'dia_reuniao':forms.Select(attrs={'class':'selectpicker','data-style':'select-with-transition','data-size':7}),
            'uf': forms.Select(attrs={'class':'selectpicker',
                'data-style':'select-with-transition','data-size':7,'data-live-search':'true'}),
            'rua': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),

        }
