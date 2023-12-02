import os
import subprocess
from django.core.files.base import File
import tempfile

from apps.screenshots.models import Screenshots, Devices


def take_screenshot():
    cmd = 'adb devices'
    tmp = subprocess.check_output(cmd, shell=True)
    connected_devices = tmp.strip().decode('utf-8')

    split = connected_devices.split("\n")
    print(split)
    for c in split[1:]:
        serial = c.split("\t")[0]

        if not is_phone_exist(serial):
            add_device(serial)

    for d in Devices.objects.filter(is_active_phone=True):

        if connected_devices.find(d.serial) == -1:
            print(f"device {d.serial} isn't connected")
            continue

        with tempfile.NamedTemporaryFile(suffix=".png") as new_screen:
            cmd_tack_screen = f'adb -s {d.serial} exec-out screencap -p > {new_screen.name}'
            os.system(cmd_tack_screen)
            try:
                Screenshots.objects.create(image=File(open(new_screen.name, "rb")), device=d)
            except Exception as e:
                print(f"{d.serial} error : {e}")


def add_device(serial):
    cmd = f'adb -s {serial} shell getprop ro.product.model'
    tmp = subprocess.check_output(cmd, shell=True)
    model = tmp.strip().decode('utf-8')

    cmd = f'adb -s {serial} shell getprop ro.product.manufacturer'
    tmp = subprocess.check_output(cmd, shell=True)
    brand = tmp.strip().decode('utf-8')

    Devices.objects.create(serial=serial, brand=brand, model=model)


def is_phone_exist(obj: str):
    if Devices.objects.filter(serial=obj):
        return True
    else:
        return False
