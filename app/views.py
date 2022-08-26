import requests
from django.db.models import Q
from django.http import HttpRequest

from django.shortcuts import render
from django.views.generic import ListView

from .forms import CityForm
from .models import City


def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=9c47ebcfb0f166925f28ce8ebb7af75f'

    if request.method=='POST':
        form=CityForm(request.POST)
        form.save()
        print(request.POST)

    form=CityForm()
    all_cities = City.objects.all()
    weather_list = []

    for city in all_cities:
        req = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temperature': req['main']['temp'],
            'description': req['weather'][0]['description'],
            'icon': req['weather'][0]['icon'],
        }

        weather_list.append(city_weather)

    q = request.GET.get("search")
    if q:
        all_cities = all_cities.filter(name__contains=q)
    context={'weather_list':weather_list,'form':form,"city_qs": all_cities}
    return render(request,'app/weather.html',context)



# class CityList(ListView):
#     model = City
#     queryset = City.objects.all()
#     template_name: str = 'app/weather.html'
#     context_object_name = "cities"
#     paginate_by = 6
#
#     def get_context_data(self, **kwargs):
#         qs = super().get_queryset()
#         q = self.request.GET.get("search")
#         if q:
#             context = super().get_context_data(**kwargs)
#             return context
#