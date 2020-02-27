from django.urls import path
from core import views

urlpatterns = [ 
    ###########################HOME############################################
	path('dashboard/',views.Dashboard.as_view(),name='dashboard'),
	path('gestao/',views.GerirCelulas.as_view(),name="gestao_celular"),
	path('aniversariantes/',views.AniversariantesView.as_view(),name='aniversariantes'),
    ############EVASAO############################################
	path('evasao/', views.evasao, name='evasao'),
	######################CRUD DE CÈLULAS############################################
	path('celulas/', views.celulas, name='celulas'),
    path('adicionar/celula/',views.CelulaCreateView.as_view(),name='adicionar_celula'),
    path('adicionar/<int:pk>/celula/',views.CelulaUpdateView.as_view(),name='atualizar_celula'),
    path('celula/sobre/<int:pk>/',views.CelulaDetailView.as_view(),name='celula_sobre'),
    path('celula/<int:pk>/excluir/',views.CelulaDeleteView.as_view(),name='excluir_celula'),

]	
	