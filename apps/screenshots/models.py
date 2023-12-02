from django.contrib import admin
from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from thumbnails.fields import ImageField
import os
from django.core.files.base import File
import tempfile


# Create your models here.

class Devices(models.Model):
    serial = models.CharField(verbose_name='Serial number', null=True, max_length=100)
    model = models.CharField(verbose_name='Model', null=True, max_length=100)
    brand = models.CharField(verbose_name='Brand', null=True, max_length=100)
    create_time = models.DateTimeField(verbose_name='Create at', auto_now_add=True, null=True)
    modified_time = models.DateTimeField(verbose_name='Last modify', auto_now=True, null=True)
    is_active_phone = models.BooleanField(verbose_name='Active', default=True)

    class Meta:
        db_table = "device"
        verbose_name_plural = _("devices")
        verbose_name = _("device")

    def take_screen_shot(self, request):

        with tempfile.NamedTemporaryFile(suffix=".png") as new_screen:
            cmd_take_screen = f'adb -s {self.serial} exec-out screencap -p > {new_screen.name}'
            os.system(cmd_take_screen)
            try:
                Screenshots.objects.create(image=File(open(new_screen.name, "rb")), device=self)
                messages.add_message(request, messages.SUCCESS, f"screenshot taken from {self.serial}")
            except Exception as e:
                messages.add_message(request, messages.ERROR,
                                     f"screenshot wasn't taken from {self.serial} // error : {e}")

    def __str__(self):
        return f'{self.serial}'


class Screenshots(models.Model):
    image = ImageField(verbose_name='Screenshot', upload_to='screenshots/')
    device = models.ForeignKey(Devices, on_delete=models.CASCADE)
    create_time = models.DateTimeField(verbose_name='Created at', auto_now_add=True, null=True)
    modified_time = models.DateTimeField(verbose_name='Last modify', auto_now=True, null=True)

    class Meta:
        db_table = "screenshot"
        verbose_name_plural = _("screenshots")
        verbose_name = _("screenshot")

    @property
    def thumbnail(self):
        try:
            return self.image.thumbnails.large.url
        except Exception as e:
            print(e)
