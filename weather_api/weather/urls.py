# weather/urls.py

from django.urls import path
from .views import get_weather_data

urlpatterns = [
    path('get_weather_data/', get_weather_data, name='get_weather_data'),
]
