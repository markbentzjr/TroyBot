import math

from position import Vector3
from ballchase import ball_chase

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
def kickoff(agent, packet):
    ball_chase(agent, packet)
    agent.controller_state.boost = True
    return agent
