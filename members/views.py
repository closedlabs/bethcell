from django.shortcuts import render,redirect
from django.views.generic import TemplateView,DetailView,CreateView,UpdateView,DeleteView
from members.models import Leader,Discipulo
from django.contrib import messages
from members.forms import LeaderForm,DiscipuloForm
from accounts.forms import CustomUserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
'''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+                         VIEWS DE LIDERES DE CÈLULA
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

def lista_lider(request):
    query = Leader.objects.filter(tipo='PR')
    return render(request,'index.html',{'leader':query})

"""
def lista_filhos(request,pk):
    query = Lider.objects.filter(lider_de_rede=pk)
    return render(request,'filhos.html',{'filhos':query})
"""
def leaders(request):
    if request.user.is_superuser:
        lideres = Leader.objects.all()
    else:
        usuario = request.user.pk
        leader = Leader.objects.get(user=usuario,ministry='LG')
        lideres = Leader.objects.filter(lider_de_rede=leader)
        print(lideres, "Esse é um Lider")
    context = {
        'lideres':lideres
    }
    return render(request,'leaders/leaders.html',context)

def add_leader(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the leader instance created by the signal
            user.user.lider_de_rede = form.cleaned_data.get('leader')
            user.user.ministry = form.cleaned_data.get('ministry')
            user.user.sex = form.cleaned_data.get('sex')
            user.save()
            messages.success(request, "Novo Lider Cadastrado Com Sucesso!")
            return redirect('leaders')
    else:
        form = CustomUserCreationForm()
    return render(request, 'leaders/add_leader.html', {'form': form})

class LeaderDetailView(DetailView):
    model = Leader
    template_name = "leaders/leader_detail.html"

class LeaderUpdateView(SuccessMessageMixin,UpdateView):
    model = Leader
    template_name = "leaders/leader_update.html"
    form_class = LeaderForm
    success_url = '/leaders'
    success_message = 'Dados Atualizos Com Sucesso!!!!'

class LeaderDeleteView(DeleteView):
    model         = Leader
    template_name = "leaders/leader_delete.html"
    success_url   = '/leaders'


"""
def update_usuario(request,pk):
    leader = Lider.objects.get(pk=pk)
    lider_form = LeaderForm(request.POST or None, instance=leader)
    if lider_form.is_valid():
        lider_form.save()
        #messages.success(request, ('Dados atualizados com Sucesso!'))
        return redirect('home')
    return render(request, 'update_lider.html', {
        'form': lider_form
    })
"""

"""
def lider_delete(request,pk):
    leader = get_object_or_404(Lider,pk=pk)
    leader.delete()
    return redirect(request.META['HTTP_REFERER'])
"""
    
'''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+                          VIEWS DE DISCIPULOS 
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

def discipulos(request):
    if request.user.is_superuser:
        discipulos = Discipulo.objects.all()
    else:
        usuario    = request.user.pk
        leader      = Leader.objects.get(user=usuario,ministry='LG')
        discipulos = Discipulo.objects.filter(lider__lider_de_rede=leader)
    context = {
        'discipulos':discipulos
    }
    return render(request,'disciples/disciples.html',context)


class DiscipuloCreateView(SuccessMessageMixin,CreateView):
    model           = Discipulo
    form_class      = DiscipuloForm
    template_name   = "disciples/add.html"
    success_url     = '/discipulos'
    success_message = 'Discipulo Cadastrado Com Sucesso!!!!'


class DiscipuloUpdateView(SuccessMessageMixin,UpdateView):
    model           = Discipulo
    form_class      = DiscipuloForm
    template_name   = "disciples/add.html"
    success_url     = '/discipulos'
    success_message = 'Dados Atualizados Com Sucesso!!!!'


class DiscipuloDetailView(DetailView):
    model = Discipulo
    template_name = "disciples/detail.html"


def discipulo_delete(request,slug):
    discipulo = get_object_or_404(Discipulo,slug=slug)   
    form = DiscipuloForm(request.POST or None,instance=discipulo)
    if request.method == 'POST':
        discipulo.saiu = request.POST.get('motivo')
        discipulo.save()
        discipulo.delete()
        return redirect('discipulos')
    return render(request,'disciples/delete.html',{'form':form})
    