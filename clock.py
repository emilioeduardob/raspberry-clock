import pygame, sys, os
import datetime
import pytz
import weather
try:
    import buttons
except:
    print "Not running in Raspberry"

from pygame.locals import *
from time import sleep
os.environ["SDL_FBDEV"] = "/dev/fb1"

font_color = (224, 224, 224)
TICK_EVENT = USEREVENT + 1
pygame.time.set_timer(TICK_EVENT, 1000)
WEATHER_EVENT = TICK_EVENT + 1
pygame.time.set_timer(WEATHER_EVENT, 60 * 60 * 1000)

current_weather = weather.Weather('asuncion')
current_weather.refresh()
weather_image = pygame.image.load(current_weather.get_icon_io())

pygame.init()
pygame.mouse.set_visible(False)

# set up the window
DISPLAYSURF = pygame.display.set_mode((320, 240), 0, 32)
BCK = pygame.image.load("images/night.png")

font = pygame.font.Font("fonts/amatic.ttf", 124)
weather_font = pygame.font.Font("fonts/amatic.ttf", 42)

def draw_clock():
    now = datetime.datetime.now(pytz.timezone('America/Santiago'))
    label = font.render("{:02d}:{:02d}:{:02d}".format(now.hour, now.minute, now.second), True, font_color)
    DISPLAYSURF.blit(BCK, (0, 0))
    DISPLAYSURF.blit(label, (30, 50))
    DISPLAYSURF.blit(weather_image, (40, 5))

    temp = round(current_weather.get_temp())
    weather_label = weather_font.render("{0:g} C".format(temp), True, font_color)
    DISPLAYSURF.blit(weather_label, (5, 5))

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == WEATHER_EVENT:
            current_weather.refresh()
            weather_image = pygame.image.load(weather.get_icon_image())
        if event.type == TICK_EVENT:
            draw_clock()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Pos: %sx%s\n" % pygame.mouse.get_pos())
            if box.collidepoint(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit()
    pygame.display.update()
    sleep(0.1)
