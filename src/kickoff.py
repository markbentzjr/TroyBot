import math

from position import Vector3
from ballchase import execute_ballchase

# Action 0: Kickoff
# action.py Dependent
def check_kickoff(agent, packet):
    ball = packet.game_ball.physics
    #print(ball.velocity.x, ball.velocity.y, ball.velocity.z)
    Condition0Loc = Vector3(0, 0, 93)
    Condition0Vel = Vector3(0, 0, 0)
    Location = Vector3(ball.location.x, ball.location.y,
                       math.ceil(ball.location.z))
    Velocity = Vector3(ball.velocity.x, ball.velocity.y, ball.velocity.z)
    if Location.real_distance(
            Condition0Loc) < 1 and Velocity.real_distance(
                Condition0Vel) < 1:
        return True
    return False

# ball_chase dependent
def execute_kickoff(agent, packet):
    execute_ballchase(agent, packet)
    agent.controller_state.boost = True
    
    ball_location = Vector3(packet.game_ball.physics.location.x, packet.game_ball.physics.location.y, packet.game_ball.physics.location.z)
    car_location = Vector3(packet.game_cars[agent.index].physics.location.x, packet.game_cars[agent.index].physics.location.y, packet.game_cars[agent.index].physics.location.z)
    #print(car_location.real_distance(ball_location))
    if car_location.real_distance(ball_location) < 500:
        agent.controller_state.jump = True
        agent.controller_state.steer = 0
        agent.controller_state.pitch = -1


    # No need to return
