from django.shortcuts import render,redirect,get_object_or_404
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

"""
def lista_filhos(request,pk):
    query = Lider.objects.filter(lider_de_rede=pk)
    return render(request,'filhos.html',{'filhos':query})
"""

# def recibos(request):
#     #variavel para distiguir atendimentos por profissional
#     prof = ""
#     #variaveis para saber o tipo de usuario logado no template
#     pf = Profissional.prof_objects.filter(user=request.user,tipo=2)
#     if pf.exists():
#         prof = Profissional.prof_objects.get(user=request.user,tipo=2)
#     else:
#         pass
    
#     if request.GET.get('date_ranger'):
#         #se buscas
#         date_range          = request.GET.get('date_ranger')
#         start_date_string   = datetime.strptime(date_range.split(' / ')[0],'%d/%m/%Y').strftime('%Y-%m-%d')
#         end_date_string     = datetime.strptime(date_range.split(' / ')[1],'%d/%m/%Y').strftime('%Y-%m-%d')
#         profissional_search = request.GET.get('profissional')
#         forma_pagamento     = request.GET.get('forma_pagamento')
#         paciente            = request.GET.get('paciente')
#         if prof:
#             #se profissional estiver logado ele exibe a busca conforme ele
#             conta = ReciboPago.objects.filter(data_upload__date__range=(
#                 start_date_string,end_date_string),profissional_id=prof.id).order_by('-data_upload')
#             #reatribui o valor do contexto com o novo valor
#             contas     = Paginator(conta,25).get_page(request.GET.get('page'))
#         else:
#             #se admin estiver logado
#             conta = ReciboPago.objects.filter(data_upload__date__range=(
#                 start_date_string,end_date_string), profissional__nome__icontains=profissional_search,
#             ).order_by('-data_upload')
#             #reatribui o valor do contexto com o novo valor
#             contas     = Paginator(conta,25).get_page(request.GET.get('page'))
#     else:
#         #exibe todos os atendimentos quando abrir a pagina conforme o tipo de user logado
#         if prof:
#             conta      = ReciboPago.objects.select_related('profissional').filter(
#                 profissional_id=prof.id).order_by('-data_upload')
#             #lista de recibos pagos profissional
#             contas     = Paginator(conta,25).get_page(request.GET.get('page'))
#         else:
#             conta      = ReciboPago.objects.select_related('profissional').order_by('-data_upload')
#             #lista de recibos pagos admin
#             contas     = Paginator(conta,25).get_page(request.GET.get('page'))

#     return render(request,'contas_pagar/recibos_pagos.html',{'lista_dados':contas})


def leaders(request):
    lideres = ''
    if request.GET.get('name'):
        name            = request.GET.get('name')
        sex             = request.GET.get('sex')
        lideres = Leader.objects.filter(name__icontains=name,sex=sex)
    else:
        lideres = Leader.objects.all().exclude(user__username='admin')
    context = {
        'lideres':lideres
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
        discipulo.exited = request.POST.get('motivo')
        discipulo.save()
        discipulo.delete()
        return redirect('discipulos')
    return render(request,'disciples/delete.html',{'form':form})
    