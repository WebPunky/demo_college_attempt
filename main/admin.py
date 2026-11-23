from django.contrib import admin

from .models import Services, Orders

@admin.register(Services)
class CustomServicesAdmin(admin.ModelAdmin):
    fields = ["image" ,"title", "desc", "price"]

@admin.register(Orders)
class CustomOrdersAdmin(admin.ModelAdmin):
    fields = ["service", "user", "scheduled_at"]