from django.db import models

# Create your models here.
class URL(models.Model):
    link=models.CharField(max_length=10000)
    shortLink=models.CharField(max_length=20)
    