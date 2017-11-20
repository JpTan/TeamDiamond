from django.db import models
from dbhandler.models import Student, Payment, Loan


class Staff(models.Model):
    email = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.email
