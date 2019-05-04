from django.contrib import admin
from core.models import *

class LiderAdmin(admin.ModelAdmin):
	list_display = ('user','tipo','lider_de_rede')

class EvasaoAdmin(admin.ModelAdmin):
	list_display = ('nome','sexo','date_delete')
	
class CelulaAdmin(admin.ModelAdmin):
	list_display = ('nome','lider',)		
class DiscipuloAdmin(admin.ModelAdmin):
	list_display = ('nome','lider','tipo','celula')	

admin.site.register(Lider,LiderAdmin)
admin.site.register(Celula,CelulaAdmin)
admin.site.register(Discipulo,DiscipuloAdmin)
admin.site.register(Evasao,EvasaoAdmin)