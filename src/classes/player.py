from constants import FREE, TREAT, PLAYER, ENEMY, ENEMY_TREAT, TILE_SIZE, WALL, SCREEN
from assets import get_cat_img, collect_treat, toy_img
from components.hud import hud
import pygame

class Player:
  def __init__(self):
    self.x = 1
    self.y = 1
    self.treats = 0
    self.direction = 'down'
    self.toys = 1
    
  def throw_toy(self, player, game, map):
    if game.game_over: return
    if self.toys <= 0:
      return
    
    self.toys -= 1
    
    xx = player.x
    yy = player.y
    
    if self.direction == 'right':
      while xx + 1 < len(map.map[0]) and map.map[yy][xx + 1] != WALL:
        xx += 1

    if self.direction == 'down':
      while yy + 1 < len(map.map) and map.map[yy + 1][xx] != WALL:
       yy += 1

    if self.direction == 'left':
      while map.map[yy][xx - 1] is not WALL and xx - 1 >= 0:
        xx -= 1

    if self.direction == 'up':
      while map.map[yy - 1][xx] is not WALL and yy - 1 >= 0:
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
      self.treats += 1
      hud.display_treats(self.treats)
      collect_treat.play()
    if location == FREE:
      dirty_tiles.append(((self.y, self.x), PLAYER))
    if location in [ENEMY, ENEMY_TREAT] or game.collected >= map.num_treats:
      game.game_over = True

    map.update_screen(dirty_tiles, get_cat_img(direction), direction)

player = Player()