# Generated by Django 4.0.3 on 2022-03-11 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joblist', '0009_jobcategory_alter_jobcard_logo_jobcard_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobcard',
            name='salary',
        ),
    ]
