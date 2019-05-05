from django.shortcuts import render,get_object_or_404,redirect
from core.models import Lider,Celula
from core.mixins import DashboardMixin
from django.views.generic import TemplateView,DetailView,CreateView,UpdateView,DeleteView
from core.forms import *
from django.db import transaction
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
import datetime

class Dashboard(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        today     = datetime.datetime.now()
        lider     = Lider.objects.filter(nascimento__day=today.day,nascimento__month=today.month).count()
        discipulo = Discipulo.objects.filter(nascimento__day=today.day,nascimento__month=today.month).count()
        context['aniversarios']   = lider + discipulo
        context['celulas']   = Celula.objects.annotate(
            number_of_discipulos=Count('discipulo')).order_by('-number_of_discipulos')
        return context


class GerirCelulas(DashboardMixin,TemplateView):
    template_name = "home/gestao_celular.html"
   

class AniversariantesView(TemplateView):
    template_name = "aniversariantes/aniversarios.html"

    def get_context_data(self, **kwargs):
        context              = super(AniversariantesView, self).get_context_data(**kwargs)
        today                = datetime.datetime.now()
        context['lideres']     = Lider.objects.filter(nascimento__day=today.day,nascimento__month=today.month)
        context['discipulos'] = Discipulo.objects.filter(nascimento__day=today.day,nascimento__month=today.month)
        return context


'''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+                         VIEWS DE LIDERES DE CÈLULA
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

def lista_lider(request):
    query = Lider.objects.filter(tipo='PR')
    return render(request,'index.html',{'lider':query})

def lista_filhos(request,pk):
    query = Lider.objects.filter(lider_de_rede=pk)
    return render(request,'filhos.html',{'filhos':query})

def lideres(request):
    if request.user.is_superuser:
        lideres = Lider.objects.all()
    else:
        usuario = request.user.pk
        lider = Lider.objects.get(user=usuario,tipo='LG')
        print('lider de rede:',lider)
        lideres = Lider.objects.filter(lider_de_rede=lider)
    context = {
        'lideres':lideres
    }
    return render(request,'lideres/lideres.html',context)

class LiderDetailView(DetailView):
    model = Lider
    template_name = "lideres/detalhes.html"

class LiderDeleteView(DeleteView):
    model         = Lider
    template_name = "lideres/delete_lider.html"
    success_url   = '/lideres'
"""
def lider_detalhe(request,pk):
    lider = Lider.objects.get(pk=pk)
    return render(request,'lideres/detalhes.html',{'lider':lider})
"""
def lider_delete(request,pk):
    lider = get_object_or_404(Lider,pk=pk)
    lider.delete()
    return redirect(request.META['HTTP_REFERER'])
    
'''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+                          VIEWS DE DISCIPULOS 
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

class DiscipuloCreateView(SuccessMessageMixin,CreateView):
    model           = Discipulo
    form_class      = DiscipuloForm
    template_name   = "discipulos/adicionar.html"
    success_url     = '/discipulos'
    success_message = 'Discipulo Cadastrado Com Sucesso!!!!'


class DiscipuloUpdateView(SuccessMessageMixin,UpdateView):
    model           = Discipulo
    form_class      = DiscipuloForm
    template_name   = "discipulos/adicionar.html"
    success_url     = '/discipulos'
    success_message = 'Dados Atualizados Com Sucesso!!!!'


class DiscipuloDetailView(DetailView):
    model = Discipulo
    template_name = "discipulos/detalhes.html"

"""
def adicionar_disicipulo(request):
    form = DiscipuloForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('discipulos')
    return render(request,'discipulos/adicionar.html',{'form':form})
"""
def discipulos(request):
    if request.user.is_superuser:
        discipulos = Discipulo.objects.all()
    else:
        usuario    = request.user.pk
        lider      = Lider.objects.get(user=usuario,tipo='LG')
        discipulos = Discipulo.objects.filter(lider__lider_de_rede=lider)
    context = {
        'discipulos':discipulos
    }
    return render(request,'discipulos/discipulos.html',context)

"""
def discipulo_update(request,pk):
    discipulo = get_object_or_404(Discipulo,pk=pk)
    form = DiscipuloForm(request.POST or None,instance=discipulo)
    if form.is_valid():
        form.save()
        return redirect('discipulos')
    return render(request,'discipulos/adicionar.html',{'form':form})
"""   
def discipulo_delete(request,slug):
    discipulo = get_object_or_404(Discipulo,slug=slug)   
    form = DiscipuloForm(request.POST or None,instance=discipulo)
    if request.method == 'POST':
        discipulo.saiu = request.POST.get('motivo')
        discipulo.save()
        discipulo.delete()
        return redirect('discipulos')
    return render(request,'discipulos/delete_confirm.html',{'form':form})
    
'''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+                           Células
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

def celulas(request):
    if request.user.is_superuser:
        celulas = Celula.objects.all()
    else:
        usuario = request.user.pk
        lider   = Lider.objects.get(user=usuario,tipo='LG')
        celulas = Celula.objects.filter(lider__lider_de_rede=lider)
    context = {
        'celulas':celulas
    }
    return render(request,'celulas/celulas.html',context)
"""   
def adicionar_celula(request):
    form = CelulaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('celulas')
    return render(request,'celulas/adicionar.html',{'form':form})
"""

class CelulaCreateView(SuccessMessageMixin,CreateView):
    model           = Celula
    template_name   = "celulas/adicionar.html"
    form_class      = CelulaForm
    success_url     = '/celulas'
    success_message = "Célula Cadastrada com Sucesso!"

class CelulaUpdateView(SuccessMessageMixin,UpdateView):
    model           = Celula
    template_name   = "celulas/adicionar.html"
    form_class      = CelulaForm
    success_url     = '/celulas'
    success_message = "Célula Atualizada com Sucesso!"

class CelulaDeleteView(DeleteView):
    model         = Celula
    template_name = "celulas/delete_celula.html"
    success_url   = '/celulas'

def evasao(request):
    evasao = Evasao.objects.all()
    return render(request,'evasao/evasao.html',{'evasao':evasao})
    