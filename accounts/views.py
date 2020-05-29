from django.shortcuts import render

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import UpdateView,CreateView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm,CustomUserChangeForm
from members.models import Leader
from core.models import Celula
from .models import CustomUser
'''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+                           Views de Usuarios
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''


#redireciona dependendo do tipo de usuario
def login_success(request):
    if request.user.is_superuser:
        # user is an admin redirect to dashboard
    #messages.success(request,"Bem Vindo ao Sistema!!")
        return redirect('dashboard')
    else:
        usuario = request.user.pk
        leader   = Leader.objects.filter(user=usuario)
        celula  = Celula.objects.filter(leader__in=leader)
        if celula.exists():
            return redirect('/celula/sobre/'+str(int(celula[0].id)))
        else:
            return redirect('dashboard')

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class UserUpdateView(UpdateView):
    model = CustomUser
    template_name = "user/update.html"
    form_class = CustomUserChangeForm
    success_url = '/leaders'
    success_message = 'Dados Atualizos Com Sucesso!!!!'

    def get_object(self, queryset=None):
        return self.request.user