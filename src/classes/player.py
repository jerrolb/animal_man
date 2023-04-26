from constants import FREE, TREAT, PLAYER, ENEMY, ENEMY_TREAT, TILE_SIZE, WALL, SCREEN, DIFFICULTY_TO_TREATS
from assets import get_cat_img, collect_treat, toy_img
from components.hud import hud
import pygame

class Player:
  def __init__(self):
    self.x = 1
    self.y = 1
    self.treats = { 'total': 0, 'spent': 0 }
    self.direction = 'down'
    self.toys = 0
    
  def throw_toy(self, game, map):
    if game.game_over: return
    game.running = True
    if self.toys <= 0:
      return
    
    self.toys -= 1
    
    hud.display_treats(self.treats, self.toys)
    
    xx = self.x
    yy = self.y
    
    if self.direction == 'right':
      while xx + 1 < len(map.map[0]) and map.map[yy][xx + 1] not in [WALL, ENEMY, ENEMY_TREAT]:
        xx += 1

    if self.direction == 'down':
      while yy + 1 < len(map.map) and map.map[yy + 1][xx] not in [WALL, ENEMY, ENEMY_TREAT]:
       yy += 1

    if self.direction == 'left':
      while map.map[yy][xx - 1] not in [WALL, ENEMY, ENEMY_TREAT] and xx - 1 >= 0:
        xx -= 1

    if self.direction == 'up':
      while map.map[yy - 1][xx] not in [WALL, ENEMY, ENEMY_TREAT] and yy - 1 >= 0:
        yy -= 1
    
    SCREEN.blit(toy_img, pygame.Rect(xx * TILE_SIZE, (yy + 1) * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    
    map.toys.append((xx, yy + 1))
    
  def move(self, x, y, game, map, direction):
    if game.game_over: return
    game.running = True
    
    self.direction = direction

    dirty_tiles = [((self.y, self.x), FREE)]
    self.x += x
    self.y += y
    location = map.map[self.y][self.x]

    if location == TREAT:
      dirty_tiles.append(((self.y, self.x), PLAYER))
      game.collected += 1
      self.treats['total'] += 1
      hud.display_treats(self.treats, self.toys)
      # collect_treat.play()
    if location == FREE:
      dirty_tiles.append(((self.y, self.x), PLAYER))
    if location in [ENEMY, ENEMY_TREAT] or game.collected >= map.num_treats:
      game.game_over = True

    map.update_screen(dirty_tiles, get_cat_img(direction), direction)
    
  def add_treats_by_difficulty(self, difficulty):
    self.treats['total'] += DIFFICULTY_TO_TREATS[difficulty]

player = Player()