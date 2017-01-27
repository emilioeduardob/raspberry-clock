import urllib2
import json
import settings
import io
import pygame as pg
try:
    # Python2
    from urllib2 import urlopen
except ImportError:
    # Python3
    from urllib.request import urlopen

def get_weather(city):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric"
    response = urllib2.urlopen(url.format(city, settings.WEATHER_APIKEY))
    data = json.load(response)
    return {'temp': data['main']['temp'], 'icon': data["weather"][0]["icon"]}

def get_icon_image(icon):
    url = "http://openweathermap.org/img/w/{}.png"
    image_str = urlopen(url.format(icon)).read()
    return io.BytesIO(image_str)

