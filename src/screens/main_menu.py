import pygame
import pygame_gui
from constants import *

def open_main_menu():
  SCREEN.fill(BLACK)
  tutorial.show()
  shop_button.show()
  new_game_button.show()
  credits.show()
  main_menu_button.hide()
  settings_button.show()

def close_main_menu():
  SCREEN.fill(BLACK)
  tutorial.hide()
  shop_button.hide()
  new_game_button.hide()
  credits.hide()
  settings_button.hide()

tutorial = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN.get_width() // 2 - 50, SCREEN.get_height() // 2 - 130, 100, 30)), text='Tutorial', manager=UI)

shop_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN.get_width() // 2 - 50, SCREEN.get_height() // 2 - 80, 100, 30)), text='Shop', manager=UI)

new_game_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN.get_width() // 2 - 50, SCREEN.get_height() // 2 - 30, 100, 30)), text='Start', manager=UI)

credits = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN.get_width() // 2 - 50, SCREEN.get_height() // 2 + 20, 100, 30)), text='Credits', manager=UI)

settings_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN.get_width() // 2 - 50, SCREEN.get_height() // 2 + 70, 100, 30)), text='Settings', manager=UI)

main_menu_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN.get_width() // 2 - 50, SCREEN.get_height() // 2 + 120, 100, 30)), text='Main Menu', manager=UI)
