from django.db import models



# Create your models here.

class Person(models.Model):
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.CharField(max_length=100)
    password_entry = models.CharField(max_length=80)
    password_confirm = models.CharField(max_length=80)
