from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=255)
    account_number = models.CharField(max_length=13, blank=True, null=True)
    business_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField()
    point = models.IntegerField(default=0)