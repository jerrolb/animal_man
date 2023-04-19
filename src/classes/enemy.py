from constants import ENEMY_TREAT, UP, LEFT, RIGHT, DOWN, NONE, ENEMY, WALL, TREAT, FREE
import random

class Enemy:
  def __init__(self, y, x, image, map):
    self.x = x
    self.y = y
    self.image = image
    map.map[self.y][self.x] = ENEMY_TREAT

  def move(self, game, player, map):
    if game.game_over: return
    x_dir = player.x - self.x
    y_dir = player.y - self.y
    moves = []
    dirty_tiles = []

    if x_dir > 0:
        moves.append(RIGHT)
    elif x_dir < 0:
        moves.append(LEFT)
    if y_dir > 0:
        moves.append(DOWN)
    elif y_dir < 0:
        moves.append(UP)
    if not moves:
        moves.append(NONE)

    dir = random.choice(moves)
    is_valid_move = 0 <= self.y + dir[1] < len(map.map) and 0 <= self.x + dir[0] < len(map.map[self.y + dir[1] - 1])
    next_pos = map.map[self.y + dir[1]][self.x + dir[0]]

    if is_valid_move and next_pos not in [ENEMY_TREAT, ENEMY, WALL]:
      if map.map[self.y][self.x] == ENEMY_TREAT:
        dirty_tiles.append(((self.y, self.x), TREAT))
      else:
        dirty_tiles.append(((self.y, self.x), FREE))

      self.x += dir[0]
      self.y += dir[1]

      if map.map[self.y][self.x] == TREAT:
        dirty_tiles.append(((self.y, self.x), ENEMY_TREAT))
      if map.map[self.y][self.x] == FREE:
        dirty_tiles.append(((self.y, self.x), ENEMY))
      if self.y == player.y and self.x == player.x:
        dirty_tiles.append(((self.y, self.x), ENEMY))
        game.game_over = True
        
    map.update_screen(dirty_tiles, self.image)