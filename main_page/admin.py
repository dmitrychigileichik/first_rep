from django.contrib import admin
from main_page import models

class UserAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'full_name',
        'is_active',
        'is_verified'
    ]

admin.site.register(models.User, UserAdmin)
