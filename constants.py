# define all colors needed
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
LIGHTGREY = (100, 100, 100) # I needed a light greyish color to draw the grid and defined the tile properly
DARKGREY = (40, 40, 40) # then our background

WIDTH = 1024 # 32 * 32
HEIGHT = 768  # 32 * 24
TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

FPS = 30
TITLE = "Macgyver espace the maze"
BGCOLOR = DARKGREY

PLAYER_IMG = 'macgyver.png'
WALL_IMG = 'wall.png'
FLOOR_IMG = 'floor.png'