from django.shortcuts import render
from rest_framework import viewsets
from . import Serializers
from . import models

class SensorDataView(viewsets.ModelViewSet):
    queryset = models.SensorData.objects.all()
    serializer_class = Serializers.SensorDataSerializer

    def update_actuators_based_on_sensor(self, sensor_data):
        print("----------------------------------")
        # Example logic to update actuators
        # logic for temperture
        if sensor_data.temperature > 30:
            models.FanState.objects.update_or_create(
                defaults={'state':True}
            )
            models.HeaterState.objects.update_or_create(
                defaults={'state':False}
            )
            
        else:
            models.FanState.objects.update_or_create(
                defaults={'state': False}
            )
            models.HeaterState.objects.update_or_create(
                defaults={'state':True}
            )
        # Logic for light
        if sensor_data.lightLevel < 50:
            models.LightState.objects.update_or_create(
                defaults={'state':True}
            )
            models.ShadeState.objects.update_or_create(
                defaults={'state':False}
            )
        else:
            models.LightState.objects.update_or_create(
                defaults={'state':False}
            )
            models.ShadeState.objects.update_or_create(
                defaults={'state':True}
            )
        # Logic for Humidity
        if sensor_data.humidity < 50:
            models.MistState.objects.update_or_create(
                defaults={'state':True}
            )
        else:
            models.MistState.objects.update_or_create(
                defaults={'state': False}
            )

        if sensor_data.soilMoisture > 30:
            models.WaterPumpState.objects.update_or_create(
                defaults={'state':True}
            )
            models.WaterState.objects.update_or_create(
                defaults={'state':True}
            )       
        else:
            models.WaterPumpState.objects.update_or_create(
                defaults={'state':False}
            )
            models.WaterState.objects.update_or_create(
                defaults={'state':False}
            )

        if sensor_data.temperature > 30:
            models.FanState.objects.update_or_create(
                defaults={'state':True}
            )
        else:
            models.FanState.objects.update_or_create(
                defaults={'state': False}
            )

        if sensor_data.temperature > 30:
            models.FanState.objects.update_or_create(
                defaults={'state':True}
            )
        else:
            models.FanState.objects.update_or_create(
                defaults={'state': False}
            )

        if sensor_data.temperature > 30:
            models.FanState.objects.update_or_create(
                defaults={'state':True}
            )
        else:
            models.FanState.objects.update_or_create(
                defaults={'state': False}
            )
            
        # Add more logic for other actuators based on sensor data

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        # Verify the response data structure
        print("Response Data:", response.data['url'].rstrip('/').split('/')[-1])
        # Use the correct key to access the ID
        sensor_data_id = response.data['url'].rstrip('/').split('/')[-1]
        print('*************************************',sensor_data_id)
        if sensor_data_id is not None:
            print('*************************************')
            new_sensor_data = models.SensorData.objects.get(pk=sensor_data_id)
            self.update_actuators_based_on_sensor(new_sensor_data)
        return response

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
    serializer_class = Serializers.ShadeStateSerializer  # Updated to correct serializer

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
