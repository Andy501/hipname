from django.db import models
from django.contrib.auth.models import User


class CoolName(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    cool_name1 = models.CharField(max_length=200)
    cool_name2 = models.CharField(max_length=200)
    coolifiedPerformed = models.BooleanField()

