# Generated by Django 4.0.2 on 2022-03-10 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
    ]
