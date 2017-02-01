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
        self.data = {}

    def refresh(self):
        try:
            url = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric"
            response = urllib2.urlopen(url.format(self.city, settings.WEATHER_APIKEY))
            data = json.load(response)
            self.data = {'temp': data['main']['temp'], 'icon': data["weather"][0]["icon"]}
        except:
            print("Couldn't get Weather info")

    def get_temp(self):
        return self.data.get('temp', 0)

    def get_icon_image(self):
        try:
            url = "http://openweathermap.org/img/w/{}.png"
            image_str = urlopen(url.format(self.data['icon'])).read()
            picture = pg.image.load(io.BytesIO(image_str))
            picture = pg.transform.scale(picture, (80, 80))
            return picture
        except:
            return None
