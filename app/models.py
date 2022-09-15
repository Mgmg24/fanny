from django.db import models

# Create your models here.
class Result(models.Model):
    top=models.CharField(max_length=50)
    letter=models.TextField(max_length=10000)