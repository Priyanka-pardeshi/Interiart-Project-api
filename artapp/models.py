from django.db import models


# Create your models here.
class Information(models.Model):
    date = models.DateTimeField()
    Arrival = models.IntegerField()
    Departures = models.IntegerField()


class Quote(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    property_type = models.CharField(max_length=30)
    service_type = models.CharField(max_length=30)
    message = models.TextField()
