from django.db import models

class personal_data(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phonenumber = models.IntegerField(max_length=50)
    gender = models.CharField(max_length=255)
    size = models.CharField(max_length=50)

