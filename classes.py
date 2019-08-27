import pygame as pg
from constants import *
from tilemap import collide_hit_rect
vec = pg.math.Vector2

"""  
All the objects for the game are defined in this file, as the title mentionned
Only classes are shown in classes.py
! vec = pg.math.Vector2 is an important import for our game and is needed in mostly all objects
 
"""

# collision function    
def collide_with_walls(sprite, group, dir):
    """ 
    defined dir for direction as an argument inside collide_with_walls
    if  Sprite hit and Sprite velocity x or y is > 0
    vel x or y  = hit[velocity you want] left right
    repeat for top and bottom of the rect that represent the Sprite
    now vel is set to 0
    vel is shown in most of the classes : self.vel = vec(0, 0)
    
    """
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if sprite.vel.x > 0:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
            if sprite.vel.x < 0:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if sprite.vel.y > 0:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2
            if sprite.vel.y < 0:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y

class Player(pg.sprite.Sprite):
    """  Player class   
    __init the class argument self, game, x, y for the pos
    add to group all_sprites then __init__ self with self.groups
    define all paramater needed
    UPPERCASE arguments can be changed in constants.py
    
    """
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.vel = vec(0, 0)
        self.pos = vec(x, y)
        self.rot = 0
        self.rot_speed = 0
        self.health = PLAYER_HEALTH
        self.point = PLAYER_POINT
        self.x = x
        self.y = y

    def get_keys(self):
        """ get_keys for input from player
        doc about key input in pygame
        https://www.pygame.org/docs/ref/key.html
        """
        self.rot_speed = 0
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rot_speed = PLAYER_ROT_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rot_speed = -PLAYER_ROT_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel = vec(PLAYER_SPEED, 0).rotate(-self.rot)
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel = vec(-PLAYER_SPEED / 2, 0).rotate(-self.rot)

    def update(self):
        """ update Player sprite 
        all actions done by the player as : pos, vel and collision
        collide with wall defined above for the collision with walls sprite
        if player health is = 0 then our sprite should be .kill()
        """
        self.get_keys()
        self.rot = (self.rot + self.rot_speed * self.game.dt) % 360
        self.image = pg.transform.rotate(self.game.player_img, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center
        if self.health <= 0:
            self.kill()

    def add_point(self, amount):
        """ When our player pick up items those items add point to a counter called MAX PLAYER POINT
        each item is = to 1 points if all points collected so 3 points since 3 items are displayed
        the MAX_PLAYER_POINT can be 3 maximum to add each point to this counter this function as 
        been implemented
        """
        self.point += amount
        if self.point > MAX_PLAYER_POINT:
            self.point = MAX_PLAYER_POINT

class Guardian(pg.sprite.Sprite):
    """  Guardian class
    The guardian represent the ennemie mob of the game
    almost same paramaters for him
    however the guardian has to be static since it's a request for the project
    the guardian almost have a self.health which is not used but can be
    the set up of the first function stay the same for all the class
    self.groups = add our new group
    init the Sprite groups
    self.game = game
    """
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.guardian
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.guardian_img
        self.rect = self.image.get_rect()
        self.hit_rect = GUARDIAN_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.rect.center = self.pos
        self.health = GUARDIAN_HEALTH

    def update(self):
        """ update Guardian Sprite during game
        the guardian also own collide_with_walls function but doesnt move
        you can re use the same paramater of player and then make him move as an npc/mob
        for the project it has to be static and unable to move
        """
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center
       
        
class Wall(pg.sprite.Sprite):
    """ define the wall
    to fit the tile rect.x and y need to be * by TILESIZE
    """
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Obstacle(pg.sprite.Sprite):
    """ Same as the class wall but for any obstacle that might be introduced in the game
    since it have the same properties it have been added to the group .walls
    """
    def __init__(self, game, x, y, w, h):
        self.groups = game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

class Item(pg.sprite.Sprite):
    """ Defined the collectable Items in the game
    they are 3 in total and all of them are niched in this class with a type for each
    we need to use brackets [type] for this argument since we use a dictionnary to nich each type and image in 
    a dictionnary placed in constants.py
    type = key of the dictionnary and value = image of the items
    """
    def __init__(self, game, pos, type):
        self.groups = game.all_sprites, game.items
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.item_images[type]
        self.rect = self.image.get_rect()
        self.type = type
        self.rect.center = pos
        self.pos = pos
