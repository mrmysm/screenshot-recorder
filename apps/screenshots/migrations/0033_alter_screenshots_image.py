# Generated by Django 4.1.5 on 2023-01-17 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screenshots', '0032_alter_screenshots_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screenshots',
            name='image',
            field=models.ImageField(upload_to='screenshots/', verbose_name='screenshot'),
        ),
    ]
