from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import TemplateView,DetailView,CreateView,UpdateView,DeleteView
from members.models import Leader,Discipulo
from django.contrib import messages
from members.forms import DiscipuloForm,LeaderForm
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

def leaders(request):
    usuario = request.user.pk
    if request.user.is_superuser:
        lideres = Leader.objects.all().exclude(user__username='admin')
    elif Leader.objects.filter(user=usuario,ministry='LG').exists():
        leader  = Leader.objects.get(user=usuario,ministry='LG')
        lideres = Leader.objects.filter(lider_de_rede=leader)
    elif Leader.objects.filter(user=usuario,ministry='LC').exists():
        leader  = Leader.objects.get(user=usuario,ministry='LC')
        lideres = Leader.objects.filter(user=usuario)

    paginator = Paginator(lideres, 12) 
    page_number = request.GET.get('page')
   
    if request.GET:
        name          = request.GET.get('name')
        if name:
            lideres   = Leader.objects.filter(name__icontains=name,) 
            paginator = Paginator(lideres, 12) 
        
    page_obj = paginator.get_page(page_number)
    context = {
        'leaders':page_obj
    }
    return render(request,'leaders/leaders.html',context)


# def leaders(request):
#     if request.user.is_superuser:
#         lideres = Leader.objects.all().exclude(user__username='admin')
#     else:
#         usuario = request.user.pk
#         leader = Leader.objects.get(user=usuario,ministry='LG')
#         lideres = Leader.objects.filter(lider_de_rede=leader)
#         print(lideres, "Esse é um Lider")
#     context = {
#         'lideres':lideres
#     }
#     return render(request,'leaders/leaders.html',context)

def add_leader(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print(form.data)
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
    return render(request, 'leaders/add_leader.html', {'form': form},locals())

class LeaderDetailView(DetailView):
    model = Leader
    template_name = "leaders/leader_detail.html"

# class LeaderUpdateView(SuccessMessageMixin,UpdateView):
#     model = Leader
#     template_name = "leaders/leader_update.html"
#     form_class = LeaderForm
#     success_url = '/leaders'
#     success_message = 'Dados Atualizos Com Sucesso!!!!'

class LeaderDeleteView(DeleteView):
    model         = Leader
    template_name = "leaders/leader_delete.html"
    success_url   = '/leaders'
    success_message = 'Excluido com sucesso'

    
    def delete(self, request, *args, **kwargs):
       messages.success(self.request, self.success_message)
       return super(LeaderDeleteView, self).delete(request, *args, **kwargs)


def leader_update(request,slug):
    leader = Leader.objects.get(slug=slug)
    lider_form = LeaderForm(request.POST or None, instance=leader)
    if lider_form.is_valid():
        lider_form.save()
        #messages.success(request, ('Dados atualizados com Sucesso!'))
        return redirect('leaders')
    return render(request, 'leaders/leader_update.html', {
        'profile_form': lider_form
    })


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
    usuario    = request.user.pk
    if request.user.is_superuser:
        discipulos = Discipulo.objects.all()
    elif Leader.objects.filter(user=usuario,ministry='LG').exists():
        leader      = Leader.objects.get(user=usuario,ministry='LG')
        discipulos  = Discipulo.objects.filter(leader__lider_de_rede=leader)
    elif Leader.objects.filter(user=usuario,ministry='LC').exists():
        leader      = Leader.objects.get(user=usuario,ministry='LC')
        discipulos  = Discipulo.objects.filter(leader=leader)

    paginator = Paginator(discipulos, 12) 
    page_number = request.GET.get('page')
   
    if request.GET:
        name          = request.GET.get('name')
        if name:
            discipulos   = Discipulo.objects.filter(name__icontains=name) 
            paginator = Paginator(discipulos, 12) 

        
    page_obj = paginator.get_page(page_number)
    context = {
        'discipulos':page_obj
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
        discipulo.exited = request.POST.get('motivo')
        discipulo.save()
        discipulo.delete()
        messages.success(request, "Excluido Com Sucesso!")
        return redirect('discipulos')
    return render(request,'disciples/delete.html',{'form':form})
    