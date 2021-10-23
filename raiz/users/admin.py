from django.contrib import admin
from django.contrib import auth
from django.contrib.auth import admin as auth_admin

from .forms import UserChangeForm, UserCreationForm
from .models import User

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Biografia", {"fields": ("bio",)}),
        ("Imagem do Usuário", {"fields": ("user_imagem",)}),


    )



