from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Test1 (models.Model):
    test = models.ImageField(blank=True, null=True)
    test2 = models.CharField(max_length=250, default=True)

    def __str__(self):
        return self.test2