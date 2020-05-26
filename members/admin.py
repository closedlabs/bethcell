from django.contrib import admin
from members.models import Lider,Discipulo


class LiderAdmin(admin.ModelAdmin):
	list_display = ('user','ministerial_situation','lider_de_rede')


class DiscipuloAdmin(admin.ModelAdmin):
	list_display = ('name','lider','ministerial_situation','celula')	

admin.site.register(Lider,LiderAdmin)	
admin.site.register(Discipulo,DiscipuloAdmin)
