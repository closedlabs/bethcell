from django.urls import path
from members import views

urlpatterns = [
##############################CRUD DE LIDERES############################################
	path('leaders/',views.leaders,name="leaders"),
	path('add_leader/',views.add_leader, name='add_leader'),
	path('leader/<str:slug>/update/',views.LeaderUpdateView.as_view(), name='leader_update'),
	path('leader/<str:slug>/detail',views.LeaderDetailView.as_view(),name="leader_detail"),
	path('leader/<str:slug>/delete',views.LeaderDeleteView.as_view(),name="leader_delete"),
	path('pastores/',views.lista_lider,name="pastores"),
	#path('update/',views.update_lider,name="lideres"),
	#path('filhos/<int:pk>',views.lista_filhos,name="lista_filhos"),

	######################CRUD DE DISCIPULOS############################################
	path('discipulos/',views.discipulos,name="discipulos"),
	path('adicionar/discipulo/',views.DiscipuloCreateView.as_view(),name="adicionar_discipulo"),
	path('discipulo/<str:slug>/',views.discipulo_delete,name="discipulo_delete"),
	path('discipulo/<str:slug>/atualizar/',views.DiscipuloUpdateView.as_view(),name="discipulo_update"),
	path('discipulo/<str:slug>/detalhes/',views.DiscipuloDetailView.as_view(),name="discipulo_detalhe"),

]	
	