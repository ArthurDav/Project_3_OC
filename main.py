import pygame as pg
import sys
from os import path
from constants import *
from classes import *
from tilemap import *

# Draw player health
def draw_player_health(surf, x, y, pct):
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

class Game:
    """  Main class for the game/loading/ main loop / new_game / run / quit """
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()
        self.font_name = pg.font.match_font(FONT_NAME)

    #load main data
    def load_data(self):
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
        # initialize all variables  etc and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.guardian = pg.sprite.Group()
        self.items = pg.sprite.Group()
        self.map = TiledMap(path.join(self.map_folder, 'map.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.camera = Camera(self.map.width, self.map.height)
        for tile_object in self.map.tmxdata.objects:
            obj_center = vec(tile_object.x + tile_object.width / 2,
                             tile_object.y + tile_object.height / 2)
            if tile_object.name == 'player':
                self.player = Player(self, obj_center.x, obj_center.y)
            if tile_object.name == 'guardian':
                Guardian(self, obj_center.x, obj_center.y)
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y,
                         tile_object.width, tile_object.height)
            if tile_object.name in ['item1', 'item2', 'item3']:
                Item(self, obj_center, tile_object.name)
# self.player = Player(self, 2, 3) spwan object using coordinates

    def run(self):
        # game loop - set self.playing = False to end the game / True keep playing
        self.playing = True
        while self.playing:
            # Explain  DT !!!
            self.dt = self.clock.tick(FPS) / 1000.0  # fix for Python 2.x
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update th whole portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)
        # colilision between 2 group, PLayer & Guardian or other 
        hits = pg.sprite.spritecollide(self.player, self.guardian, False, collide_hit_rect)
        for hit in hits:
            self.player.health -= GUARDIAN_DAMMAGE
            if self.player.health <= 0:
                g.show_go_screen()
                self.playing = False 
            if self.player.point == MAX_PLAYER_POINT:
                hit.kill()
                g.quit()
                
        # player hit items
        hits = pg.sprite.spritecollide(self.player, self.items, False, collide_hit_rect)
        for hit in hits:
            if hit.type == 'item1' and self.player.point < MAX_PLAYER_POINT:
                self.player.add_point(ITEM1_POINT_AMOUNT)
                hit.kill()
            if hit.type == 'item2' and self.player.point < MAX_PLAYER_POINT:
                self.player.add_point(ITEM3_POINT_AMOUNT)
                hit.kill()
            if hit.type == 'item3' and self.player.point < MAX_PLAYER_POINT:
                self.player.add_point(ITEM2_POINT_AMOUNT)
                hit.kill()

    """def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))"""

    def draw(self):
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps())) # fps 
        #self.screen.fill(BGCOLOR)
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        #self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        # pg.draw.rect(self.screen, WHITE, self.player.hit_rect, 2)

        # HEALTH HUD 
        draw_player_health(self.screen, 25, 30, self.player.health / PLAYER_HEALTH)       
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

    def show_start_screen(self): # will implement later
        self.screen.fill(RED)
        self.draw_text(TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Macgyver Escaping the MAZE ", 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press a key to play ", 22, GREEN, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        self.screen.fill(BLACK)
        self.draw_text('GAMEOVER', 48, RED, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Press a key 2 times to play again ", 22, RED, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
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
