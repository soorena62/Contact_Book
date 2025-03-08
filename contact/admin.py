from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Contact, CustomUser
# Register your models here:


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "user"]
    search_fields = ("first_name", "last_name", "phone_number")
    ordering = ["first_name"]

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "is_staff", "ia_active")
    ordering = ["username"]

admin.site.register(CustomUser, UserAdmin)

