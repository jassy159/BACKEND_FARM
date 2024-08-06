from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views
router = DefaultRouter()
router.register(r'sensordata',views.SensorDataView)
router.register(r'fanstate',views.FanStateView)
router.register(r'waterstate',views.WaterStateView)
router.register(r'lightstate',views.LightStateView)
router.register(r'shadestate',views.ShadeStateView)
router.register(r'fertilizerstate',views.FertilizersStateView)
router.register(r'miststate',views.MistStateView)
router.register(r'waterpumpstate',views.WaterPumpView)
router.register(r'heaterstate',views.HeaterStateView)


urlpatterns = [

    path('',include(router.urls))
]