from typing import Any
from django.db import models

# Create your models here.
class News(models.Model):
    headline = models.CharField(max_length=250)
    body = models.TextField()
    date = models.DateField()
    def __str__(self) -> str:
        return self.headline