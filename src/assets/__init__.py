import os
import sys
import pygame

script_path = os.path.abspath(sys.argv[0])
script_dir = os.path.dirname(script_path)
assets_dir = os.path.join(script_dir, "assets")
cat_path = os.path.join(assets_dir, "images", "cat.png")
dog1_path = os.path.join(assets_dir, "images", "dog1.png")
dog2_path = os.path.join(assets_dir, "images", "dog2.png")
wall_path = os.path.join(assets_dir, "images", "wall.jpeg")
collect_treat_path = os.path.join(assets_dir, "sounds", "collect_treat.wav")

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

collect_treat = pygame.mixer.Sound(collect_treat_path)