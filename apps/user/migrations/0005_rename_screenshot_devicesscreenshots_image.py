# Generated by Django 4.1.4 on 2023-01-01 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_devices_phone_id_devices_d_id_devices_d_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='devicesscreenshots',
            old_name='screenShot',
            new_name='image',
        ),
    ]
