from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form  = CustomUserChangeForm
    model = get_user_model()
    list_display = ['username','email','is_cell_leader','is_generation_leader','is_teacher']

    #adiciona os novos campos customizados no form de admin
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_teacher','is_generation_leader','is_cell_leader')}),

    )

admin.site.register(get_user_model(), CustomUserAdmin)