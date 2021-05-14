from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core.models import User

from core.forms import UserCreationForm


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_admin')
    list_filter = ('is_admin', 'is_active')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),

        ('Permissions', {'fields': ('is_admin',)}),
    )

    search_fields = ('username', 'email')
    ordering = ('date_joined', 'username', 'email')

    filter_horizontal = ()
