# Generated by Django 4.1.4 on 2023-01-03 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('screenshots', '0010_alter_screenshots_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devices',
            name='device_model',
        ),
    ]