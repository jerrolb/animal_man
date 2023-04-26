import json
import os

def set_player_stats(treats, toys):
  data = { 'treats': { 'total': treats['total'], 'spent': treats['spent'] }, 'toys': toys }
  with open("stats.json", "w") as f:
    json.dump(data, f)

def get_player_stats(player):
  try:
    with open("stats.json", "r") as f:
      stats = json.load(f)
      player.treats = stats['treats']
      player.toys = stats['toys']
  except FileNotFoundError:
    set_player_stats(0, 10)
    player.treats = { 'total': 0, 'spent': 0 }
    player.toys = 10