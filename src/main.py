import pygame
import pygame_gui
import sys

pygame.init()

from constants import *
from screens.main_menu import *
from screens.credits import *
from screens.settings import *
from classes import player, game, map, Enemy
from event_handlers import move_player

pygame.display.set_caption("Cat-man")
clock = pygame.time.Clock()
open_main_menu()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        player.throw_toy(player, game, map)
      else:
        move_player(event.key, player, game, map)
      
    

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
        print('shop')
      if event.ui_element == main_menu_button:
        game.running = False
        game.game_over = True
        SCREEN.fill(BLACK)
        close_credits()
        close_settings()
    
    UI.process_events(event)

  if game.running and game.game_over:
    game.stop()
    game.end_game(map)

  UI.update(FPS)
  clock.tick(FPS)
  UI.draw_ui(SCREEN)
  pygame.display.update()