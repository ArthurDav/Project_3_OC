# /python3
# -*- coding: Utf-8 -*

import  pygame
from pygame.locals import *
import os
import sys
import random



""" Game Macgyver, main file game files/scripts : macgyver.py, constant.py, classes.py  """

# define colors needed in the game
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGRAY = (40, 40, 40)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# define settings
WIDTH = 1024 # or 32 * 32
HEIGHT = 768  # or 32 * 24
FPS = 30
TITLE = "Macgyver escape the maze!"
BG_COLOR = DARKGRAY

TILESIZE = 32
GRID_WIDTH = WIDTH / TILESIZE
GRID_HEIGHT = HEIGHT / TILESIZE

#initialize pygame and set up
pygame.init()
CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode(((WIDTH, HEIGHT)))
pygame.display.set_caption(' MacGyver ESCAPE THE MAZE ')

ALL_SPRITES = pygame.sprite.Group()





# game main loop  - game stay open or endgame if player quit
RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        

    pygame.display.update()

    pygame.quit()
