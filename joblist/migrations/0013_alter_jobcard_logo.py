# Generated by Django 4.0.3 on 2022-03-19 18:01

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joblist', '0012_merge_20220319_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobcard',
            name='logo',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/home/sevilledev/Desktop/Django/jobscout/media/job_media'), upload_to=''),
        ),
    ]
