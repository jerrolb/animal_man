import pygame
from constants import BLACK, SCREEN, MOVE_ENEMY, ENEMY_SPEED_MAP, WHITE, TILE_SIZE, SCREEN_WIDTH, DIFFICULTY_TO_TREATS
from assets import get_enemy1_img, get_enemy2_image
from screens import close_main_menu, main_menu_button, new_game_button, settings_button, close_settings, shop_button, close_shop
from components.hud import hud
import api

class Game:
  def __init__(self):
    self.difficulty = 'Easy'
    self.collected = 0
    self.game_over = False
    self.running = False
    self.enemy1 = None
    self.enemy2 = None

  def start(self, map, Enemy, player):
    SCREEN.fill(BLACK)
    close_settings()
    close_shop()
    close_main_menu()
    main_menu_button.hide()
    self.collected = 0
    self.game_over = False
    player.x = 1
    player.y = 1
    self.set_difficulty(self.difficulty)
    for row, col in enumerate(map.default_map):
      for col, val in enumerate(col):
        map.map[row][col] = val
    map.toys = []
    map.draw_initial_screen()
    player.direction = 'down'
    hud.display_hud(self.difficulty, map.map_name)
    hud.display_treats(player.treats, player.toys)
    self.enemy1 = Enemy(map.enemy1_pos[0], map.enemy1_pos[1], get_enemy1_img, map, 1)
    self.enemy2 = Enemy(map.enemy2_pos[0], map.enemy2_pos[1], get_enemy2_image, map, 2)

  def stop(self):
    self.running = False
    self.game_over = True

  def end_game(self, map, player):
    new_game_button.show()
    main_menu_button.show()
    settings_button.show()
    shop_button.show()
    player.add_treats_by_difficulty(self.difficulty)
    hud.display_treats(player.treats, player.toys)
    api.set_player_stats(player.treats, player.toys)
    
    if game.collected >= map.num_treats:
      self.display_win_text()
    else:
      self.display_dead_text()
  
  def set_difficulty(self, difficulty):
    self.difficulty = difficulty
    pygame.time.set_timer(MOVE_ENEMY, ENEMY_SPEED_MAP[self.difficulty])

  def display_win_text(self):
    font = pygame.font.Font(None, 30)
    text1 = font.render("You Won!", True, WHITE)
    text2 = font.render(f"{self.difficulty} +{DIFFICULTY_TO_TREATS[self.difficulty]} treats!", True, WHITE)
    text_rect1 = text1.get_rect(center=(SCREEN_WIDTH // 2, 30))
    text_rect2 = text2.get_rect(center=(SCREEN_WIDTH // 2, 50))
    SCREEN.blit(text1, text_rect1)
    SCREEN.blit(text2, text_rect2)
          
  def display_dead_text(self):
    font = pygame.font.Font(None, 36)
    text = font.render("You died!", True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 30))
    SCREEN.blit(text, text_rect)

game = Game()