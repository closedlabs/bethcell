from django.contrib import admin
from core.models import Celula,Evasao,Meeting


class EvasaoAdmin(admin.ModelAdmin):
	list_display = ('name','sex','date_delete')
	
class CelulaAdmin(admin.ModelAdmin):
	list_display = ('name','leader',)		


class MeetingAdmin(admin.ModelAdmin):
	list_display = ('meeting_date','amount_member_present','amount_decicions','amount_visitors')	

admin.site.register(Celula,CelulaAdmin)
admin.site.register(Evasao,EvasaoAdmin)
admin.site.register(Meeting,MeetingAdmin)