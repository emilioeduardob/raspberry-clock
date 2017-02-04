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
from clock import Clock
os.environ["SDL_FBDEV"] = "/dev/fb1"

font_color = (224, 224, 224)
TICK_EVENT = USEREVENT + 1
pygame.time.set_timer(TICK_EVENT, 1000)
WEATHER_EVENT = TICK_EVENT + 1
pygame.time.set_timer(WEATHER_EVENT, 15 * 60 * 1000)

weather = weather.Weather('asuncion')
weather.refresh()
clock = Clock(weather)

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == WEATHER_EVENT:
            weather.refresh()
        if event.type == TICK_EVENT:
            clock.draw_clock()
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
