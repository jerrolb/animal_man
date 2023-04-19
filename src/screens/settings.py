import pygame
import pygame_gui
from constants import SCREEN, UI, BLACK
from screens.main_menu import *

settings_dropdown = pygame_gui.elements.UIDropDownMenu(
  options_list=['Easy', 'Medium', 'Hard', 'Expert', 'Expert+'],
  starting_option='Easy',
  relative_rect=pygame.Rect((SCREEN.get_width() // 2 - 100, SCREEN.get_height() // 2 - 30, 100, 30)),
  manager=UI,
)
settings_dropdown.hide()

map_dropdown = pygame_gui.elements.UIDropDownMenu(
  options_list=['Map1', 'Map2', 'Map3', 'Map4'],
  starting_option='Map1',
  relative_rect=pygame.Rect((SCREEN.get_width() // 2, SCREEN.get_height() // 2 - 30, 100, 30)),
  manager=UI,
)
map_dropdown.hide()

def open_settings():
  SCREEN.fill(BLACK)
  close_main_menu()
  settings_dropdown.show()
  map_dropdown.show()
  main_menu_button.show()

def close_settings():
  settings_dropdown.hide()
  map_dropdown.hide()
  SCREEN.fill(BLACK)
  open_main_menu()
