# Generated by Django 4.1.4 on 2023-01-08 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('screenshots', '0020_remove_devices_device_code_devices_d_brand_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='screenshots',
            name='device',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='screenshots.devices'),
            preserve_default=False,
        ),
    ]