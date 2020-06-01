from django import forms
from members.models import Leader,Discipulo


class LeaderForm(forms.ModelForm):
    class Meta:
        model = Leader
        exclude = ['user','slug']
        fields = '__all__'
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth': forms.DateInput(attrs={'class': 'form-control datetimepicker'}),
            'sex': forms.Select(attrs={'class':'selectpicker','data-style':'select-with-transition','data-size':7}),
            'ladder': forms.Select(attrs={'class':'selectpicker','data-style':'select-with-transition','data-size':7}),
            'lider_de_rede': forms.Select(attrs={'class':'selectpicker','data-style':'select-with-transition','data-size':7}),
            'telephone':forms.TextInput(attrs={'class':'form-control'}),
            'schooling':forms.Select(attrs={'class':'selectpicker','data-style':'select-with-transition','data-size':7}),
            'conversion_date':forms.DateInput(attrs={'class':'form-control datetimepicker'}),
            'date_batismo':forms.DateInput(attrs={'class':'form-control datetimepicker'}),
            'meeting_date':forms.DateInput(attrs={'class':'form-control datetimepicker'}),
            'cep':forms.TextInput(attrs={'class':'form-control'}),
            'street':forms.TextInput(attrs={'class':'form-control'}),
            'neighborhood':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'number':forms.TextInput(attrs={'class':'form-control'}),
            'facebook':forms.TextInput(attrs={'class':'form-control'}),
            'complement':forms.TextInput(attrs={'class':'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'uf': forms.Select(attrs={'class':'selectpicker',
                'data-style':'select-with-transition','data-size':7,'data-live-search':'true'}),
            'ministry': forms.Select(attrs={'class':'selectpicker',
                'data-style':'select-with-transition','data-size':7,'data-live-search':'true'}),
            'profession': forms.TextInput(attrs={'class': 'form-control'}),
        }


class DiscipuloForm(forms.ModelForm):
    class Meta:
        model = Discipulo
        fields = '__all__'
        exclude = ['slug']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required':'true'}),
            'sex': forms.Select(attrs={'class':'selectpicker',
                'data-style':'select-with-transition','data-size':7,'data-live-search':'true','title':'Escolha a cidade','required':'true'}),
            'birth': forms.DateInput(attrs={'class': 'form-control datetimepicker','required':'true'}),
            'leader': forms.Select(attrs={'class':'selectpicker', 
                'data-style':'select-with-transition','data-size':7,'data-live-search':'true','required':'true'}),
            'cell': forms.Select(attrs={'class':'selectpicker',
                'data-style':'select-with-transition','data-size':7,'data-live-search':'true','required':'true'}),
            #'lider': forms.Select(attrs={'class':'selectpicker','data-style':'select-with-transition','data-size':7}),
            'ladder': forms.Select(attrs={'class':'selectpicker',
                'data-style':'select-with-transition','data-size':7,'title':'Escolha o Nível'}),
            'conversion_date':forms.DateInput(attrs={'class':'form-control datetimepicker','required':'true'}),
            'profession':forms.TextInput(attrs={'class':'form-control datetimepicker'}),
            'consolidator':forms.TextInput(attrs={'class':'form-control datetimepicker'}),
            'date_batismo':forms.DateInput(attrs={'class':'form-control datetimepicker'}),
            'meeting_date':forms.DateInput(attrs={'class':'form-control datetimepicker'}),
            'telephone':forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook':forms.TextInput(attrs={'class':'form-control'}),
            'schooling':forms.Select(attrs={'class':'selectpicker','data-style':'select-with-transition','data-size':7}),
            'cep': forms.TextInput(attrs={'class': 'form-control','required':'true'}),
            'uf': forms.Select(attrs={'class':'selectpicker',
                'data-style':'select-with-transition','data-size':7,'data-live-search':'true','required':'true'}),            
            'city':forms.TextInput(attrs={'class':'form-control','required':'true'}),
            'neighborhood':forms.TextInput(attrs={'class':'form-control','required':'true'}),
            'street':forms.TextInput(attrs={'class':'form-control'}),
            'number':forms.TextInput(attrs={'class':'form-control'}),
        }
