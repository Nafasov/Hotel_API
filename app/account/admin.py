from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'created_date')
    date_hierarchy = 'created_date'
    fieldsets = (
        (None, {"fields": ('email', 'password')}),
        ("Personal Datas", {"fields": ('first_name', 'last_name', 'avatar')}),
        ("Permissions", {"fields": ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ("Imported Dates", {"fields": ('last_login', 'modified_date', 'created_date')})
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    readonly_fields = ('last_login', 'modified_date', 'created_date')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    filter_horizontal = ('groups', 'user_permissions')
    list_editable = ('is_active', 'is_staff', 'is_superuser')
    ordering = ()
