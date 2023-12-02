from django.contrib import admin
from django.utils.html import format_html

from .models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as AbstractUserAdmin
from utils.strings import *


@admin.register(User)
class UserAdmin(AbstractUserAdmin):
    """
        Admin for user model
    """
    list_display = (ID, 'show_avatar', EMAIL, FIRST_NAME, LAST_NAME, IS_ACTIVE, IS_STAFF, IS_SUPERUSER)
    ordering = (EMAIL,)
    search_fields = (f"={ID}", EMAIL, FIRST_NAME, LAST_NAME)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": (AVATAR, "first_name", "last_name", "email", "icon")}),
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
    readonly_fields = ("icon",)

    @staticmethod
    def icon(obj: "User"):
        return format_html(
            f'<a>'
            f'<image src="{obj.avatar.url}" width=64 height=64/>'
            f'</a>'
        )
