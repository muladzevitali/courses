from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class MyUserAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email', 'last_login', 'is_active', 'is_staff',)
    list_display_links = ('first_name', 'last_name', 'username', 'email')
    readonly_fields = ('password', 'last_login', 'date_joined')
    search_fields = ('first_name', 'last_name', 'username', 'email')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


# Register your models here.
admin.site.register(User, MyUserAdmin)
