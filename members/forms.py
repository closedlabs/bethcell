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
            'conversion_date':forms.TextInput(attrs={'class':'form-control datetimepicker'}),
            'date_batismo':forms.TextInput(attrs={'class':'form-control datetimepicker'}),
            'meeting_date':forms.TextInput(attrs={'class':'form-control datetimepicker'}),
            'cep':forms.TextInput(attrs={'class':'form-control'}),
            'street':forms.TextInput(attrs={'class':'form-control'}),
            'neighborhood':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'number':forms.TextInput(attrs={'class':'form-control'}),
            'facebook':forms.TextInput(attrs={'class':'form-control'}),
            'complement':forms.TextInput(attrs={'class':'form-control'}),
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
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class':'selectpicker',
                'data-style':'select-with-transition','data-size':7,'data-live-search':'true','title':'Escolha a cidade'}),
            'birth': forms.DateInput(attrs={'class': 'form-control datetimepicker'}),
            'leader': forms.Select(attrs={'class':'selectpicker', 
                'data-style':'select-with-transition','data-size':7,'data-live-search':'true'}),
            'cell': forms.Select(attrs={'class':'selectpicker',
                'data-style':'select-with-transition','data-size':7,'data-live-search':'true'}),
            #'lider': forms.Select(attrs={'class':'selectpicker','data-style':'select-with-transition','data-size':7}),
            'ladder': forms.Select(attrs={'class':'selectpicker',
                'data-style':'select-with-transition','data-size':7,'title':'Escolha a cidade'}),
            'conversion_date':forms.TextInput(attrs={'class':'form-control datetimepicker'}),
            'profession':forms.TextInput(attrs={'class':'form-control datetimepicker'}),
            'date_batismo':forms.TextInput(attrs={'class':'form-control datetimepicker'}),
            'meeting_date':forms.TextInput(attrs={'class':'form-control datetimepicker'}),
            'telephone':forms.TextInput(attrs={'class':'form-control'}),
            'schooling':forms.Select(attrs={'class':'selectpicker','data-style':'select-with-transition','data-size':7}),
            'uf': forms.Select(attrs={'class':'selectpicker',
                'data-style':'select-with-transition','data-size':7,'data-live-search':'true'}),
        }
