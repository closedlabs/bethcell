from django import forms
from members.models import Lider,Discipulo


class LiderForm(forms.ModelForm):
    class Meta:
        model = Lider
        exclude = ['user','slug']
        fields = '__all__'
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'nascimento': forms.DateInput(attrs={'class': 'form-control datetimepicker'}),
            'sexo': forms.Select(attrs={'class':'selectpicker','data-style':'select-with-transition','data-size':7}),
            'tipo': forms.Select(attrs={'class':'selectpicker','data-style':'select-with-transition','data-size':7}),
            'lider_de_rede': forms.Select(attrs={'class':'selectpicker','data-style':'select-with-transition','data-size':7}),
            'telefone':forms.TextInput(attrs={'class':'form-control'}),
            'escolaridade':forms.Select(attrs={'class':'selectpicker','data-style':'select-with-transition','data-size':7}),
            'endereco': forms.TextInput(attrs={'class':'form-control'}),
            'data_conversao':forms.TextInput(attrs={'class':'form-control datetimepicker'}),
            'data_batismo':forms.TextInput(attrs={'class':'form-control datetimepicker'}),
            'data_encontro':forms.TextInput(attrs={'class':'form-control datetimepicker'}),
            'telefone':forms.TextInput(attrs={'class':'form-control'}),
            'cep':forms.TextInput(attrs={'class':'form-control'}),
            'rua':forms.TextInput(attrs={'class':'form-control'}),
            'bairro':forms.TextInput(attrs={'class':'form-control'}),
            'cidade':forms.TextInput(attrs={'class':'form-control'}),
            'numero':forms.TextInput(attrs={'class':'form-control'}),
            'facebook':forms.TextInput(attrs={'class':'form-control'}),
            'uf': forms.Select(attrs={'class':'selectpicker',
                'data-style':'select-with-transition','data-size':7,'data-live-search':'true'}),
            'profissao': forms.TextInput(attrs={'class': 'form-control'}),
        }


class DiscipuloForm(forms.ModelForm):
    class Meta:
        model = Discipulo
        fields = '__all__'
        exclude = ['slug']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class':'selectpicker',
                'data-style':'select-with-transition','data-size':7,'data-live-search':'true','title':'Escolha a cidade'}),
            'nascimento': forms.DateInput(attrs={'class': 'form-control datetimepicker'}),
            'lider': forms.Select(attrs={'class':'selectpicker', 
                'data-style':'select-with-transition','data-size':7,'data-live-search':'true'}),
            'celula': forms.Select(attrs={'class':'selectpicker',
                'data-style':'select-with-transition','data-size':7,'data-live-search':'true'}),
            #'lider': forms.Select(attrs={'class':'selectpicker','data-style':'select-with-transition','data-size':7}),
            'tipo': forms.Select(attrs={'class':'selectpicker',
                'data-style':'select-with-transition','data-size':7,'title':'Escolha a cidade'}),
            'data_conversao':forms.TextInput(attrs={'class':'form-control datetimepicker'}),
            'profissao':forms.TextInput(attrs={'class':'form-control datetimepicker'}),
            'data_batismo':forms.TextInput(attrs={'class':'form-control datetimepicker'}),
            'data_encontro':forms.TextInput(attrs={'class':'form-control datetimepicker'}),
            'telefone':forms.TextInput(attrs={'class':'form-control'}),
            'telefone':forms.TextInput(attrs={'class':'form-control'}),
            'escolaridade':forms.Select(attrs={'class':'selectpicker','data-style':'select-with-transition','data-size':7}),
            'uf': forms.Select(attrs={'class':'selectpicker',
                'data-style':'select-with-transition','data-size':7,'data-live-search':'true'}),
        }
