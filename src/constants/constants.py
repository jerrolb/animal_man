import pygame
import pygame_gui
from .maps import *

TILE_SIZE = 80

UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)
NONE = (0, 0)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (150, 75, 0)
LIGHT_BROWN = (230, 200, 170)

FREE = 0
WALL = 1
TREAT = 2
ENEMY = 3
ENEMY_TREAT = 4
PLAYER = 5
ENEMY1 = -1
ENEMY2 = -2

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
MOVEMENT_SURFACE = pygame.Surface((TILE_SIZE, TILE_SIZE))
UI = pygame_gui.UIManager(SCREEN.get_size())

MOVE_ENEMY = pygame.USEREVENT + 2

FPS = 90

ENEMY_SPEED_MAP = {
  'Easy': 1000,
  'Medium': 500,
  'Hard': 300,
  'Expert': 200,
  'Expert+': 100,
}

DIFFICULTY_TO_TREATS = {
  'Easy': 100,
  'Medium': 200,
  'Hard': 400,
  'Expert': 800,
  'Expert+': 1600,
}