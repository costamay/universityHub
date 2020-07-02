from django.db import models

# Create your models here.

class Home(models.Model):
    header = models.CharField(max_length=60)
    description = models.TextField()
    home_image = models.ImageField()