import pygame
from constants import SCREEN, BLACK, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT, UI
from .main_menu import close_main_menu, main_menu_button, open_main_menu
from assets import bg_image

def open_credits():
  SCREEN.fill(BLACK)
  close_main_menu()
  main_menu_button.show()

  font = pygame.font.Font(None, 30)

  SCREEN.blit(bg_image, (0, 0))
  
  text = font.render("Designer: Jane Brooks", True, WHITE)
  text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 30))
  SCREEN.blit(text, text_rect)

  text = font.render("Designer: Lauren Brooks", True, WHITE)
  text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 60))
  SCREEN.blit(text, text_rect)

  text = font.render("Artist: Jane Brooks", True, WHITE)
  text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 90))
  SCREEN.blit(text, text_rect)

  text = font.render("Tester: Lauren Brooks", True, WHITE)
  text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 120))
  SCREEN.blit(text, text_rect)

  text = font.render("Programmer: Jerrol Brooks", True, WHITE)
  text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 150))
  SCREEN.blit(text, text_rect)

def close_credits():
  SCREEN.fill(BLACK)
  open_main_menu()