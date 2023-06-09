import pygame
import pygame_gui
from constants import SCREEN, UI, BLACK
from screens.main_menu import open_main_menu, close_main_menu, main_menu_button, new_game_button
from assets import bg_image

settings_dropdown = pygame_gui.elements.UIDropDownMenu(
  options_list=['Easy', 'Medium', 'Hard', 'Expert', 'Expert+'],
  starting_option='Easy',
  relative_rect=pygame.Rect((SCREEN.get_width() // 2 - 100, SCREEN.get_height() // 2 - 180, 100, 30)),
  manager=UI,
)
settings_dropdown.hide()

map_dropdown = pygame_gui.elements.UIDropDownMenu(
  options_list=['Map1', 'Map2', 'Map3', 'Map4', 'Map5'],
  starting_option='Map1',
  relative_rect=pygame.Rect((SCREEN.get_width() // 2, SCREEN.get_height() // 2 - 180, 100, 30)),
  manager=UI,
)
map_dropdown.hide()

def open_settings():
  SCREEN.fill(BLACK)
  close_main_menu()
  settings_dropdown.show()
  map_dropdown.show()
  main_menu_button.show()
  new_game_button.show()
  SCREEN.blit(bg_image, (0, 0))

def close_settings():
  settings_dropdown.hide()
  map_dropdown.hide()
  SCREEN.fill(BLACK)
  open_main_menu()
