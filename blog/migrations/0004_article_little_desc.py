# Generated by Django 4.0.3 on 2022-03-20 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='little_desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
