from django.db import models

# Create your models here.
class SensorData(models.Model):
    
    time = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField(blank=True)
    humidity = models.FloatField(blank=True)
    soilMoisture = models.FloatField(blank=True)
    lightLevel = models.FloatField(blank=True)
    phLevel = models.FloatField(blank=True)

    def __str__(self):
        return self.time
    

class FanState(models.Model):
    time = models.DateTimeField(primary_key=True)
    state = models.BooleanField(default=False)
    def __str__(self):
        return self.time

class WaterState(models.Model):
    time = models.DateTimeField(primary_key=True)
    state = models.BooleanField(default=False)
    def __str__(self):
        return self.time

class LightState(models.Model):
    time = models.DateTimeField(primary_key=True)
    state = models.BooleanField(default=False)
    def __str__(self):
        return self.time

class ShadeState(models.Model):
    time = models.DateTimeField(primary_key=True)
    state = models.BooleanField(default=False)
    def __str__(self):
        return self.time

class FertilizersState(models.Model):
    time = models.DateTimeField(primary_key=True)
    state = models.BooleanField(default=False)
    def __str__(self):
        return self.time

class MistState(models.Model):
    time = models.DateTimeField(primary_key=True)
    state = models.BooleanField(default=False)
    def __str__(self):
        return self.time

class WaterPumpState(models.Model):
    time = models.DateTimeField(primary_key=True)
    state = models.BooleanField(default=False)
    def __str__(self):
        return self.time

class HeaterState(models.Model):
    time = models.DateTimeField(primary_key=True)
    state = models.BooleanField(default=False)
    def __str__(self):
        return self.time
