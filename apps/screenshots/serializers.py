from utils.strings import *
from .models import Devices, Screenshots
from rest_framework import serializers


class DeviceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = (SERIAL, MODEL, BRAND, CREATE)


class ScreenshotsSerializer(serializers.ModelSerializer):
    device = serializers.SlugRelatedField(read_only=True, slug_field=SERIAL)

    class Meta:
        model = Screenshots
        fields = (ID, THUMBNAIL, DEVICE, CREATE)


class ScreenshotInfoSerializer(serializers.ModelSerializer):
    device = DeviceDetailSerializer()

    class Meta:
        model = Screenshots
        fields = (ID, THUMBNAIL, DEVICE, CREATE)


class ScreenshotCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screenshots
        fields = (IMAGE, DEVICE)
