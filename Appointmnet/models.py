from django.db import models
import datetime
# Create your models here.


class Appointment(models.Model):
    first_name = models.CharField(max_length=101)
    last_name = models.CharField(max_length=101)
    email = models.EmailField()
    address_line1 = models.CharField(max_length=256)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    pincode = models.IntegerField()
    date_field = models.DateField()
    # time_field = models.TimeField()