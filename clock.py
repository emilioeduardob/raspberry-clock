import pygame, os
from datetime import datetime
import pytz
import weather

from pygame.locals import *
from time import sleep
os.environ["SDL_FBDEV"] = "/dev/fb1"

class Clock():
    FONT_COLOR = (224, 224, 224)

    def __init__(self, weather):
        self.weather = weather
        self.weather_image = weather.get_icon_image()
        self.init_pygame()
        self.setup_fonts()

    def setup_fonts(self):
        self.clock_font = pygame.font.Font("fonts/digital-mono.ttf", 120)
        self.weather_font = pygame.font.Font("fonts/digital-mono.ttf", 38)

    def init_pygame(self):
        pygame.init()
        pygame.mouse.set_visible(False)
        # set up the window
        self.surface = pygame.display.set_mode((320, 240), 0, 32)

    def set_wallpaper(self):
        if (self.is_day()):
            bck = pygame.image.load("images/day.png")
        else:
            bck = pygame.image.load("images/night.png")
        self.surface.blit(bck, (0, 0))

    def is_day(self):
        now = datetime.now()
        return (now > self.weather.sunrise() and now < self.weather.sunset())

    def draw_clock(self):
        self.set_wallpaper()
        now = datetime.now(pytz.timezone('America/Santiago'))
        if (now.second % 2 == 0):
            pattern = "{:02d} {:02d}"
        else:
            pattern = "{:02d}:{:02d}"
        label = self.clock_font.render(pattern.format(now.hour, now.minute), True, self.FONT_COLOR)
        self.surface.blit(label, (20, 80))
        if self.weather_image is not None:
            self.surface.blit(self.weather_image, (0, 0))

        temp = round(self.weather.get_temp())
        weather_label = self.weather_font.render("{0:g} C".format(temp), True, self.FONT_COLOR)
        self.surface.blit(weather_label, (84, 20))
