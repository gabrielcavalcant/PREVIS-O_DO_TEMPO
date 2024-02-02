from django.db import models

class WeatherData(models.Model):
    temperature = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    precipitation = models.FloatField()
    condition = models.CharField(max_length=255)
