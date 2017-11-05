from django.db import models


# Create your models here.
class Student(models.Model):
    idNum = models.CharField(max_length=8)
    lastName = models.CharField(max_length=20)
    firstName = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    cpNum = models.CharField(max_length=10)
    college = models.CharField(max_length=3)
    degree = models.CharField(max_length=20)
    level = models.CharField(max_length=1)
    password = models.CharField(max_length=20)


class Payment(models.Model):
    orNum = models.CharField(max_length=20)
    amount = models.FloatField()
    date = models.DateField()
    idNum = models.ForeignKey(Student, on_delete=models.CASCADE)
    isApproved = models.BooleanField()


class Loan(models.Model):
    idNum = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateField()
    status = models.CharField(max_length=10)
    balance = models.FloatField()


