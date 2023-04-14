import pygame

INITIAL_MAP = [
  [1, 1, 2, 1, 1, 1, 1, 2, 1, 1],
  [1, 5, 2, 2, 2, 2, 2, 2, 2, 1],
  [1, 2, 1, 1, 2, 2, 1, 1, 4, 1],
  [1, 2, 1, 2, 2, 2, 2, 1, 2, 1],
  [2, 2, 2, 2, 1, 1, 2, 2, 2, 2],
  [1, 2, 1, 2, 2, 2, 2, 1, 2, 1],
  [1, 4, 1, 1, 2, 2, 1, 1, 2, 1],
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

TREATS = 47

UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)
NONE = (0, 0)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (205, 133, 63)
BROWN = (150, 75, 0)

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

MOVE_ENEMY = pygame.USEREVENT + 1
ENEMY_SPEED_INTERVAL = 300

cat = pygame.image.load("assets/images/cat.png")
CAT = pygame.transform.scale(cat, (TILE_SIZE, TILE_SIZE))
dog = pygame.image.load("assets/images/dog.png")
DOG = pygame.transform.scale(dog, (TILE_SIZE, TILE_SIZE))

def draw_dog(target_rect):
  SCREEN.blit(DOG, target_rect)

def draw_cat(target_rect):
  SCREEN.blit(CAT, target_rect)

def draw_circle(row, col, screen):
  pygame.draw.circle(screen, BROWN, (col * TILE_SIZE + TILE_SIZE // 2, row * TILE_SIZE + TILE_SIZE // 2), 3)

TILE_MAP = {
  FREE: (BLACK, None),
  WALL: (GREEN, None),
  TREAT: (BLACK, draw_circle),
  ENEMY: (None, draw_dog),
  ENEMY_TREAT: (None, draw_dog),
  PLAYER: (None, draw_cat)
}