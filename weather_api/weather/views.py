# weather/views.py

from django.shortcuts import render
from .models import WeatherData

def get_weather_data(request):
    # Lógica para obter os dados do tempo (substitua pelos seus dados reais)
    temperature = 25.5
    pressure = 1013.2
    humidity = 65.0
    precipitation = 10.0
    condition = "Ensolarado"

    # Salva os dados no banco de dados
    WeatherData.objects.create(
        temperature=temperature,
        pressure=pressure,
        humidity=humidity,
        precipitation=precipitation,
        condition=condition
    )

    # Renderiza o template com os dados do tempo
    context = {
        'temperature': temperature,
        'pressure': pressure,
        'humidity': humidity,
        'precipitation': precipitation,
        'condition': condition,
    }
    return render(request, 'weather/weather_data.html', context)
