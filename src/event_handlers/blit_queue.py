from constants import SCREEN

def blit_queue(map):
  if (len(map.enemy_moves[1])):
    blit1 = map.enemy_moves[1].popleft()
    if blit1[0] == 'treat':
      map.draw_treat(blit1[1], blit1[2])
    elif blit1[0] == 'group':
      SCREEN.blit(blit1[1][0], blit1[1][1])
      SCREEN.blit(blit1[2][0], blit1[2][1])
      SCREEN.blit(blit1[3][0], blit1[3][1])
    else:
      SCREEN.blit(blit1[0], blit1[1])
  if (len(map.enemy_moves[2])):
    blit2 = map.enemy_moves[2].popleft()
    if blit2[0] == 'treat':
      map.draw_treat(blit2[1], blit2[2])
    elif blit2[0] == 'group':
      SCREEN.blit(blit2[1][0], blit2[1][1])
      SCREEN.blit(blit2[2][0], blit2[2][1])
      SCREEN.blit(blit2[3][0], blit2[3][1])
    else:
      SCREEN.blit(blit2[0], blit2[1])
  if (len(map.player_moves)):
    player_blit = map.player_moves.popleft()
    if player_blit[0] == 'group':
      SCREEN.blit(player_blit[1][0], player_blit[1][1])
      SCREEN.blit(player_blit[2][0], player_blit[2][1])
      SCREEN.blit(player_blit[3][0], player_blit[3][1])
    else:
      SCREEN.blit(player_blit[0], player_blit[1])
  