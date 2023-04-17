import pygame
import pygame_gui
import sys
import random

pygame.init()

from constants import *
from screens.main_menu import *
from screens.credits import *

pygame.display.set_caption("Cat-man")
pygame.time.set_timer(MOVE_ENEMY, ENEMY_SPEED_INTERVAL)
collect_treat = pygame.mixer.Sound('assets/sounds/collect_treat.wav')
clock = pygame.time.Clock()

class Game:
  def __init__(self):
    self.collected = 0
    self.game_over = False
    self.running = False
    self.enemy1 = Enemy(6, 1, DOG1)
    self.enemy2 = Enemy(2, 8, DOG2)

  def start(self):
    SCREEN.fill(BLACK)
    close_main_menu()
    main_menu_button.hide()
    self.running = True
    self.collected = 0
    player.x = 1
    player.y = 1
    self.game_over = False
    for row, col in enumerate(INITIAL_MAP):
      for col, val in enumerate(col):
        MAP[row][col] = val
    draw_initial_screen()
    self.enemy1 = Enemy(6, 1, DOG1)
    self.enemy2 = Enemy(2, 8, DOG2)

  def stop(self):
    self.running = False
    self.game_over = True

  def end_game(self):
    new_game_button.show()
    main_menu_button.show()
    if game.collected >= TREATS:
      display_win_text()
    else:
      display_dead_text()

class Player:
  def __init__(self):
    self.x = 1
    self.y = 1
  
  def move(self, x, y):
    if game.game_over: return
    dirty_tiles = [((self.y, self.x), FREE)]
    self.x += x
    self.y += y
    location = MAP[self.y][self.x]

    if location == TREAT:
      dirty_tiles.append(((self.y, self.x), PLAYER))
      if game.game_over == False:
        game.collected += 1
      collect_treat.play()
    if location == FREE:
      dirty_tiles.append(((self.y, self.x), PLAYER))
    if location in [ENEMY, ENEMY_TREAT] or game.collected >= TREATS:
      game.game_over = True

    update_screen(dirty_tiles, CAT)

class Enemy:
  def __init__(self, y, x, image):
    self.x = x
    self.y = y
    self.image = image
    MAP[self.y][self.x] = ENEMY_TREAT

  def move(self):
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
    is_valid_move = 0 <= self.y + dir[1] < len(MAP) and 0 <= self.x + dir[0] < len(MAP[self.y + dir[1] - 1])
    next_pos = MAP[self.y + dir[1]][self.x + dir[0]]

    if is_valid_move and next_pos not in [ENEMY_TREAT, ENEMY, WALL]:
      if MAP[self.y][self.x] == ENEMY_TREAT:
        dirty_tiles.append(((self.y, self.x), TREAT))
      else:
        dirty_tiles.append(((self.y, self.x), FREE))

      self.x += dir[0]
      self.y += dir[1]

      if MAP[self.y][self.x] == TREAT:
        dirty_tiles.append(((self.y, self.x), ENEMY_TREAT))
      if MAP[self.y][self.x] == FREE:
        dirty_tiles.append(((self.y, self.x), ENEMY))
      if self.y == player.y and self.x == player.x:
        dirty_tiles.append(((self.y, self.x), ENEMY))
        game.game_over = True
        
    update_screen(dirty_tiles, self.image)

def handle_map_action(row, col, tile_type, image):
  target_rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
  color, action = TILE_MAP.get(tile_type, (None, None))
  if color:
    pygame.draw.rect(SCREEN, color, target_rect)
  if action == draw_dog:
    action(target_rect, image)
  if action == draw_cat:
    action(target_rect)
  if action == draw_circle:
    action(row, col, SCREEN)
  if action == draw_wall:
    action(target_rect, image)

def draw_initial_screen():    
  for row, col in enumerate(MAP):
    for col, tile_type in enumerate(col):
      image = None
      if tile_type == ENEMY1:
        image = DOG1
      if tile_type == ENEMY2:
        image = DOG2
      if tile_type == WALL:
        image = WALL_IMG

      handle_map_action(row, col, tile_type, image)

def update_screen(dirty_tiles, image):
  for item in dirty_tiles:
    row, col = item[0]
    tile_type = item[1]
    MAP[row][col] = tile_type
    handle_map_action(row, col, tile_type, image)

def display_win_text():
  font = pygame.font.Font(None, 30)
  text = font.render("You Won!", True, WHITE)
  text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 15))
  SCREEN.blit(text, text_rect)
        
def display_dead_text():
  font = pygame.font.Font(None, 30)
  text = font.render("You died!", True, WHITE)
  text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 15))
  SCREEN.blit(text, text_rect)

open_main_menu()
game = Game()
player = Player()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == MOVE_ENEMY:
      for enemy in [game.enemy1, game.enemy2]:
        if game.running:
          enemy.move()
    if event.type == pygame_gui.UI_BUTTON_PRESSED:
      if event.ui_element == new_game_button:
        game.start()
      if event.ui_element == tutorial:
        print('tutorial')
      if event.ui_element == credits:
        open_credits()
      if event.ui_element == shop_button:
        print('shop')
      if event.ui_element == main_menu_button:
        close_credits()
        game.running = False
        game.game_over = True
    if event.type == pygame.KEYDOWN:
      cat_rect = pygame.Rect(player.x * TILE_SIZE, player.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
      if event.key == pygame.K_UP:
        if cat_rect.top > 0 and MAP[player.y - 1][player.x] != WALL:
          player.move(0, -1)
        elif cat_rect.top == 0 and MAP[MAP_HEIGHT - 1][player.x] != WALL:
          player.move(0, MAP_HEIGHT - 1 - player.y)
      elif event.key == pygame.K_DOWN:
        if cat_rect.bottom < SCREEN_HEIGHT and MAP[player.y + 1][player.x] != WALL:
          player.move(0, 1)
        elif cat_rect.bottom == SCREEN_HEIGHT and MAP[0][player.x] != WALL:
          player.move(0, -player.y)
      elif event.key == pygame.K_LEFT:
        if cat_rect.left > 0 and MAP[player.y][player.x - 1] != WALL:
          player.move(-1, 0)
        elif cat_rect.left == 0 and MAP[player.y][MAP_WIDTH - 1] != WALL:
          player.move(MAP_WIDTH - 1 - player.x, 0)
      elif event.key == pygame.K_RIGHT:
        if cat_rect.right < SCREEN_WIDTH and MAP[player.y][player.x + 1] != WALL:
          player.move(1, 0)
        elif cat_rect.right == SCREEN_WIDTH and MAP[player.y][0] != WALL:
          player.move(-player.x, 0)
    UI.process_events(event)

  if game.running and game.game_over:
    game.stop()
    game.end_game()

  UI.update(FPS)
  clock.tick(FPS)
  UI.draw_ui(SCREEN)
  pygame.display.update()