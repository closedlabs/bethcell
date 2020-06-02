from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(
    	template_name='login/login.html'), name='login'),
	path('bemvindo/',views.login_success,name="login_success"),
	path('change/password/user/',views.change_password_user, name='update'),
	path('sair',auth_views.LogoutView.as_view(), name='logout'),
	
]
