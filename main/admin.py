from django.contrib import admin

from .models import Services

@admin.register(Services)
class CustomServicesAdmin(admin.ModelAdmin):
    fields = ["image" ,"title", "desc", "price"]