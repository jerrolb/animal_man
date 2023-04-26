import pygame
import pygame_gui
from constants import SCREEN, UI, BLACK, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT
from screens.main_menu import open_main_menu, close_main_menu, main_menu_button, new_game_button
from assets import bg_image

toys_input = pygame_gui.elements.UITextEntryLine(
  initial_text="1",
  relative_rect=pygame.Rect((SCREEN.get_width() // 2 - 50, SCREEN.get_height() // 2 - 150, 100, 30)),
  manager=UI,
)
toys_input.set_allowed_characters(['0','1','2','3','4','5','6','7','8','9','0'
])
toys_input.set_text_length_limit(4)
toys_input.hide()

purchase_button = pygame_gui.elements.UIButton(
  relative_rect=pygame.Rect((SCREEN.get_width() // 2 + 55, SCREEN.get_height() // 2 - 150, 100, 30)),
  text="Purchase",
  manager=UI,
)
purchase_button.hide()

def open_shop():
  SCREEN.fill(BLACK)
  close_main_menu()
  toys_input.show()
  purchase_button.show()
  main_menu_button.show()
  new_game_button.show()
  SCREEN.blit(bg_image, (0, 0))
  
  font = pygame.font.Font(None, 30)  
  text = font.render("Toys (100x treats)", True, WHITE)
  text_rect = text.get_rect(center=(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 135))
  SCREEN.blit(text, text_rect)

def close_shop():
  SCREEN.fill(BLACK)
  toys_input.hide()
  purchase_button.hide()
  open_main_menu()
