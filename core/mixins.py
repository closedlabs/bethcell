# -*- coding: utf-8 -*-
from core.models import Celula
from members.models import Lider,Discipulo

class DashboardMixin(object):
    #conta o total de lideres no banco.. 
    def get_context_data(self, **kwargs):
        context              = super(DashboardMixin, self).get_context_data(**kwargs)
        #is admin
        if self.request.user.is_superuser:
            context['lideres_count']    = Lider.objects.all().count()
            context['celulas_count']    = Celula.objects.all().count()
            context['discipulos_count'] = Discipulo.objects.all().count()

        else:
            lider = Lider.objects.get(user=self.request.user.pk,tipo='LG')
            context['lideres_count']     = Lider.objects.filter(lider_de_rede=lider).count()
            context['celulas_count']     = Celula.objects.filter(lider__lider_de_rede=lider).count()
            context['discipulos_count']  = Discipulo.objects.filter(lider__lider_de_rede=lider).count()
        return context
    
    #retorna os aniversariantes do dia..
    def aniversarios(self):
        today     = timezone.now().date()
        lider     = Lider.objects.filter(nascimento__day=today.day,nascimento__month=today.month).count()
        discipulo = Discipulo.objects.filter(nascimento__day=today.day,nascimento__month=today.month).count()
        return discipulo + lider
