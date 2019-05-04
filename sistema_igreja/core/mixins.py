# -*- coding: utf-8 -*-
from core.models import Lider,Discipulo,Celula

class DashboardMixin(object):
	#conta o total de lideres no banco..
	def lideres_count(self):
		return Lider.objects.all().count()

	#conta o total de discipulos no banco.. 
	def discipulos_count(self):
		return Discipulo.objects.all().count()

	#conta o total de Células no banco.. 
	def celulas_count(self):
		return Celula.objects.all().count()

	#retorna os aniversariantes do dia..
	def aniversarios(self):
		today     = timezone.now().date()
		lider     = Lider.objects.filter(nascimento__day=today.day,nascimento__month=today.month).count()
		discipulo = Discipulo.objects.filter(nascimento__day=today.day,nascimento__month=today.month).count()
		return discipulo + lider
