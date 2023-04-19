from constants import FREE, TREAT, PLAYER, ENEMY, ENEMY_TREAT, TILE_SIZE
from assets import CAT, collect_treat
from components.hud.hud import display_treats

class Player:
  def __init__(self):
    self.x = 1
    self.y = 1
    self.treats = 0
  
  def move(self, x, y, game, map):
    if game.game_over: return
    dirty_tiles = [((self.y, self.x), FREE)]
    self.x += x
    self.y += y
    location = map.map[self.y][self.x]

    if location == TREAT:
      dirty_tiles.append(((self.y, self.x), PLAYER))
      game.collected += 1
      self.treats += 1
      display_treats(self.treats)
      collect_treat.play()
    if location == FREE:
      dirty_tiles.append(((self.y, self.x), PLAYER))
    if location in [ENEMY, ENEMY_TREAT] or game.collected >= map.num_treats:
      game.game_over = True

    map.update_screen(dirty_tiles, CAT(TILE_SIZE))

player = Player()