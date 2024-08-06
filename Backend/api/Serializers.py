from rest_framework import serializers
from . import models 

class SensorDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.SensorData
        fields = '__all__'

class FanStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.FanState
        fields = '__all__'

class WaterStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.WaterState
        fields = '__all__'

class LightStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.LightState
        fields = '__all__'

class ShadeStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ShadeState
        fields = '__all__'

class FertilizerStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.FertilizersState
        fields = '__all__'

class MistStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MistState
        fields = '__all__'

class WaterPumpStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.WaterPumpState
        fields = '__all__'

class HeaterStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.HeaterState
        fields = '__all__'

