import pygame
from constants import BLACK, SCREEN, MOVE_ENEMY, ENEMY_SPEED_MAP, WHITE, TILE_SIZE, SCREEN_WIDTH
from assets import DOG1, DOG2
from screens import close_main_menu, main_menu_button, new_game_button
from components.hud import hud

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
    map.draw_initial_screen()
    hud.display_hud(self.difficulty, map.map_name)
    hud.display_treats(player.treats)
    self.enemy1 = Enemy(map.enemy1_pos[0], map.enemy1_pos[1], DOG1(TILE_SIZE), map)
    self.enemy2 = Enemy(map.enemy2_pos[0], map.enemy2_pos[1], DOG2(TILE_SIZE), map)

  def stop(self):
    self.running = False
    self.game_over = True

  def end_game(self, map):
    new_game_button.show()
    main_menu_button.show()
    if game.collected >= map.num_treats:
      self.display_win_text()
    else:
      self.display_dead_text()
  
  def set_difficulty(self, difficulty):
    self.difficulty = difficulty
    pygame.time.set_timer(MOVE_ENEMY, ENEMY_SPEED_MAP[self.difficulty])

  def display_win_text(self):
    font = pygame.font.Font(None, 36)
    text = font.render("You Won!", True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 30))
    SCREEN.blit(text, text_rect)
          
  def display_dead_text(self):
    font = pygame.font.Font(None, 36)
    text = font.render("You died!", True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 30))
    SCREEN.blit(text, text_rect)

game = Game()