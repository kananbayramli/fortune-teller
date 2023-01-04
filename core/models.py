from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    horoscope = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.user