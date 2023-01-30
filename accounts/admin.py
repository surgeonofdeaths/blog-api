from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):  # customizing user admin panel
    model = UserAdmin
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ['email', 'username', 'name', 'is_staff', ]
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('name',), }),)  # new user
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('name', )}), )


admin.site.register(CustomUser, CustomUserAdmin)
