from django.db import models

# Create your models here.

class Photocard(models.Model):
  name = models.CharField(max_length=100)
  band = models.CharField(max_length=100)
  era = models.CharField(max_length=100)
  description = models.TextField(max_length=250)