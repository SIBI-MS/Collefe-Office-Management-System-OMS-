from django.db import models
from django.utils import timezone
from datetime import timedelta


from django.db import models

class Student(models.Model):
    card_id = models.CharField(max_length=20, primary_key=True, default='0')
    admission_no = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    level = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    sex = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    time_spend = models.IntegerField(default=0)


    def __str__(self):
        if self.name is None:
            return str(self.card_id)
        else:
            return str(self.name) 


class Log(models.Model):
    card_id = models.CharField(max_length=20, default='0')

    admission_no = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    level = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(default=timezone.now)  # Use timezone.now for date
    time_in = models.TimeField(default=timezone.now)  # Use timezone.now for time_in
    time_out = models.TimeField(blank=True, null=True)
    total_hours=models.CharField(max_length=50)
    status = models.TextField(max_length=100)

    def __str__(self):
        return str(self.name) + ' : ' + str(self.date)

