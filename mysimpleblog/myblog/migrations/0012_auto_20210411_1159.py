# Generated by Django 3.0 on 2021-04-11 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0011_auto_20210225_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('email', models.CharField(max_length=100)),
                ('password_entry', models.CharField(max_length=80)),
                ('password_confirm', models.CharField(max_length=80)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='facebook_url',
            field=models.CharField(blank='True', max_length=255, null='True'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='instagram_url',
            field=models.CharField(blank='True', max_length=255, null='True'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pinterest_url',
            field=models.CharField(blank='True', max_length=255, null='True'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter_url',
            field=models.CharField(blank='True', max_length=255, null='True'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='website_url',
            field=models.CharField(blank='True', max_length=255, null='True'),
        ),
    ]
