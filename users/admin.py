from django.contrib import admin

from .models import Users

@admin.register(Users)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["username", "phone", "email"]
