#settings
import pygame as pg
# game options/settings
TITLE = "Geopython"
ICON = "images.ico"
FONT = 'consolas'
WIDTH = 1200
HEIGHT = 600
FPS = 60
GAME_SPEED = 7.5
# Player proprieties
PLAYER_ACC = 0.98
PLAYER_FRICTION = -0.12
JUMPFORCE = -20
# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHTGREEN = (0, 100, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)

TOTALMAPS = 2

TILESIZE = 60
GRIDWITH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE