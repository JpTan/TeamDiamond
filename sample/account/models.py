from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    id_number = models.CharField(max_length=8)
    college = models.CharField(max_length=10)
    course = models.CharField(max_length=10)
    cellphone_number = models.CharField(max_length=11)
    payment = models.FloatField(default=0.0)

    def get_absolute_url(self):
        return reverse('account:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.first_name + ' ' + self.last_name
