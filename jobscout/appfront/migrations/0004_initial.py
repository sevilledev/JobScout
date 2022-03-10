# Generated by Django 4.0.2 on 2022-03-08 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appfront', '0003_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=20)),
                ('message', models.TextField()),
            ],
        ),
    ]
