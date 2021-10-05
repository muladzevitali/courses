from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import (User, UserProfile)


class MyUserAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email', 'last_login', 'is_active', 'is_staff',)
    list_display_links = ('first_name', 'last_name', 'username', 'email')
    readonly_fields = ('password', 'last_login', 'date_joined')
    search_fields = ('first_name', 'last_name', 'username', 'email')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html(f'<img src="{obj.profile_picture.url}" width="30" style="border-radius: 50%;">')

    thumbnail.short_description = 'Profile picture'
    list_display = ('user', 'city', 'state', 'country', 'thumbnail')


# Register your models here.
admin.site.register(User, MyUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
