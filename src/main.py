import pygame
import pygame_gui
import sys

pygame.init()

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN, MOVE_ENEMY, FPS
from screens.main_menu import *
from screens.credits import *
from screens.settings import *
from screens.shop import *
from classes import player, game, map, Enemy
from event_handlers import move_player, blit_queue
from api import get_player_stats
from components.hud import hud
import api

pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cat-man")
clock = pygame.time.Clock()
get_player_stats(player)
open_main_menu()

while True:
  blit_queue(map)
      
  UI.update(FPS)
  clock.tick(FPS)
  UI.draw_ui(SCREEN)
  pygame.display.update()
    
  keys = pygame.key.get_pressed()
  if (not len(map.player_moves)):
    if keys[pygame.K_RIGHT]:
      move_player(pygame.K_RIGHT, player, game, map)
    if keys[pygame.K_DOWN]:
      move_player(pygame.K_DOWN, player, game, map)
    if keys[pygame.K_LEFT]:
      move_player(pygame.K_LEFT, player, game, map)
    if keys[pygame.K_UP]:
      move_player(pygame.K_UP, player, game, map)
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        player.throw_toy(game, map)

    if event.type == MOVE_ENEMY:
      for enemy in [game.enemy1, game.enemy2]:
        if game.running:
          enemy.move(game, player, map)

    if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
      if event.ui_element == settings_dropdown:
        game.set_difficulty(settings_dropdown.selected_option)
      if event.ui_element == map_dropdown:
        map.set_map(map_dropdown.selected_option)
    if event.type == pygame_gui.UI_BUTTON_PRESSED:
      if event.ui_element == settings_button:
        open_settings()
      if event.ui_element == new_game_button:
        game.start(map, Enemy, player)
      if event.ui_element == tutorial:
        print('tutorial')
      if event.ui_element == credits:
        open_credits()
      if event.ui_element == shop_button:
        open_shop()
        hud.display_treats(player.treats, player.toys)
      if event.ui_element == purchase_button:
        purchase_amount = int(toys_input.get_text())
        current = player.treats['total'] - player.treats['spent']
        purchase_total = purchase_amount * 100
        
        if current >= purchase_total:
          player.treats['spent'] += purchase_total
          player.toys += purchase_amount
          api.set_player_stats(player.treats, player.toys)
          hud.display_treats(player.treats, player.toys)

      if event.ui_element == main_menu_button:
        game.running = False
        game.game_over = True
        SCREEN.fill(BLACK)
        close_credits()
        close_settings()
        close_shop()
    
    UI.process_events(event)

  if game.running and game.game_over:
    game.stop()
    game.end_game(map, player)
