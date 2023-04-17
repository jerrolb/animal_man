from constants import *

def open_main_menu():
  SCREEN.fill(BLACK)
  tutorial.show()
  shop_button.show()
  new_game_button.show()
  credits.show()
  main_menu_button.hide()

def close_main_menu():
  SCREEN.fill(BLACK)
  tutorial.hide()
  shop_button.hide()
  new_game_button.hide()
  credits.hide()

tutorial = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN.get_width() // 2 - 50, SCREEN.get_height() // 2 - 100, 100, 30)), text='Tutorial', manager=UI)

shop_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN.get_width() // 2 - 50, SCREEN.get_height() // 2 - 50, 100, 30)), text='Shop', manager=UI)

new_game_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN.get_width() // 2 - 50, SCREEN.get_height() // 2, 100, 30)), text='New Game', manager=UI)

credits = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN.get_width() // 2 - 50, SCREEN.get_height() // 2 + 50, 100, 30)), text='Credits', manager=UI)

main_menu_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN.get_width() // 2 - 50, SCREEN.get_height() // 2 + 100, 100, 30)), text='Main Menu', manager=UI)