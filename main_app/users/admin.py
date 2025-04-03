from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("nickname", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "email")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important dates", {"fields": ("date_joined",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("nickname", "email", "password1", "password2"),
        }),
    )

    list_display = ("nickname", "email", "is_staff")
    search_fields = ("nickname", "email")
    ordering = ("nickname",)

admin.site.register(CustomUser, CustomUserAdmin)