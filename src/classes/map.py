import pygame
from constants import SCREEN, BROWN, ENEMY1, ENEMY2, WALL, PLAYER, FREE, TREAT, ENEMY, ENEMY_TREAT, BLACK, MAP1, MAP2, MAP3, MAP4, TILE_SIZE
from assets import DOG1, DOG2, CAT, WALL_IMG, TREAT_IMG

class Map:
  def __init__(self):
    self.tile_map = {
      FREE: (BLACK, None),
      WALL: (None, self.draw_wall),
      TREAT: (BLACK, self.draw_treat),
      ENEMY: (None, self.draw_enemy),
      ENEMY1: (None, self.draw_enemy),
      ENEMY2: (None, self.draw_enemy),
      ENEMY_TREAT: (None, self.draw_enemy),
      PLAYER: (None, self.draw_player)
    }
    self.default_map = MAP1
    self.init_map()

  def init_map(self):
    self.map = [row[:] for row in self.default_map]
    self.width = len(self.map[0])
    self.height = len(self.map)
    self.num_treats = sum(row.count(TREAT) + row.count(ENEMY1) + row.count(ENEMY2) for row in self.default_map)
    self.enemy1_pos = [(i, j) for i, row in enumerate(self.default_map) for j, elem in enumerate(row) if elem == -1][0]
    self.enemy2_pos = [(i, j) for i, row in enumerate(self.default_map) for j, elem in enumerate(row) if elem == -2][0]

  def draw_enemy(self, target_rect, image):
    SCREEN.blit(image, target_rect)

  def draw_player(self, target_rect, image):
    SCREEN.blit(image, target_rect)

  def draw_treat(self, row, col):
    SCREEN.blit(TREAT_IMG(TILE_SIZE), pygame.Rect(col * TILE_SIZE + TILE_SIZE / 4, row * TILE_SIZE + TILE_SIZE / 4, TILE_SIZE, TILE_SIZE))

  def draw_wall(self, target_rect, image):
    SCREEN.blit(image, target_rect)

  def handle_map_action(self, row, col, tile_type, image):
    row += 1
    target_rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
    color, action = self.tile_map.get(tile_type, (None, None))
    if color:
      pygame.draw.rect(SCREEN, color, target_rect)
    if action == self.draw_enemy:
      action(target_rect, image)
    if action == self.draw_player:
      action(target_rect, image)
    if action == self.draw_treat:
      action(row, col)
    if action == self.draw_wall:
      action(target_rect, image)

  def draw_initial_screen(self):    
    for row, col in enumerate(self.default_map):
      for col, tile_type in enumerate(col):
        image = None
        if tile_type == ENEMY1:
          image = DOG1(TILE_SIZE)
        if tile_type == ENEMY2:
          image = DOG2(TILE_SIZE)
        if tile_type == WALL:
          image = WALL_IMG(TILE_SIZE)
        if tile_type == PLAYER:
          image = CAT(TILE_SIZE)
        if tile_type == TREAT:
          image = TREAT_IMG(TILE_SIZE)

        self.handle_map_action(row, col, tile_type, image)

  def update_screen(self, dirty_tiles, image):
    for item in dirty_tiles:
      row, col = item[0]
      tile_type = item[1]
      self.map[row][col] = tile_type
      self.handle_map_action(row, col, tile_type, image)
  
  def set_map(self, map):
    map_map = {
      'Map1': MAP1,
      'Map2': MAP2,
      'Map3': MAP3,
      'Map4': MAP4,
    }
    self.default_map = map_map[map]
    self.init_map()

map = Map()
