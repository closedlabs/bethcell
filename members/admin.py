from django.contrib import admin
from members.models import Leader,Discipulo


class LeaderAdmin(admin.ModelAdmin):
	list_display = ('user','ministry','lider_de_rede','slug')


class DiscipuloAdmin(admin.ModelAdmin):
	list_display = ('name','leader','ladder','cell')	

admin.site.register(Leader,LeaderAdmin)	
admin.site.register(Discipulo,DiscipuloAdmin)
