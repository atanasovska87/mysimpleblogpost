# Generated by Django 3.0 on 2021-02-25 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0010_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook_url',
            field=models.CharField(max_length=255, null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram_url',
            field=models.CharField(max_length=255, null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='profile',
            name='pinterest_url',
            field=models.CharField(max_length=255, null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter_url',
            field=models.CharField(max_length=255, null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='profile',
            name='website_url',
            field=models.CharField(max_length=255, null='True'),
            preserve_default='True',
        ),
    ]
