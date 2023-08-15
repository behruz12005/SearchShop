from django.db import models

# Create your models here.

class MyModel(models.Model):
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    file = models.FileField(upload_to='file/')

