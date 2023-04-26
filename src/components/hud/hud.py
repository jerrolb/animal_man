import pygame
from constants import BLACK, WHITE, SCREEN_WIDTH, SCREEN, TILE_SIZE

def display_treats(treats, toys):
  font = pygame.font.Font(None, 25)
  text = font.render(f"All-time: {treats['total']}", True, WHITE)
  text2 = font.render(f"Treats: {treats['total'] - treats['spent']}", True, WHITE)
  text3 = font.render(f"Toys: {toys}", True, WHITE)
  total_rect = text.get_rect(topleft=(SCREEN_WIDTH - 180, 10))
  spent_rect = text.get_rect(topleft=(SCREEN_WIDTH - 180, 30))
  toys_rect = text2.get_rect(topleft=(SCREEN_WIDTH - 180, 50))
  pygame.draw.rect(SCREEN, BLACK, total_rect.inflate(50, 80))
  SCREEN.blit(text, total_rect)
  SCREEN.blit(text2, spent_rect)
  SCREEN.blit(text3, toys_rect)

def display_hud(difficulty, map_name):
  hud_background = pygame.Surface((SCREEN_WIDTH, 3))
  hud_background.fill((64, 64, 64, 50))
  SCREEN.blit(hud_background, (0, TILE_SIZE - 1))

  font = pygame.font.Font(None, 30)
  text = font.render(f"Difficulty: {difficulty}", True, WHITE)
  text_rect = text.get_rect(topleft=(10, 20))
  SCREEN.blit(text, text_rect)

  font = pygame.font.Font(None, 30)
  text = font.render(f"Map: {map_name}", True, WHITE)
  text_rect = text.get_rect(topleft=(10, 40))
  SCREEN.blit(text, text_rect)
