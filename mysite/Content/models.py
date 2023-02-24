from django.db import models

# Create your models here.

class Propuesta(models.Model):
    Title =  models.CharField(max_length=20)
    Description = models.TextField()
    Grado = models.IntegerField()
    Email = models.EmailField()