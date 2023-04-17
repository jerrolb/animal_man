import pygame

INITIAL_MAP = [
  [1, 1, 2, 1, 1, 1, 1, 2, 1, 1],
  [1, 5, 2, 2, 2, 2, 2, 2, 2, 1],
  [1, 2, 1, 1, 2, 2, 1, 1, -2, 1],
  [1, 2, 1, 2, 2, 2, 2, 1, 2, 1],
  [2, 2, 2, 2, 1, 1, 2, 2, 2, 2],
  [1, 2, 1, 2, 2, 2, 2, 1, 2, 1],
  [1, -1, 1, 1, 2, 2, 1, 1, 2, 1],
  [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
  [1, 1, 2, 1, 1, 1, 1, 2, 1, 1],
]

MAP = [row[:] for row in INITIAL_MAP]

MAP_WIDTH = len(MAP[0])
MAP_HEIGHT = len(MAP)

TILE_SIZE = 32
SCREEN_WIDTH = MAP_WIDTH * TILE_SIZE
SCREEN_HEIGHT = MAP_HEIGHT * TILE_SIZE

FREE = 0
WALL = 1
TREAT = 2
ENEMY = 3
ENEMY_TREAT = 4
PLAYER = 5
ENEMY1 = -1
ENEMY2 = -2

TREATS = 47

UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)
NONE = (0, 0)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (150, 75, 0)

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

MOVE_ENEMY = pygame.USEREVENT + 2
ENEMY_SPEED_INTERVAL = 1000

cat = pygame.image.load("assets/images/cat.png")
CAT = pygame.transform.scale(cat, (TILE_SIZE, TILE_SIZE))
dog1 = pygame.image.load("assets/images/dog1.png")
DOG1 = pygame.transform.scale(dog1, (TILE_SIZE, TILE_SIZE))
dog2 = pygame.image.load("assets/images/dog2.png")
DOG2 = pygame.transform.scale(dog2, (TILE_SIZE, TILE_SIZE))
treat = pygame.image.load("assets/images/treat.png")
TREAT_IMG = pygame.transform.scale(treat, (TILE_SIZE / 4, TILE_SIZE / 4))

def draw_dog(target_rect, image):
  SCREEN.blit(image, target_rect)

def draw_cat(target_rect):
  SCREEN.blit(CAT, target_rect)

def draw_circle(row, col, screen):
  screen.blit(TREAT_IMG, (col * TILE_SIZE + TILE_SIZE // 2 - TREAT_IMG.get_height() / 2, row * TILE_SIZE + TILE_SIZE // 2 - TREAT_IMG.get_width() / 2))

TILE_MAP = {
  FREE: (BLACK, None),
  WALL: (BROWN, None),
  TREAT: (BLACK, draw_circle),
  ENEMY: (None, draw_dog),
  ENEMY1: (None, draw_dog),
  ENEMY2: (None, draw_dog),
  ENEMY_TREAT: (None, draw_dog),
  PLAYER: (None, draw_cat)
}

FPS = 90