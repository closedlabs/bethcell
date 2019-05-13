from django import forms
from django.contrib.auth.models import User
from core.models import *
from core.choices import SEXO_CHOICES
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from  core.models import Lider

LIDER_CHOICES   = (
    ('LC','Lider de Célula'),
    ('LG','Lider de Geração'),
    ('PR','Pastores'),

)
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

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


class SignUpForm(UserCreationForm):
    tipo_lider =  forms.CharField(widget=forms.Select(choices=LIDER_CHOICES,attrs={'class':'selectpicker','data-style':'select-with-transition','data-size':7}))
    lider      =  forms.ModelChoiceField(required = False,queryset=Lider.objects.all(),widget=forms.Select(
        attrs={'class':'selectpicker','data-style':'select-with-transition','data-size':7,'data-live-search':'true'}))
    sexo       =  forms.ChoiceField(choices=SEXO_CHOICES,widget=forms.Select(
        attrs={'class':'selectpicker','data-style':'select-with-transition','data-size':7}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','tipo_lider' )
        widgets = { 
            'username':forms.TextInput(attrs={'class':'form-control','required':'true'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','required':'true'}),   
            'last_name':forms.TextInput(attrs={'class':'form-control','required':'true'}),   
            'email':forms.EmailInput(attrs={'class':'form-control','required':'true'}),    
            'password1':forms.PasswordInput(attrs={'class':'form-control','required':'true'}),    
            'password2':forms.PasswordInput(attrs={'class':'form-control','required':'true'}),    
            }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control',})    

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
