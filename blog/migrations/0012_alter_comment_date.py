# Generated by Django 4.0.3 on 2022-03-14 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_comment_main_parent_alter_comment_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default='14.03.2022 12:51:52'),
        ),
    ]
