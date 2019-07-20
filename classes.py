import pygame
import main *


class Player(pygame.sprite.Sprites):
    """ I define the player as an object( a sprite ) """
    def __init__(self):
        pygame.sprite.Sprites.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN) 
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        
        
class Guardian(pygame.sprite.Sprites):
    """ I define also the guardian as a sprite, but a static one"""
    """ if in the future i want him to move I can re use this class """
    def __init__(self):
        pygame.sprite.Sprites.__init__(self)
        self.image = pygame.Surface((50, 50))



            
