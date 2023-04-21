import pygame
from constants import SCREEN, BROWN, ENEMY1, ENEMY2, WALL, PLAYER, FREE, TREAT, ENEMY, ENEMY_TREAT, BLACK, MAP1, MAP2, MAP3, MAP4, MAP5, TILE_SIZE
from assets import get_enemy1_img, get_enemy2_image, get_cat_img, get_wall_img, treat_img, grass_img
import random

class Map:
  def __init__(self):
    self.tile_map = {
      FREE: (None, self.draw_free),
      WALL: (None, self.draw_wall),
      TREAT: (BLACK, self.draw_treat),
      ENEMY: (None, self.draw_enemy),
      ENEMY1: (None, self.draw_enemy),
      ENEMY2: (None, self.draw_enemy),
      ENEMY_TREAT: (None, self.draw_enemy),
      PLAYER: (None, self.draw_player)
    }
    self.default_map = MAP1
    self.map_name = 'Map1'
    self.toys = []
    self.init_map()

  def init_map(self):
    self.toys = []
    self.map = [row[:] for row in self.default_map]
    self.width = len(self.map[0])
    self.height = len(self.map)
    self.num_treats = sum(row.count(TREAT) + row.count(ENEMY1) + row.count(ENEMY2) for row in self.default_map)
    self.enemy1_pos = [(i, j) for i, row in enumerate(self.default_map) for j, elem in enumerate(row) if elem == -1][0]
    self.enemy2_pos = [(i, j) for i, row in enumerate(self.default_map) for j, elem in enumerate(row) if elem == -2][0]

  def draw_enemy(self, target_rect, image, direction, tile_type, row, col):
    current_position = target_rect.copy()
    if direction == 'up':
      current_position.y = current_position.y + TILE_SIZE
    if direction == 'right':
      current_position.x = current_position.x - TILE_SIZE
    if direction == 'down':
      current_position.y = current_position.y - TILE_SIZE
    if direction == 'left':
      current_position.x = current_position.x + TILE_SIZE
      
    curr_ref = current_position.copy()
    
    for i in range(0, TILE_SIZE // 8):
      SCREEN.blit(grass_img, current_position)
      if direction == 'up':
        current_position.y = current_position.y - 8
      if direction == 'right':
        current_position.x = current_position.x + 8
      if direction == 'down':
        current_position.y = current_position.y + 8
      if direction == 'left':
        current_position.x = current_position.x - 8

      SCREEN.blit(grass_img, curr_ref)
      SCREEN.blit(grass_img, target_rect)
      SCREEN.blit(image, current_position)
      pygame.display.flip()
      
    if tile_type == ENEMY:
      SCREEN.blit(grass_img, curr_ref)
    elif tile_type == ENEMY_TREAT:
      self.draw_treat(row, col)
      
    SCREEN.blit(image, target_rect)
    
    if len(self.toys) > 0 and target_rect.x // TILE_SIZE == self.toys[0][0] and target_rect.y // TILE_SIZE == self.toys[0][1]:
      self.toys.pop()

  def draw_player(self, target_rect, image, direction):
    current_position = target_rect.copy()
    if direction == 'up':
      current_position.y = current_position.y + TILE_SIZE
    if direction == 'right':
      current_position.x = current_position.x - TILE_SIZE
    if direction == 'down':
      if current_position.y > TILE_SIZE:
        current_position.y = current_position.y - TILE_SIZE
    if direction == 'left':
      current_position.x = current_position.x + TILE_SIZE
      
    curr_ref = current_position.copy()
    
    for i in range(0, TILE_SIZE // 8):
      if direction == 'up':
        current_position.y = current_position.y - 8
      if direction == 'right':
        current_position.x = current_position.x + 8
      if direction == 'down':
        if current_position.y > TILE_SIZE:
          current_position.y = current_position.y + 8
        else:
          break
      if direction == 'left':
        current_position.x = current_position.x - 8
    
      SCREEN.blit(grass_img, curr_ref)
      SCREEN.blit(grass_img, target_rect)
      SCREEN.blit(image, current_position)
      pygame.display.flip()
      
    SCREEN.blit(image, target_rect)
    
    if len(self.toys) > 0 and target_rect.x // TILE_SIZE == self.toys[0][0] and target_rect.y // TILE_SIZE == self.toys[0][1]:
      self.toys.pop()

  def draw_treat(self, row, col):
    SCREEN.blit(grass_img, pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    SCREEN.blit(treat_img, pygame.Rect(col * TILE_SIZE + TILE_SIZE / 4, row * TILE_SIZE + TILE_SIZE / 4, TILE_SIZE, TILE_SIZE))

  def draw_wall(self, target_rect, image):
    SCREEN.blit(image, target_rect)
  
  def draw_free(self, target_rect):
    SCREEN.blit(grass_img, target_rect)

  def handle_map_action(self, row, col, tile_type, image, direction):
    row += 1
    target_rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
    color, action = self.tile_map.get(tile_type, (None, None))
    if color:
      pygame.draw.rect(SCREEN, color, target_rect)
    if action == self.draw_enemy:
      action(target_rect, image, direction, tile_type, row, col)
    if action == self.draw_player:
      action(target_rect, image, direction)
    if action == self.draw_treat:
      action(row, col)
    if action == self.draw_wall:
      action(target_rect, image)
    if action == self.draw_free:
      action(target_rect)

  def draw_initial_screen(self):    
    random_wall = random.choice([0, 1])
    for row, col in enumerate(self.default_map):
      for col, tile_type in enumerate(col):
        image = None
        if tile_type == ENEMY1:
          image = get_enemy1_img('down')
        if tile_type == ENEMY2:
          image = get_enemy2_image('down')
        if tile_type == WALL:
          image = get_wall_img(random_wall)
        if tile_type == PLAYER:
          image = get_cat_img('down')
        if tile_type == TREAT:
          image = treat_img
        if tile_type == FREE:
          image = grass_img

        self.handle_map_action(row, col, tile_type, image, '')

  def update_screen(self, dirty_tiles, image, direction):
    for item in reversed(dirty_tiles):
      row, col = item[0]
      tile_type = item[1]
      self.map[row][col] = tile_type
      self.handle_map_action(row, col, tile_type, image, direction)
  
  def set_map(self, map):
    map_map = {
      'Map1': MAP1,
      'Map2': MAP2,
      'Map3': MAP3,
      'Map4': MAP4,
      'Map5': MAP5,
    }
    self.default_map = map_map[map]
    self.map_name = map
    self.init_map()

map = Map()
