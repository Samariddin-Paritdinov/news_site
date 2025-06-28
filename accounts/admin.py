from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import User
# Register your models here.


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("id", "email", "first_name", "last_name", "is_active", "is_staff")
    list_display_links = ("id", "email", "first_name", "last_name")
    search_fields = ("email", "first_name", "last_name")
    list_filter = ("is_active", "is_staff")
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'avatar', 'bio')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Other info'), {'fields': ('created_at', 'updated_at')}),
    )
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-id',)
