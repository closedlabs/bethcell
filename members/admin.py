from django.contrib import admin
from members.models import Lider,Discipulo


class LiderAdmin(admin.ModelAdmin):
	list_display = ('user','tipo','lider_de_rede')


class DiscipuloAdmin(admin.ModelAdmin):
	list_display = ('nome','lider','tipo','celula')	

admin.site.register(Lider,LiderAdmin)	
admin.site.register(Discipulo,DiscipuloAdmin)
