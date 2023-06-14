from django.db import models

class Task(models.Model):
    title=models.CharField(max_length=40)
    desc = models.CharField(max_length=200)


# Create your models here.
