import pygame as pg
import sys
import random
from os import path
from constants import *
from classes import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(300, 80) # repeat key and speed between  the press  300 represent 0.3 s
        self.load_data() 
        self.font_name = pg.font.match_font(FONT_NAME)

    def load_data(self): # later on
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        self.map_data = []
        with open(path.join(game_folder, 'gamemap.tkt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)

        self.player_img = pg.image.load(path.join(img_folder , PLAYER_IMG)).convert_alpha()
        self.player_img = pg.transform.scale(self.player_img, (TILESIZE, TILESIZE))

        self.guardian_img = pg.image.load(path.join(img_folder , GUARDIAN_IMG)).convert_alpha()
        self.guardian_img = pg.transform.scale(self.guardian_img, (TILESIZE, TILESIZE))

        self.wall_img = pg.image.load(path.join(img_folder, WALL_IMG)).convert_alpha()
        self.wall_img = pg.transform.scale(self.wall_img, (TILESIZE, TILESIZE))

        self.wall2_img = pg.image.load(path.join(img_folder, WALL2_IMG)).convert_alpha()
        self.wall2_img = pg.transform.scale(self.wall2_img, (TILESIZE, TILESIZE))
        

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.wall2 = pg.sprite.Group()
        self.guardian = pg.sprite.Group()
        self.items = pg.sprite.Group()
        for row, tiles in enumerate(self.map_data): #u enumerate got me the key to read the index, items in the list
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == '2':
                    Wall2(self, col, row)
                if tile == 'G':
                    Guardian(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
                


                
    def run(self):
        # game loop - set self.playing = False to end the game
        game_over = True
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
        #self.draw_grid()
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

                if  self.player.health == 0:
                    self.playing = False 

    def show_start_screen(self):  # I will make a start menu and a pause menu
        self.screen.fill(START_BG_COLOR)
        self.draw_text(TITLE, 40, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Arrows to move, get all the items to leave the maze", 24, WHITE, WIDTH / 2, HEIGHT / 2 )
        self.draw_text("Press a key to play", 26, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key_press()

    def show_go_screen(self): # later on
        pass 

    def wait_for_key_press(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                if event.type == pg.KEYUP:
                    waiting = False

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

# create all the game objects needed
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()

print(*map_data)