import subprocess

from django.contrib import admin, messages
from django.utils.html import format_html
from django_admin_relation_links import AdminChangeLinksMixin
from django_object_actions import DjangoObjectActions, action, takes_instance_or_queryset
from utils.strings import *
import thumbnails

from apps.screenshots.models import Devices, Screenshots


# Register your models here.


@admin.register(Devices)
class DeviceAdmin(admin.ModelAdmin, DjangoObjectActions):
    list_display = (ID, SERIAL, MODEL, BRAND, IS_ACTIVE_PHONE)
    changelist_links = ('screenshots',)
    list_editable = (IS_ACTIVE_PHONE,)
    ordering = (f"-{ID}",)
    search_fields = (f"={SERIAL}",)
    fieldsets = (
        (None, {FIELDS: (SERIAL, MODEL, BRAND, IS_ACTIVE_PHONE)}),
        ('times', {FIELDS: (CREATE, MODIFIED)})
    )

    # @takes_instance_or_queryset
    @action(description="Take a screenshot")
    def take_screen(self, request, queryset):
        cmd = 'adb devices'
        tmp = subprocess.check_output(cmd, shell=True)
        connected_devices = tmp.strip().decode('utf-8')

        for obj in queryset:
            if connected_devices.find(obj.serial) == -1:
                messages.add_message(request, messages.ERROR, f"device {obj.serial} isn't connected")
            elif not obj.is_active_phone:
                messages.add_message(request, messages.ERROR, f"device {obj.serial} isn't active!")
            else:
                obj.take_screen_shot(request)

    # @takes_instance_or_queryset
    @action(description="Activate the devices")
    def update_status(self, request, queryset):
        queryset.update(is_active_phone=True)
        messages.add_message(request, messages.SUCCESS, "The specified devices are available.")

    # @takes_instance_or_queryset
    @action(description='Massage')
    def massage(self):
        pass

    readonly_fields = (CREATE, MODIFIED)
    actions = ("take_screen", 'update_status', 'massage')
    change_actions = ("take_screen", 'update_status', 'massage')


@admin.register(Screenshots)
class ScreenshotsAdmin(admin.ModelAdmin):
    list_display = (ID, 'screen_logo', DEVICE, CREATE, MODIFIED)
    change_links = (DEVICE,)
    ordering = (f"-{CREATE}",)
    search_fields = (f"=device__serial",)
    fieldsets = (
        (None, {FIELDS: (DEVICE,)}),
        ('times', {FIELDS: (CREATE, MODIFIED)}),
        ('screenshot', {FIELDS: (IMAGE, 'screen')})
    )
    readonly_fields = ('screen_logo', CREATE, MODIFIED, 'screen')

    @staticmethod
    def screen(obj: "Screenshots"):
        try:
            return format_html(
                f'<a>'
                f'<image src="{obj.image.url}" width=250/>'
                f'</a>'
            )
        except Exception as e:
            print(e)

    @staticmethod
    def screen_logo(obj: 'Screenshots'):
        try:
            return format_html(
                f'<a>'
                f'<image src="{obj.thumbnail}" width="64"/>'
                f'</a>'
            )
        except Exception as e:
            print(e)
