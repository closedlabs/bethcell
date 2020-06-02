from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from core.choices import LIDER_CHOICES,SEXO_CHOICES
from members.models import Leader


class CustomUserCreationForm(UserCreationForm):
    ministry =  forms.CharField(widget=forms.Select(choices=LIDER_CHOICES,
        attrs={'class':'selectpicker','data-style':'select-with-transition','data-size':7}))
    leader      =  forms.ModelChoiceField(required = False,queryset=Leader.objects.all(),
        widget=forms.Select(attrs={'class':'selectpicker','data-style':'select-with-transition',
            'data-size':7,'data-live-search':'true'}))
    sex       =  forms.ChoiceField(choices=SEXO_CHOICES,widget=forms.Select(
        attrs={'class':'selectpicker','data-style':'select-with-transition','data-size':7}))
    
    class Meta:
        model  = get_user_model()
        fields = (
            'username', 'first_name', 'last_name', 'password1', 
            'password2', 'email','is_cell_leader',
            'is_generation_leader','is_teacher'
        )
        widgets = { 
            'username':forms.TextInput(attrs={'class':'form-control','required':'true'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','required':'true'}),   
            'last_name':forms.TextInput(attrs={'class':'form-control','required':'true'}),   
            'email':forms.EmailInput(attrs={'class':'form-control','required':'true'}),    
            'password1':forms.PasswordInput(attrs={'class':'form-control','required':'true'}),    
            'password2':forms.PasswordInput(attrs={'class':'form-control','required':'true'}),    
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control',})  
        self.fields['leader'].queryset = Leader.objects.filter(ministry='LG')


class CustomUserChangeForm(UserChangeForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)
  
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control',})  

    class Meta:
        model = get_user_model()
        fields = ('email', 'password','username')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
   

