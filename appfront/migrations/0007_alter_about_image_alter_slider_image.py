# Generated by Django 4.0.3 on 2022-03-19 18:01

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfront', '0006_rename_services_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/home/sevilledev/Desktop/Django/jobscout/media/slider_media'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/home/sevilledev/Desktop/Django/jobscout/media/slider_media'), upload_to=''),
        ),
    ]
