from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("username", "full_name", "email", "phone_number", "is_active", "is_staff", "date_joined")
    search_fields = ("username", "full_name", "email", "phone_number")
    fieldsets = BaseUserAdmin.fieldsets + (
        ("Delivery Profile", {"fields": ("full_name", "phone_number", "home_address")}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ("Delivery Profile", {"fields": ("full_name", "email", "phone_number", "home_address")}),
    )