from django.urls import path
from core import views

urlpatterns = [
##############################HOME############################################
	path('',views.Dashboard.as_view(),name='dashboard'),
	path('gestao/',views.GerirCelulas.as_view(),name="gestao_celular"),
	path('aniversariantes/',views.AniversariantesView.as_view(),name='aniversariantes'),
##############################CRUD DE LIDERES############################################
	path('lideres/',views.lideres,name="lista_lideres"),
	path('pastores/',views.lista_lider,name="pastores"),
	path('lider/<int:pk>/',views.lider_delete,name="lider_delete"),
	path('lider/<str:slug>/detalhes',views.LiderDetailView.as_view(),name="lider_detalhe"),
	path('lider/<str:slug>/excluir',views.LiderDeleteView.as_view(),name="excluir_lider"),
	#path('update/',views.update_lider,name="lideres"),
	path('filhos/<int:pk>',views.lista_filhos,name="lista_filhos"),
	######################CRUD DE DISCIPULOS############################################
	path('discipulos/',views.discipulos,name="discipulos"),
	path('adicionar/discipulo/',views.DiscipuloCreateView.as_view(),name="adicionar_discipulo"),
	path('discipulo/<str:slug>/',views.discipulo_delete,name="discipulo_delete"),
	path('discipulo/<str:slug>/atualizar/',views.DiscipuloUpdateView.as_view(),name="discipulo_update"),
	path('discipulo/<str:slug>/detalhes/',views.DiscipuloDetailView.as_view(),name="discipulo_detalhe"),
	######################CRUD DE CÈLULAS############################################
	path('celulas/', views.celulas, name='celulas'),
    path('adicionar/celula/',views.CelulaCreateView.as_view(),name='adicionar_celula'),
    path('adicionar/<int:pk>/celula/',views.CelulaUpdateView.as_view(),name='atualizar_celula'),
    path('celula/<int:pk>/excluir/',views.CelulaDeleteView.as_view(),name='excluir_celula'),

    ############EVASAO############################################
	path('evasao/', views.evasao, name='evasao'),
]	
	