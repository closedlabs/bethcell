from django.urls import path
from django.contrib.auth import views as auth_views
from usuarios import views

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(
    	template_name='login.html'), name='login'),
	path('bemvindo/',views.login_success,name="login_success"),
	path('sair',auth_views.LogoutView.as_view(), name='logout'),
	path('adicionar_lider/',views.add_usuario, name='adicionar_usuario'),
	path('lider/<str:slug>/atualizar/',views.LiderUpdateView.as_view(), name='atualizar_usuario'),
]
