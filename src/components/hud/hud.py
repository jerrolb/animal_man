import pygame
from constants import BLACK, WHITE, SCREEN_WIDTH, SCREEN, TILE_SIZE

def display_treats(treats):
  font = pygame.font.Font(None, 36)
  text = font.render(f"Treats: {treats}", True, WHITE)
  text_rect = text.get_rect(topright=(SCREEN_WIDTH - 40, 30))
  pygame.draw.rect(SCREEN, BLACK, text_rect.inflate(10, 10))
  SCREEN.blit(text, text_rect)

def display_hud(difficulty, map_name):
  hud_background = pygame.Surface((SCREEN_WIDTH, 3))
  hud_background.fill((64, 64, 64, 50))
  SCREEN.blit(hud_background, (0, TILE_SIZE - 1))

  font = pygame.font.Font(None, 36)
  text = font.render(f"Difficulty: {difficulty}", True, WHITE)
  text_rect = text.get_rect(topleft=(10, 10))
  SCREEN.blit(text, text_rect)

  font = pygame.font.Font(None, 36)
  text = font.render(f"Map: {map_name}", True, WHITE)
  text_rect = text.get_rect(topleft=(10, 35))
  SCREEN.blit(text, text_rect)
