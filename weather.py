import urllib2
import json
import settings

def get_weather(city):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric"
    response = urllib2.urlopen(url.format(city, settings.WEATHER_APIKEY))
    data = json.load(response)
    return data['main']['temp']
