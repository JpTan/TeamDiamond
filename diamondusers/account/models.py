from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    id_number = models.CharField(max_length=8, blank=True)
    college = models.CharField(max_length=10, blank=True)
    course = models.CharField(max_length=10, blank=True)
    cellphone_number = models.CharField(max_length=11, blank=True)
    payment = models.FloatField(default=0.0)
