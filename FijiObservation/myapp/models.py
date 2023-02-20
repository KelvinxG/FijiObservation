from django.db import models

# Create your models here.

class FileUpload(models.Model):
    file=models.FileField()

class Parameter(models.Model):
    name = models.CharField(max_length=255)

class Station(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

class Observation(models.Model):
    time = models.DateTimeField()
    value = models.FloatField()
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)