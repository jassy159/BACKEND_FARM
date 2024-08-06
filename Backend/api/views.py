from django.shortcuts import render

# Create your views here.
from . import Serializers
from . import models  
from rest_framework import viewsets

class SensorDataView(viewsets.ModelViewSet):
    queryset = models.SensorData.objects.all()
    serializer_class = Serializers.SensorDataSerializer

class FanStateView(viewsets.ModelViewSet):
    queryset = models.FanState.objects.all()
    serializer_class = Serializers.FanStateSerializer

class WaterStateView(viewsets.ModelViewSet):
    queryset = models.WaterState.objects.all()
    serializer_class = Serializers.WaterStateSerializer

class LightStateView(viewsets.ModelViewSet):
    queryset = models.LightState.objects.all()
    serializer_class = Serializers.LightStateSerializer

class ShadeStateView(viewsets.ModelViewSet):
    queryset = models.ShadeState.objects.all()
    serializer_class = Serializers.SensorDataSerializer

class FertilizersStateView(viewsets.ModelViewSet):
    queryset = models.FertilizersState.objects.all()
    serializer_class = Serializers.FertilizerStateSerializer

class MistStateView(viewsets.ModelViewSet):
    queryset = models.MistState.objects.all()
    serializer_class = Serializers.MistStateSerializer

class WaterPumpView(viewsets.ModelViewSet):
    queryset = models.WaterPumpState.objects.all()
    serializer_class = Serializers.WaterPumpStateSerializer

class HeaterStateView(viewsets.ModelViewSet):
    queryset = models.HeaterState.objects.all()
    serializer_class = Serializers.HeaterStateSerializer
