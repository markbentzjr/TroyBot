import math

from position import *
from rlbot.utils.structures.game_data_struct import GameTickPacket

#get ball location
ball_location_y =  packet.game_ball.physics.location.y
                   
  
#If ball in enemy half change state team Blue
if packet.game_cars[agent.index].team == 0 and ball_location_y > 0
  state = strategy.shooting
else
  state = strategy.defense
  
#If ball in enemy half change state team Orange
if packet.game_cars[agent.index].team == 1 and ball_location_y < 0
  state = strategy.shooting
else
  state = strategy.defense

#shooting code
def shooting(agent, packet)
  
