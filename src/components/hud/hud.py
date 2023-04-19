import pygame
from constants import BLACK, WHITE, SCREEN_WIDTH, SCREEN

def display_treats(treats):
  font = pygame.font.Font(None, 36)
  text = font.render(f"Treats: {treats}", True, WHITE)
  text_rect = text.get_rect(topright=(SCREEN_WIDTH - 40, 30))
  pygame.draw.rect(SCREEN, BLACK, text_rect.inflate(10, 10))
  SCREEN.blit(text, text_rect)