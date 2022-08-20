import requests

from django.shortcuts import render

def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=9c47ebcfb0f166925f28ce8ebb7af75f'
    city="lasvegas"
    req=requests.get(url.format(city))
    city_weather = {
        'city': city.name,
        'temperature': req['main']['temp'],
        'description': req['weather'][0]['description'],
        'icon': req['weather'][0]['icon'],
    }
    context={'city_weather':city_weather}
    return render(request,'app/weather.html',context)

