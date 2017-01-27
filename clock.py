import pygame, sys, os
import datetime
import pytz
import weather

from pygame.locals import *
os.environ["SDL_FBDEV"] = "/dev/fb1"

font_color = (224, 224, 224)
TICK_EVENT = USEREVENT + 1
pygame.time.set_timer(TICK_EVENT, 1000)
WEATHER_EVENT = TICK_EVENT + 1
pygame.time.set_timer(WEATHER_EVENT, 60 * 60 * 1000)

current_wather = weather.get_weather('asuncion')

pygame.init()
pygame.mouse.set_visible(False)

# set up the window
DISPLAYSURF = pygame.display.set_mode((320, 240), 0, 32)
BCK = pygame.image.load("images/night.png")

font = pygame.font.Font("fonts/amatic.ttf", 124)
weather_font = pygame.font.Font("fonts/amatic.ttf", 20)

def draw_clock():
    now = datetime.datetime.now(pytz.timezone('America/Santiago'))
    label = font.render("{:02d}:{:02d}:{:02d}".format(now.hour, now.minute, now.second), True, font_color)
    DISPLAYSURF.blit(BCK, (0, 0))
    DISPLAYSURF.blit(label, (30, 50))

    weather_label = weather_font.render("{} C".format(current_wather), True, font_color)
    DISPLAYSURF.blit(weather_label, (5, 5))

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == WEATHER_EVENT:
            current_wather = weather.get_weather('asuncion')
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
