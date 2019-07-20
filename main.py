import pygame
import random

WIDTH = 1200
HEIGHT = 600
FPS = 30

# define all colors needed
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):
    #sprite for the Player BTW now the player is only a green square on purpose 
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)


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
