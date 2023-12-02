from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from thumbnails.fields import ImageField


class User(AbstractUser):
    """
        User model
    """
    phone = models.CharField(_('phone'), unique=True, max_length=13)
    avatar = ImageField(_('avatar'), max_length=200, null=True)

    class Meta:
        db_table = "user"
        verbose_name_plural = _("user")
        verbose_name = _("user")

    def __str__(self):
        return self.get_full_name()

    @admin.display(description='avatar')
    def show_avatar(self):
        return format_html(
            f'<a>'
            f'<image src="{self.avatar.thumbnails.large.url}" width=64 style="border-radius:2rem"/>'
            f'</a>'
        )

