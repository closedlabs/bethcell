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

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
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

def change_password_user(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Sua senha foi atualizada com sucesso!')
            return redirect('leaders')
        else:
            messages.error(request, 'por favor Corrija o erro abaixo.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request,  "user/update.html", {
        'form': form
    })

# class UserUpdateView(SuccessMessageMixin,UpdateView):
#     model = CustomUser
#     template_name = "user/update.html"
#     form_class = CustomUserChangeForm
#     success_url = 'update/'
#     success_message = 'Dados Atualizos Com Sucesso!!!!'

#     def get_object(self, queryset=None):
#         return self.request.user