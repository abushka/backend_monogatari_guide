from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email')
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "email")

    fieldsets = (
        (None, {"fields": ("username", "password", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)  # Сначала сохраните модель
        obj.set_password(obj.password)  # Затем установите пароль
        obj.save()  # Сохраните модель с хешированным паролем

admin.site.register(CustomUser, CustomUserAdmin)