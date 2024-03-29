import os
import sys
import pygame
from constants import TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT
import random

script_path = os.path.abspath(sys.argv[0])
script_dir = os.path.dirname(script_path)
assets_dir = os.path.join(script_dir, "assets")
player_path = os.path.join(assets_dir, "sprites", "player.png")
enemy1_path = os.path.join(assets_dir, "sprites", "enemy1.png")
enemy2_path = os.path.join(assets_dir, "sprites", "enemy2.png")
wall1_path = os.path.join(assets_dir, "images", "wall1.jpeg")
wall2_path = os.path.join(assets_dir, "images", "wall2.jpeg")
splash_path = os.path.join(assets_dir, "images", "splash.jpeg")
treat_path = os.path.join(assets_dir, "images", "treat.png")
free_path = os.path.join(assets_dir, "images", "grass.png")
toy_path = os.path.join(assets_dir, "images", "chew_toy.png")
collect_treat_path = os.path.join(assets_dir, "sounds", "collect_treat.wav")

def scale_img(image, width = TILE_SIZE, height = TILE_SIZE):
  return pygame.transform.scale(image, (width, height))

treat_img = scale_img(pygame.image.load(treat_path), TILE_SIZE / 2, TILE_SIZE / 2)
player_sprite = pygame.image.load(player_path)
enemy1_sprite = pygame.image.load(enemy1_path)
enemy2_sprite = pygame.image.load(enemy2_path)
wall1_img = scale_img(pygame.image.load(wall1_path))
wall2_img = scale_img(pygame.image.load(wall2_path))
grass_img = scale_img(pygame.image.load(free_path))
toy_img = scale_img(pygame.image.load(toy_path))
bg_image = scale_img(pygame.image.load(splash_path), SCREEN_WIDTH, SCREEN_HEIGHT)
bg_image.set_alpha(100)

walls = [wall1_img, wall2_img]

collect_treat = pygame.mixer.Sound(collect_treat_path)

player_dir_images = {
  'down': {
    1: player_sprite.subsurface(0, 0, 32, 32),
    2: player_sprite.subsurface(32, 0, 32, 32),
    3: player_sprite.subsurface(64, 0, 32, 32),
    4: player_sprite.subsurface(96, 0, 32, 32),
  },
  'left': {
    1: player_sprite.subsurface(0, 32, 32, 32),
    2: player_sprite.subsurface(32, 32, 32, 32),
    3: player_sprite.subsurface(64, 32, 32, 32),
    4: player_sprite.subsurface(96, 32, 32, 32),
  },
  'right': {
    1: player_sprite.subsurface(0, 64, 32, 32),
    2: player_sprite.subsurface(32, 64, 32, 32),
    3: player_sprite.subsurface(64, 64, 32, 32),
    4: player_sprite.subsurface(96, 64, 32, 32),
  },
  'up': {
    1: player_sprite.subsurface(0, 96, 32, 32),
    2: player_sprite.subsurface(32, 96, 32, 32),
    3: player_sprite.subsurface(64, 96, 32, 32),
    4: player_sprite.subsurface(96, 96, 32, 32),
  },
}

enemy1_dir_images = {
  'down': {
    1: enemy1_sprite.subsurface(0, 0, 80, 80),
    2: enemy1_sprite.subsurface(80, 0, 80, 80),
    3: enemy1_sprite.subsurface(160, 0, 80, 80),
    4: enemy1_sprite.subsurface(240, 0, 80, 80),
  },
  'right': {
    1: enemy1_sprite.subsurface(0, 80, 80, 80),
    2: enemy1_sprite.subsurface(80, 80, 80, 80),
    3: enemy1_sprite.subsurface(160, 80, 80, 80),
    4: enemy1_sprite.subsurface(240, 80, 80, 80),
  },
  'up': {
    1: enemy1_sprite.subsurface(0, 160, 80, 80),
    2: enemy1_sprite.subsurface(80, 160, 80, 80),
    3: enemy1_sprite.subsurface(160, 160, 80, 80),
    4: enemy1_sprite.subsurface(240, 160, 80, 80),
  },
  'left': {
    1: enemy1_sprite.subsurface(0, 240, 80, 80),
    2: enemy1_sprite.subsurface(80, 240, 80, 80),
    3: enemy1_sprite.subsurface(160, 240, 80, 80),
    4: enemy1_sprite.subsurface(240, 240, 80, 80),
  },
}

enemy2_dir_images = {
  'down': {
    1: enemy2_sprite.subsurface(0, 0, 130, 127.5),
    2: enemy2_sprite.subsurface(130, 0, 130, 127.5),
    3: enemy2_sprite.subsurface(260, 0, 130, 127.5),
  },
  'left': {
    1: enemy2_sprite.subsurface(0, 127.5, 130, 127.5),
    2: enemy2_sprite.subsurface(130, 127.5, 130, 127.5),
    3: enemy2_sprite.subsurface(260, 127.5, 130, 127.5),
  },
  'right': {
    1: enemy2_sprite.subsurface(0, 255, 130, 127.5),
    2: enemy2_sprite.subsurface(130, 255, 130, 127.5),
    3: enemy2_sprite.subsurface(260, 255, 130, 127.5),
  },
  'up': {
    1: enemy2_sprite.subsurface(0, 382.5, 130, 127.5),
    2: enemy2_sprite.subsurface(130, 382.5, 130, 127.5),
    3: enemy2_sprite.subsurface(260, 382.5, 130, 127.5),
  },
}

for dir_images in [player_dir_images, enemy1_dir_images, enemy2_dir_images]:
  for key, value in dir_images.items():
    for subkey, subvalue in value.items():
      scaled_img = scale_img(subvalue)
      value[subkey] = scaled_img

def get_cat_img(direction):
  return player_dir_images[direction][random.randint(1, 4)]

def get_enemy1_img(direction):
  return enemy1_dir_images[direction][random.randint(1,4)]

def get_enemy2_image(direction):
  return enemy2_dir_images[direction][random.randint(1,3)]

def get_wall_img(random_wall):
  return walls[random_wall]