# Generated by Django 4.1.5 on 2023-01-16 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screenshots', '0027_alter_screenshots_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screenshots',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='screenshot'),
        ),
    ]
