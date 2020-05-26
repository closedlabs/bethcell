from django.contrib import admin
from core.models import Celula,Evasao


class EvasaoAdmin(admin.ModelAdmin):
	list_display = ('name','sex','date_delete')
	
class CelulaAdmin(admin.ModelAdmin):
	list_display = ('name','leader',)		

admin.site.register(Celula,CelulaAdmin)
admin.site.register(Evasao,EvasaoAdmin)