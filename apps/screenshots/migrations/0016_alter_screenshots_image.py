# Generated by Django 4.1.4 on 2023-01-08 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screenshots', '0015_remove_screenshots_device'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screenshots',
            name='image',
            field=models.ImageField(upload_to='images', verbose_name='screenshot'),
        ),
    ]
