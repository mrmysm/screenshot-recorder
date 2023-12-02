import datetime
import os

from django.core.management.base import BaseCommand, CommandError
from apps.screenshots.models import Screenshots, Devices
from subprocess import call

from take_device_screen.settings import BASE_DIR, MEDIA_ROOT


class Command(BaseCommand):
    help = 'tack screenshot from phone'

    def handle(self, *args, **options):
        current_time = datetime.datetime.now().time()
        cmd = f'adb exec-out screencap -p > {MEDIA_ROOT}/screen-{current_time}.jpg'

        os.system(cmd)
        scr = Screenshots.objects.create(image=f"screen-{current_time}.jpg",
                                         time=current_time)
        scr.save()
        self.stdout.write(self.style.SUCCESS('Success...'))

# f"screen-{datetime.datetime.now().time()}.png"
