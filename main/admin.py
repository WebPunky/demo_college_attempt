from django.contrib import admin

from .models import Services, Orders, Review

@admin.register(Services)
class CustomServicesAdmin(admin.ModelAdmin):
    fields = ["image" ,"title", "desc", "price"]

@admin.register(Orders)
class CustomOrdersAdmin(admin.ModelAdmin):
    fields = ["service", "user", "scheduled_at", "status"]

@admin.register(Review)
class CustomReviewAdmin(admin.ModelAdmin):
    fields = ["rating", "comment"]