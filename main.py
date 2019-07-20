import pygame
from os import path
from classes import  *
from constants import *

# initialize pygame and create a window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Macgyver escape the maze")
clock = pygame.time.Clock()

# group all the sprites using .Group
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game main loop
running = True
while running:
    # keep loop running at the right speed ( Fram Per Second)
    clock.tick(FPS)
    # Process input (events are inputs)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update all the sprites
    all_sprites.update()

    # Draw & render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # after drawing everything it gonna flip the display
    pygame.display.flip()

pygame.quit()
