# Generated by Django 4.0.3 on 2022-03-20 13:29

from django.db import migrations, models
import utils.uploadimg


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_merge_20220319_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlefile',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=utils.uploadimg.upload_blog_img),
        ),
    ]