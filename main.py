import pygame as pg
import sys
from os import path
from constants import *
from classes import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 80) # repeat key and speed between  the press  500 represent 0.5 second
        self.load_data() 

    def load_data(self): # later on 
        game_folder =  path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        self.map_data = []
        with open(path.join(game_folder, 'gamemap.tkt'), 'rt') as f:
            for line in f :
                self.map_data.append(line)
        self.player_img = pg.image.load(path.join(img_folder ,PLAYER_IMG)).convert_alpha()
        self.wall_img = pg.image.load(path.join(img_folder ,WALL_IMG)).convert_alpha()
        self.wall_img = pg.transform.scale(self.wall_img, (TILESIZE, TILESIZE))

         

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        for row, tiles in enumerate(self.map_data): # enumerate got me the key to read the index, items in the list
            for col, tile in enumerate(tiles):
                if tile == '1': # so if 1 then tile = wall col & row 
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit() # seems that we cant use sys.exit directly, need to exit pygame first using pygame.quit

    def update(self):
        """update portion of the game loop"""
        self.all_sprites.update()

    def draw_grid(self):
        """ we define our grid settings here """
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, RED, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, RED, (0, y), (WIDTH, y))      

    def draw(self):
        """ draw our background, grid and all sprites """
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        # catch all events/inputs here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=1)

    def show_start_screen(self):  # I will make a start menu and a pause menu
        pass

    def show_go_screen(self): # later on
        pass

# create all the game objects needed
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()