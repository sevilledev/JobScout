# Generated by Django 4.0.3 on 2022-03-31 13:55

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joblist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobcard',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
