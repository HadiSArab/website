from django.db import models

# Create your models here.

class item(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    score = models.IntegerField(max_length=100)
    creation_time = models.DateTimeField(auto_now_add=True)