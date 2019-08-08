import pygame as pg
from constants import *
import pytmx

"""  tilemap.py is the file that link our map.tmx to the game and also niche the Camera option
the map has been created using Tiled a software for tile map editing
doc --> https://doc.mapeditor.org/en/stable/

A Map and a Tile Map are different there is 2 class for each of them

!!!! to load the tile map you will need to import pytmx 
doc --> https://github.com/bitcraft/PyTMX
https://pypi.org/project/PyTMX/     
"""

def collide_hit_rect(one, two):
    """ collide two rect for collision """
    return one.hit_rect.colliderect(two.rect)

class Map:
    """ init the map with self and our filename
            loop to add each line and defined tile size height and width
            if any modification are hard please check above the pytmx doc
            the sample and set up of our map is the same than the documentation
     """
    def __init__(self, filename):
        """ init the Map !! and not the TileMap """  
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE

class TiledMap:
    """  defined the Tilemap of the game 
    Define width & height for the tiles
    """
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

    def render(self, surface):
        """ render visible layers """
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth,
                                            y * self.tmxdata.tileheight))

    def make_map(self):
        """ map surface rendering """
        temp_surface = pg.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface

class Camera:
    """  A camera function as been implemented to make more immersion in the game
    doc about camera in pygame : https://www.pygame.org/docs/tut/CameraIntro.html
    """
    def __init__(self, width, height):
        """ initialize the camera  """
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        """ return the movement of the entity followed, move the camera """
        return entity.rect.move(self.camera.topleft)

    def apply_rect(self, rect):
        """ same as above for rect """
        return rect.move(self.camera.topleft)

    def update(self, target):
        """ update x y position of the target """
        x = -target.rect.centerx + int(WIDTH / 2)
        y = -target.rect.centery + int(HEIGHT / 2)

        # limit scrolling to map size
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.width - WIDTH), x)  # right
        y = max(-(self.height - HEIGHT), y)  # bottom
        self.camera = pg.Rect(x, y, self.width, self.height)