import random
import sys
from os import path
import pygame as pg
from constants import *
from classes import *
from tilemap import *

"""
OC project number 3
python 3.7.3
UTF-8
Versionning : 1.0 Stable
Non previous versionning have been made (Master ----> Master only)
!! all UPPERCASE VARIABLES are located in constants.py !!
pygame as pg
Tile Game based
libraries :
pygame --> doc --> https://www.pygame.org/docs/
random --> doc --> https://docs.python.org/3/library/random.html
Pygame
Used modules:
pygame.Sprite
https://www.pygame.org/docs/ref/sprite.html
pygame.Rect
https://www.pygame.org/docs/ref/rect.html
pygame.Surface
https://www.pygame.org/docs/ref/surface.html
pygame.event
https://www.pygame.org/docs/ref/event.html
-----------------------------------------------Overall of the gamefolder-----------------------------------
/img
contain all images graphicals elements of the games as ..:
    guardian.png
    macgyver.png
    item1.png
    item2.png
    item3.png
    wall.png
/maps
contain graphical elements for the map of the game :
!USE A TMX MAP EDITOR TOO EDIT THE FILES!
    floortile.tsx
    guardian.tsx
    map.tmx  ! PRESIZED RAW SAMPLE !
    maps.tmx
    tilewall.tsx
/__pycache__
containing Python 3 bytecode compiled.
Keeping this help python to launch the program faster
You can prevent the creation of this file iw you wish using PYTHONDONTWRITEBYTECODE
You can find more about there -->
https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE
main.py
    contain main class/func to launch the game
    main loop
    Game setting/propers
classes.py
    all Class/Objects as the player, floor etc
    Collision function
constants.py
    contain all variables and constant data / properties
tilemap.py
    contain the class Map for map data reading, Tile render
    contain the class Camera for the Camera functionnality
-----------------------------------------------Overview of main.py-----------------------------------
def draw_player_health
    Global function that draw the player's health on screen
def draw_score
    Global function that draw player's score at the midtop position of the screen
Class Game
    This is the main class of the game.
    Inside you'll find all functions that run the game in this order
    def __init__()
        Initialaze the content and Pygame
    def load_data()
        load all neccessary media, pictures, audio, etc
    def  new()
        all elements needed for a new game
        load all groups of sprites
        Place all objects on the tile of the map
    def run()
        main game loop
        while playing = True then game is running
    def quit()
        quit the game / pygame
    def update()
        all properties that change the game while running are nested inside this funtion.
        Update all the Sprites         self.all_sprites.update()
        You'll find al collision properties and outcome inside update()
    def draw()
        draw elements on the screens as, score, player health, title, game over screen etc
    def events()
    Take the input of pygame.events
    Like player press a key, quit the game etc
    def show_start_screen()
        defined the start screen when you launch the game.
        Font, color, message, string, game rules etc
    def show_go_screen()
        defined the game over screen.
        this screen appear when the player touch the guardian and die
    def wait_for key()
        during our show_start_screen and show_go_screen, we ask the player to press a key
        to go on the next stage. This function is the function that wait for the player input to pass the start/go screen
    def draw_text()
        define  text parameters as font size, color etc
        Used to draw text on the show_start\go_screen
g = Game()
defined the game object.
Since our game parameters are all nested inside the class Game,
think about the game as a gobale object.
"""

# Draw player health
def draw_player_health(surf, x, y, pct):

    """ 
    Defined the player health bar and draw it. We use pct(percentage).
    Fill the BAR lenght * with our current percentage of health.
    Outline our bar with is a rect pg.Rect , we outline it on x y and lenght , height.
    We fill the Rect of the bar  with our x, y, fill defined previously, bar height
        then if my percentage(pct) is superior to 60% (0.6) fill Rect it with a GREEN color
        then if my percentage(pct) is superior to 40% (0.4) fill Rect with YELLOW color
        then if my percentage (pct) is something else fill Rect with RED color
    Then create pg.draw.rect with what we defined above
      """
    if pct < 0:
        pct = 0
    fill = pct * BAR_LENGTH
    outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
    if pct > 0.6:
        col = GREEN
    elif pct > 0.4:
        col = YELLOW
    else:
        col = RED
    pg.draw.rect(surf, col, fill_rect)
    pg.draw.rect(surf, WHITE, outline_rect, 2)

# defined the best font that match your OS using the match_font from Pygame
font_name = pg.font.match_font('arial')

def draw_score(surf, text, size, x, y):
    """ 
Global Function to draw a score at the miptop of the screen
Defined my font, then my text surface
get_rect my surface
place my surface on the midtop of the screen and .blit it 
    """
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE) # True for .render
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

