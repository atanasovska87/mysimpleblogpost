# Generated by Django 3.0 on 2021-02-19 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0007_post_header_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click on the link Above to read Blog Post', max_length=255),
        ),
    ]
