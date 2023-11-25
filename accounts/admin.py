from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # CustomUserAdmin
    # Fields: id, email, password, last_login, is_superuser, username, first_name, last_name, is_staff, is_active, date_joined, groups, user_permissions
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('is_student', 'is_author')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (None, {'fields': ('is_student', 'is_author')}),

admin.site.register(CustomUser, CustomUserAdmin)
