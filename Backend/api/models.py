from django.db import models

# Create your models here.
class SensorData(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField(blank=True)
    humidity = models.FloatField(blank=True)
    soilMoisture = models.FloatField(blank=True)
    lightLevel = models.FloatField(blank=True)
    phLevel = models.FloatField(blank=True)

    def __str__(self):
        return self.time
    

class FanState(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now_add=True)
    state = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.time} {self.state}"

class WaterState(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now_add=True)
    state = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.time} {self.state}"

class LightState(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now_add=True)
    state = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.time} {self.state}"

class ShadeState(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now_add=True)
    state = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.time} {self.state}"

class FertilizersState(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now_add=True)
    state = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.time} {self.state}"

class MistState(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now_add=True)
    state = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.time} {self.state}"

class WaterPumpState(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now_add=True)
    state = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.time} {self.state}"

class HeaterState(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now_add=True)
    state = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.time} {self.state}"
