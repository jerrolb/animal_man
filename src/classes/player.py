from constants import FREE, TREAT, PLAYER, ENEMY, ENEMY_TREAT, TILE_SIZE
from assets import get_cat_img, collect_treat
from components.hud import hud

class Player:
  def __init__(self):
    self.x = 1
    self.y = 1
    self.treats = 0
    
  def throw_toy(self, game):
    if game.game_over: return
  
  def move(self, x, y, game, map, direction):
    if game.game_over: return
    game.running = True

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