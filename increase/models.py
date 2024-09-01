from django.db import models

# Create your models here.
class Count(models.Model):
    count = models.IntegerField(default=0)