class Game:

    """  
    Main class for the game/loading/ main loop / new_game / run / quit 
    See above main.py overview to check quickly the full content of  the class.
    The class Game has many components build with a logic of 
    Initialize --> Load --> main loop --> new game set up --> run --> update external output --> quit 
    many attributes will be defined outside of __init__
    It's totally fine to use attributes outside of __init__ when those paramaters are niched inside a main class
    like our main class Game: 
    """
    def __init__(self):

        """
        Initialize the game with py.init()
        set up the screen
        set title caption
        set pygame.Clock
        self the loading
        """
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()
        # another font_name is defined above, you can use both
            # the font_name above use a non defined match_font
            # the font_name below can be changed with FONT_NAME in constants.py 
        self.font_name = pg.font.match_font(FONT_NAME)

    def load_data(self):

        """ 
        function to load all the data neccessary as media img audio etc
         Set up the game folder         game_folder = path.dirname(__file__)
         Set up the img folder         img_folder = path.join(game_folder, 'img')
        folders path have been created
        now load all data from those path
        self.item_images is defined a dictionnary and cannot be changed for a list nor tuple
            since our items object are nested in a dictionnary 
        Loop thought each item in ITEMS_IMAGE inside constants.py 
            all items as explained above are nested in a dictionnary called ITEM_IMAGE 
        img can be transformed to be scaled using :
            pg.transform.scale(self.my_img, (MYSIZEX, MYSIZEY))
        """
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        self.map_folder = path.join(game_folder, 'maps')
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.player_img = pg.transform.scale(self.player_img, (TILESIZE, TILESIZE))
        self.guardian_img = pg.image.load(path.join(img_folder, GUARDIAN_IMG)).convert_alpha()
        self.wall_img = pg.image.load(path.join(img_folder, WALL_IMG)).convert_alpha()
        self.wall_img = pg.transform.scale(self.wall_img, (TILESIZE, TILESIZE))
        self.item_images = {}
        for item in ITEMS_IMAGE:
            self.item_images[item] = pg.image.load(path.join(img_folder, ITEMS_IMAGE[item])).convert_alpha()

    def new(self):

        """ 
        new() defined all new data/Objects needed for a new game
    All objects are insed a group
    Each sprites have a group name which make it easier to load them since everything is grouped
    new map defined from the map_folder 'map.tmx'
    creating map rect
    ! self.camera !  all information about the camera properties in Gamefolder/tilemap.py
    Place objects on the map using tile_object.name
    Defined tile name using a tmx editor as Tiled etc """
   
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.guardian = pg.sprite.Group()
        self.items = pg.sprite.Group()
        self.map = TiledMap(path.join(self.map_folder, 'map.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.camera = Camera(self.map.width, self.map.height)
        
        # loop thought all tile_object in the map
        for tile_object in self.map.tmxdata.objects:

            # I'll defined the location/center of each object to place them in the middle of their tile using vec
            # each object  as player/mob etc and have a paramater position self.pos = vec(x, y)
            obj_center = vec(tile_object.x+ tile_object.width / 2,tile_object.y + tile_object.height / 2)
            
            # for the need of this project our items in our game needed to pop at random coordinates
            # random.randrange is used to move the x or the y of the items 
            # x and y are defined using a tiled map editor, it helps to visualize the coordinates
            # I defined a fixed Y position then I can pick a rondom X between coordinates
            # the position of the item is the result of x and y 
            # x1 stand for x of item 1 same for the y
            # x2 stand for x of item 2 same for the y  etc.. for all items
            # some item have a x and a y fixed since they move verticaly or horizontaly only

            # Item 1 position
            x1 = [random.randrange(200, 1001, 100)]
            y1 = [119]
            item1_xy = x1 + y1

        # item 2 position
            x2 = [random.randrange(200, 801, 100)]
            y2 = [597]
            item2_xy = x2 + y2 
 
        # item 3 position
            x3 = [1068]
            y3 = [random.randrange(300, 800 , 100)]
            item3_xy = x3 + y3

            """ if total random pos needed, randint used and working
            rand1 = [random.randint(100, 1000)]
            rand2 = [random.randint(100, 1000)]
            itempos = rand1 + rand2"""

            # from my loop if my tile_object == to my object name
            # then place this object in tile_object.x and y 
            if tile_object.name == 'player':
                self.player = Player(self, obj_center.x, obj_center.y)
            if tile_object.name == 'guardian':
                Guardian(self, obj_center.x, obj_center.y)
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y,
                         tile_object.width, tile_object.height)
            # since our items pop randomly, we replace tile_object.y and y for our coordinates defined above
            #  then tile_object.name to match each item's coordinates              
            if tile_object.name in ['item1']:
                Item(self, item1_xy, tile_object.name)
            if tile_object.name in ['item2']:
                Item(self, item2_xy, tile_object.name)
            if tile_object.name in ['item3']:
                Item(self, item3_xy, tile_object.name)
        
    def run(self):
        """ game loop - set self.playing = False to end the game / True keep playing
        it contain only elements needed to run the game
        Events()
        updates()
        draw()
        ! if you include another func inside the game loop the game will break !
        """
        self.playing = True
        while self.playing:
            # Defined dt as pygame clock tick for timing etc 
            self.dt = self.clock.tick(FPS) / 1000.0  
            self.events()
            self.update()
            self.draw()

    def quit(self):
        """  explicite / quit the game / close the prog """
        pg.quit()
        sys.exit()

    def update(self):
        """  update() as named, update all sprites 
                collision between sprites are niched inside with hits
                the camera option is also updated since our player is moving  
         """
        # update the whole sprites in the game
        # all sprites & sprites group are defined above in new()
        self.all_sprites.update()
        # camera is updated constantly since our player is moving most of the time
        self.camera.update(self.player)

        # collision between 2 types of sprite self.player & self.guardian
        #  Defined some particularities in our loop
        # player.health = GUARDIAN dammage since our guardian will do some dammage .health will change
        # then if player.health = 0, the game will stop it's gameover main loop self.playing= False 
        # if MAX_PLAYER_POINT = to our current point hold by the player acquired when picking the items
        # then we .kill() the sprite to make the Guardian disappear
        hits = pg.sprite.spritecollide(self.player, self.guardian, False, collide_hit_rect)
        for hit in hits:
            self.player.health -= GUARDIAN_DAMMAGE
            if self.player.health <= 0:
                g.show_go_screen()
                self.playing = False 
            if self.player.point == MAX_PLAYER_POINT:
                hit.kill()
                g.quit()
         
        # we defined another collision between Payer and Items
        # the system is my PLayer sprite hit Item sprite
        # when hitting the item we add the item properties (ITEM_POINT_AMOUNT) to our Payer sprite
        # we add the Item properties to our PLayer using self.player.add_point
        # hit.kill() kill the item Sprite after the collision
        hits = pg.sprite.spritecollide(self.player, self.items, False, collide_hit_rect) # False for no hit yet
        for hit in hits:
            if hit.type == 'item1' and self.player.point < MAX_PLAYER_POINT:
                self.player.add_point(ITEM1_POINT_AMOUNT)
                hit.kill()
            if hit.type == 'item2' and self.player.point < MAX_PLAYER_POINT:
                self.player.add_point(ITEM2_POINT_AMOUNT)
                hit.kill()
            if hit.type == 'item3' and self.player.point < MAX_PLAYER_POINT:
                self.player.add_point(ITEM3_POINT_AMOUNT)
                hit.kill()

    def draw(self):
        """ set the UHD on the screen any drawn UHD etc are nested in this function
            most of the code found here was defined above before  class Game:
         """
        pg.display.set_caption(TITLE) # here you can set the caption of the frame
        # screen.blit 
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        # refresh sprite with the camera
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        # draw player's score 
        draw_score(self.screen, str(self.player.point), 30, WIDTH / 2, 20 )
        # HEALTH HUD  
        draw_player_health(self.screen, 25, 30, self.player.health / PLAYER_HEALTH)    
        #update  the whole content of the screen
        pg.display.flip()

    def events(self):
        """catch all events/input from player here"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

    def show_start_screen(self): 
        """ we define a start screen when we launch the game
                at the end wait_for_keys is added since we ask the player to press a key to start
        """
        self.screen.fill(RED)
        self.draw_text(TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Macgyver Escaping the MAZE ", 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press a key to play ", 22, GREEN, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        """ same as above however this screen is the game over one used when PLayer die """
        self.screen.fill(BLACK)
        self.draw_text('GAMEOVER', 48, RED, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Press a key 2 times to play again ", 22, RED, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        """ since we ask to our player to press a key to play when he/she launch the game
                and to press 2 times a key to re pop when died a wait_for_key function has been 
                implemented
                """
        pg.event.wait()
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.quit()
                if event.type == pg.KEYUP:
                    waiting = False

    def draw_text(self, text, size, color, x, y):
        """ to draw text on screen we need to define how the text will look police / size etc """
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

# create the game object 
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()