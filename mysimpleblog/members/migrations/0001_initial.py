# Generated by Django 3.0 on 2021-04-11 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
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
    ]