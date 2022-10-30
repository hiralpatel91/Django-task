from django.db import models

# Create your models here.

class Add(models.Model):
    name = models.CharField( max_length=50 )
    branch = models.CharField( max_length=50 )
    language = models.CharField( max_length=50 )
    field = models.CharField( max_length=50 )
    technical_language = models.CharField( max_length=50 )