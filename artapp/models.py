from django.db import models


# Create your models here.
class Information(models.Model):
    date = models.DateTimeField()
    arrival = models.IntegerField()
    departures = models.IntegerField()



class Quote(models.Model):
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    property = models.CharField(max_length=30)
    service = models.CharField(max_length=30)
    message = models.TextField()
