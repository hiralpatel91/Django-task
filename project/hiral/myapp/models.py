from django.db import models

# Create your models here.

class Add(models.Model):
    name = models.CharField( max_length=50)
    branch = models.CharField( max_length=50)