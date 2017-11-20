from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    id_number = models.CharField(max_length=8, blank=True, primary_key=True)
    college = models.CharField(max_length=10, blank=True)
    course = models.CharField(max_length=10, blank=True)
    cellphone_number = models.CharField(max_length=11, blank=True)
    level = models.CharField(max_length=1, blank=True)

    def __str__(self):
        return self.last_name + ' ' + self.first_name


class Payment(models.Model):
    orNum = models.CharField(max_length=20)
    amount = models.FloatField()
    date = models.DateField()
    idNum = models.ForeignKey(Student, on_delete=models.CASCADE)
    isApproved = models.BooleanField(default=False)

    def __str__(self):
        return self.orNum


class Loan(models.Model):
    idNum = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, default='In Process')
    balance = models.FloatField(default=0)

    def __str__(self):
        return self.amount
