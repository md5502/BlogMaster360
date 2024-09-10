from django.contrib import admin

# Register your models here.

from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'created_at', 'updated_at']
    search_fields = ['user', 'created_at']
    list_filter = ['created_at']
    readonly_fields = ['created_at', 'updated_at']

admin.site.register(Profile, ProfileAdmin)