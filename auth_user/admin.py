from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser
from allauth.socialaccount.models import SocialAccount


from django.contrib.auth.forms import (
    ReadOnlyPasswordHashField,
)

class SocialAccountInline(admin.StackedInline):
    model = SocialAccount
    extra = 0
    readonly_fields = ['provider', 'uid', 'user', 'extra_data', 'date_joined']


class CustomUserAdminForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            "Raw passwords are not stored, so there is no way to see this "
            "user’s password, but you can change the password using "
            '<a href="{}">this form</a>.'
        ),
    )
    class Meta:
        model = CustomUser
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = self.fields.get("password")
        if password:
            password.help_text = password.help_text.format("../password/")
        user_permissions = self.fields.get("user_permissions")
        if user_permissions:
            user_permissions.queryset = user_permissions.queryset.select_related(
                "content_type"
            )
        self.fields['email'].required = False


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email')
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "email",)
    inlines = [SocialAccountInline]
    # change_password_form = AdminPasswordChangeForm
    # form = CustomUserAdminForm
    # form = UserChangeForm

    fieldsets = (
        (None, {"fields": ("username", "password", "email", "github_account")}),
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
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    readonly_fields = ("last_login", "date_joined")

admin.site.register(CustomUser, CustomUserAdmin)
