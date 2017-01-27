import pygame, sys, os
import datetime
import pytz
from pygame.locals import *
os.environ["SDL_FBDEV"] = "/dev/fb1"

font_color = (224, 224, 224)
TICK_EVENT = USEREVENT + 1
pygame.time.set_timer(TICK_EVENT, 1000)

pygame.init()
pygame.mouse.set_visible(False)

# set up the window
DISPLAYSURF = pygame.display.set_mode((320, 240), 0, 32)
BCK = pygame.image.load("images/night.png")

#font = pygame.font.Font("fonts/jersey.ttf", 52)
font = pygame.font.SysFont("arial", 52)
#label = font.render("22:24", True, font_color)
#DISPLAYSURF.blit(label, (100, 100))


# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == TICK_EVENT:
            now = datetime.datetime.now(pytz.timezone('America/Santiago'))
            label = font.render("{:02d}:{:02d}:{:02d}".format(now.hour, now.minute, now.second), True, font_color)
            DISPLAYSURF.blit(BCK, (0, 0))
            DISPLAYSURF.blit(label, (25, 100))
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Pos: %sx%s\n" % pygame.mouse.get_pos())
            if box.collidepoint(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit()
    pygame.display.update()

