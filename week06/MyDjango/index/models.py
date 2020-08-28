from django.db import models

# Create your models here.

class Film(models.Model):
    shortreview = models.CharField(max_length= 200)
    stars = models.CharField(max_length= 5)
    date = models.CharField(max_length= 20)