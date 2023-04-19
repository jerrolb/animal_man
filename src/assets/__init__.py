import os
import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

script_path = os.path.abspath(sys.argv[0])
script_dir = os.path.dirname(script_path)
assets_dir = os.path.join(script_dir, "assets")
cat_path = os.path.join(assets_dir, "images", "cat.png")
dog1_path = os.path.join(assets_dir, "images", "dog1.png")
dog2_path = os.path.join(assets_dir, "images", "dog2.png")
wall_path = os.path.join(assets_dir, "images", "wall.jpeg")
splash_path = os.path.join(assets_dir, "images", "splash.png")
treat_path = os.path.join(assets_dir, "images", "treat.png")
collect_treat_path = os.path.join(assets_dir, "sounds", "collect_treat.wav")

treat_img = pygame.image.load(treat_path)
def TREAT_IMG(tile_size):
  return pygame.transform.scale(treat_img, (tile_size / 2, tile_size / 2))
cat = pygame.image.load(cat_path)
def CAT(tile_size):
  return pygame.transform.scale(cat, (tile_size, tile_size))
dog1 = pygame.image.load(dog1_path)
def DOG1(tile_size):
  return pygame.transform.scale(dog1, (tile_size, tile_size))
dog2 = pygame.image.load(dog2_path)
def DOG2(tile_size):
  return pygame.transform.scale(dog2, (tile_size, tile_size))
wall_img = pygame.image.load(wall_path)
def WALL_IMG(tile_size):
  return pygame.transform.scale(wall_img, (tile_size, tile_size))

bg_image = pygame.image.load(splash_path)
bg_image.set_alpha(40)
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

collect_treat = pygame.mixer.Sound(collect_treat_path)
