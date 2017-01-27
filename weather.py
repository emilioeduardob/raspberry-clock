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

class Weather:
    def __init__(self, city):
        self.city = city

    def refresh(self):
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric"
        response = urllib2.urlopen(url.format(self.city, settings.WEATHER_APIKEY))
        data = json.load(response)
        self.data = {'temp': data['main']['temp'], 'icon': data["weather"][0]["icon"]}

    def get_temp(self):
        return self.data['temp']

    def get_icon_io(self):
        url = "http://openweathermap.org/img/w/{}.png"
        image_str = urlopen(url.format(self.data['icon'])).read()
        return io.BytesIO(image_str)
