# Generated by Django 4.1.5 on 2023-01-17 07:26

from django.db import migrations
import thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('screenshots', '0036_alter_screenshots_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screenshots',
            name='image',
            field=thumbnails.fields.ImageField(upload_to='screenshots/', verbose_name='screenshot'),
        ),
    ]
