# Generated by Django 4.1.4 on 2023-01-03 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screenshots', '0009_alter_devices_device_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screenshots',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='screenshot'),
        ),
    ]
