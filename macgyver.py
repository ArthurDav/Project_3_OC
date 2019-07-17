#!/usr/bin/python3
# -*- coding: Utf-8 -*

""" Game Macgyver, main file """
""" game files/scripts : macgyver.py, constant.py, classes.py  """

import  pygame
from pygame.locals import *
import os
import sys

pygame.init()
# frame set up
game_display = pygame.display.set_mode((600, 600))
# game title displayed
pygame.display.set_caption('/MacGyver/ ESCAPE THE MAZE')
# internal clock might be used for events
clock = pygame.time.Clock()

# game main loop  - game stay open or endgame if player quit
endgame = False
while not endgame :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            endgame = True
        print(event)

    pygame.display.update()

pygame.quit()