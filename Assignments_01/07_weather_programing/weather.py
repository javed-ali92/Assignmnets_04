import requests
from pprint import pprint

API_key = 'a66123c65d244efc512035d9acbb75c2'

city = input('Enter a city:')

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)