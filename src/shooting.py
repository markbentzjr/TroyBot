import math

from position import Vector3
from closest_opponent import closest

# Should return True/False
def check_shooting(agent, packet):

    car = packet.game_cars[agent.index]
    ball = packet.game_ball
    car_position = Vector3(car.physics.location.x, car.physics.location.y, car.physics.location.z)
    ball_position = Vector3(ball.physics.location.x, ball.physics.location.y, ball.physics.location.z)
    
    ball_location_y = ball.physics.location.y
    ball_velocity_y = ball.physics.velocity.y

    car_distance = car_position.real_distance(ball_position)
    
    if agent.team == 0:
        if ball_location_y > 0 and ball_velocity_y > 0:
            # If it is possible to hit the ball
            # Ball is closer (ideally: time to hit the ball is shorter)
            # If car is placed behind the ball to opponent side
            return True
    elif agent.team == 1:
        if ball_location_y < 0 and ball_velocity_y < 0:
            # If it is possible to hit the ball
            return True
    return False

def execute_shooting(agent, packet):
    pass
