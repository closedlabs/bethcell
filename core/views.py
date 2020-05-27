from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect
from core.models import Celula, Evasao
from members.models import Leader,Discipulo
from django.db.models import Count
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
        leader     = Leader.objects.filter(birth__day=today.day,birth__month=today.month).count()
        discipulo = Discipulo.objects.filter(birth__day=today.day,birth__month=today.month).count()
        context['aniversarios']   = leader + discipulo
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
        context['lideres']     = Leader.objects.filter(birth__day=today.day,birth__month=today.month)
        context['discipulos'] = Discipulo.objects.filter(birth__day=today.day,birth__month=today.month)
        return context

   
'''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+                                              Células
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

def celulas(request):
    if request.user.is_superuser:
        celulas = Celula.objects.all()
    else:
        usuario = request.user.pk
        leader   = Leader.objects.get(user=usuario,tipo='LG')
        celulas = Celula.objects.filter(lider__lider_de_rede=leader)
    context = {
        'celulas':celulas
    }
    return render(request,'celulas/celulas.html',context)

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

class CelulaDetailView(SuccessMessageMixin,DetailView):
    model           = Celula
    template_name   = "celulas/celula_sobre.html"

    def get_context_data(self, **kwargs):
        context = super(CelulaDetailView, self).get_context_data(**kwargs)
        #celula = Celula.get_object_or_404(Celula,pk=pk)
        context['nivel_0']  = Discipulo.objects.filter(celula=self.object,ladder='N0').count()
        context['nivel_1']  = Discipulo.objects.filter(celula=self.object,ladder='N1').count()
        context['nivel_2']  = Discipulo.objects.filter(celula=self.object,ladder='N2').count()
        context['nivel_3']  = Discipulo.objects.filter(celula=self.object,ladder='N3').count()
        context['trainee']  = Discipulo.objects.filter(celula=self.object,ladder='N4').count()
        context['trainee_formado']  = Discipulo.objects.filter(celula=self.object,ladder='N5').count()
        return context

class CelulaDeleteView(DeleteView):
    model         = Celula
    template_name = "celulas/delete_celula.html"
    success_url   = '/celulas'

def evasao(request):
    evasao = Evasao.objects.all()
    return render(request,'evasao/evasao.html',{'evasao':evasao})
    