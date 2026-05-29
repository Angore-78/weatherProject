from django.shortcuts import render
from .models import City
import requests

def index(request):
	url='https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=1b3a90d0e878c5aef83f4210c32f5899' 
	cities=City.objects.all()
	city_weather=requests.get(url.format(city)).json()
	for city in cities:
	#print(city_weather) #Temporary view output for json objects representation
		weather={
			'city':city,
			'temprature':city_weather['main']['temp'],
			'description':city_weather['weather'][0]['description'],
			'icon':city_weather['weather'][0]['icon'],
		}
	weather_data.append(weather) #Adds data for selected city into the list of cities
	context={'weather':weather}
	return render(request,'places/index.html',context )
