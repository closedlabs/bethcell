from django.shortcuts import render

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from core.forms import SignUpForm,LiderForm
from django.views.generic import UpdateView
from core.models import Lider,Celula
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

'''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+                           Views de Usuarios
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

def add_usuario(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.user.lider_de_rede = form.cleaned_data.get('lider')
            user.user.tipo = form.cleaned_data.get('tipo_lider')
            user.user.sexo = form.cleaned_data.get('sexo')
            user.save()
            messages.success(request, "Novo Lider Cadastrado Com Sucesso!")
            return redirect('lista_lideres')
    else:
        form = SignUpForm()
    return render(request, 'adicionar_usuario.html', {'form': form})


#redireciona dependendo do tipo de usuario
def login_success(request):
    if request.user.is_superuser:
        # user is an admin redirect to dashboard
    #messages.success(request,"Bem Vindo ao Sistema!!")
        return redirect('dashboard')
    else:
        usuario = request.user.pk
        lider   = Lider.objects.filter(user=usuario)
        celula  = Celula.objects.filter(lider__in=lider)
        if celula.exists():
            return redirect('/celula/sobre/'+str(int(celula[0].id)))
        

"""
def update_usuario(request,pk):
    lider = Lider.objects.get(pk=pk)
    lider_form = LiderForm(request.POST or None, instance=lider)
    if lider_form.is_valid():
        lider_form.save()
        #messages.success(request, ('Dados atualizados com Sucesso!'))
        return redirect('home')
    return render(request, 'update_lider.html', {
        'form': lider_form
    })
"""

class LiderUpdateView(SuccessMessageMixin,UpdateView):
    model = Lider
    template_name = "update_lider.html"
    form_class = LiderForm
    success_url = '/lideres'
    success_message = 'Dados Atualizos Com Sucesso!!!!'

