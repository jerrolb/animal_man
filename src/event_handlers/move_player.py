import pygame
from constants import WALL

def move_player(key, player, game, map):
  if key == pygame.K_UP:
    if player.y > 0 and map.map[player.y - 1][player.x] != WALL:
      player.move(0, -1, game, map, 'up')
    elif player.y == 0 and map.map[map.height - 1][player.x] != WALL:
      player.move(0, map.height - 1 - player.y, game, map, 'up')
  elif key == pygame.K_DOWN:
    if player.y < map.height - 1 and map.map[player.y + 1][player.x] != WALL:
      player.move(0, 1, game, map, 'down')
    elif player.y == map.height - 1 and map.map[0][player.x] != WALL:
      player.move(0, -player.y, game, map, 'down')
  elif key == pygame.K_LEFT:
    if player.x > 0 and map.map[player.y][player.x - 1] != WALL:
      player.move(-1, 0, game, map, 'left')
    elif player.x == 0 and map.map[player.y][map.width - 1] != WALL:
      player.move(map.width - 1 - player.x, 0, game, map, 'left')
  elif key == pygame.K_RIGHT:
    if player.x < map.width - 1 and map.map[player.y][player.x + 1] != WALL:
      player.move(1, 0, game, map, 'right')
    elif player.x == map.width - 1 and map.map[player.y][0] != WALL:
      player.move(-player.x, 0, game, map, 'right')