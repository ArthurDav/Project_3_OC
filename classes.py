import pygame as pg
from constants import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self. health = PLAYER_HEALTH
    

    def move(self, dx=0, dy=0):
        if not self.wall_collision(dx, dy): # you can move if not colision with the walls
            self.x += dx
            self.y += dy
        

    def wall_collision(self, dx=0, dy=0):
        for wall in self.game.walls:
            if  wall.x == self.x + dx and wall.y == self.y + dy:
                return True # we did collide
        return False # we did not collide


    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Guardian(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.guardian
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = GUARDIAN_IMG
        self.image = game .guardian_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game .wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Wall2(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = WALL2_IMG
        self.image = game .wall2_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Item(object):

    class Aiguille(pg.sprite.Sprite):
        def __init__(self, game, x, y):
            self.groups = game.all_sprites, game.items
            pg.sprite.Sprite.__init__(self,self.groups)
            self.game = game
            self.image = AIGUILLE
            self.image = game .aiguille_img
            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
    
    class tube_plastique(pg.sprite.Sprite):
        def __init__(self, game, x, y):
            self.groups = game.all_sprites, game.items
            pg.sprite.Sprite.__init__(self, self.groups)
            self.game = game
            self.image = TUBE_PLASTIQUE
            self.image = game.tube_plastique_img
            self.rect = self.image.get_rect()
            self.x = x 
            self.y = y
            
    class seringue(pg.sprite.Sprites):
        def __init__(self, game, x, y):
            self.groups = game.all_sprites, game.items
            pg.sprite.Sprite.__init__(self, self.groups)
            self.game = game
            self.image = SERINGUE
            self.image = game.seringue_img
            self.rect = self.image.get_rect()
            self.x = x 
            self.y = y

    class ether(pg.sprite.Sprite):
        def __init__(self, game, x ,y):
            self.groups = game.all_sprites, game.items
            pg.sprite.Sprite.__init__(self, self.groups)
            self.game = game
            self.image = ETHER
            self.image = game.ether_img
            self.rect = self.image.get_rect()
            self.x = x 
            self.y = y

        