from django.db import models


# Create your models here.
class Information(models.Model):
    date = models.DateField()
    Arrival = models.IntegerField()
    Departures = models.IntegerField()

# 2007 M 02
