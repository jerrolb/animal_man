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
splash_path = os.path.join(assets_dir, "images", "splash.png")
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
    1: enemy1_sprite.subsurface(0, 0, 40, 40),
    2: enemy1_sprite.subsurface(40, 0, 40, 40),
    3: enemy1_sprite.subsurface(80, 0, 40, 40),
    4: enemy1_sprite.subsurface(120, 0, 40, 40),
  },
  'left': {
    1: enemy1_sprite.subsurface(0, 40, 40, 40),
    2: enemy1_sprite.subsurface(40, 40, 40, 40),
    3: enemy1_sprite.subsurface(80, 40, 40, 40),
    4: enemy1_sprite.subsurface(120, 40, 40, 40),
  },
  'right': {
    1: enemy1_sprite.subsurface(0, 80, 40, 40),
    2: enemy1_sprite.subsurface(40, 80, 40, 40),
    3: enemy1_sprite.subsurface(80, 80, 40, 40),
    4: enemy1_sprite.subsurface(120, 80, 40, 40),
  },
  'up': {
    1: enemy1_sprite.subsurface(0, 120, 40, 40),
    2: enemy1_sprite.subsurface(40, 120, 40, 40),
    3: enemy1_sprite.subsurface(80, 120, 40, 40),
    4: enemy1_sprite.subsurface(120, 120, 40, 40),
  },
}

enemy2_dir_images = {
  'down': {
    1: enemy2_sprite.subsurface(0, 0, 50, 48),
    2: enemy2_sprite.subsurface(50, 0, 50, 48),
    3: enemy2_sprite.subsurface(100, 0, 50, 48),
    4: enemy2_sprite.subsurface(150, 0, 50, 48),
  },
  'left': {
    1: enemy2_sprite.subsurface(0, 48, 50, 48),
    2: enemy2_sprite.subsurface(50, 48, 50, 48),
    3: enemy2_sprite.subsurface(100, 48, 50, 48),
    4: enemy2_sprite.subsurface(150, 48, 50, 48),
  },
  'right': {
    1: enemy2_sprite.subsurface(0, 96, 50, 48),
    2: enemy2_sprite.subsurface(50, 96, 50, 48),
    3: enemy2_sprite.subsurface(100, 96, 50, 48),
    4: enemy2_sprite.subsurface(150, 96, 50, 48),
  },
  'up': {
    1: enemy2_sprite.subsurface(0, 144, 50, 48),
    2: enemy2_sprite.subsurface(50, 144, 50, 48),
    3: enemy2_sprite.subsurface(100, 144, 50, 48),
    4: enemy2_sprite.subsurface(150, 144, 50, 48),
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
  return enemy2_dir_images[direction][random.randint(1,4)]

def get_wall_img(random_wall):
  return walls[random_wall]