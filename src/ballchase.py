import math

from position import *

# Action 99: Ballchase
def execute_ballchase(agent, packet):
    # Need to use Vector3 class to locate position. ball_location is now an object of type Vector3
    ball_location = Vector3(packet.game_ball.physics.location.x,
                            packet.game_ball.physics.location.y,
                            packet.game_ball.physics.location.z)
    
    ball_velocity = packet.game_ball.physics.velocity
    
    my_car = packet.game_cars[agent.index]

    # Same as this one
    car_location = Vector3(my_car.physics.location.x,
                           my_car.physics.location.y,
                           my_car.physics.location.z)
    
    car_direction = facing(my_car)
    car_to_ball = ball_location - car_location

    steer_correction_radians = car_direction.correction_2D(car_to_ball)

    if steer_correction_radians > 0.1:
        if abs(steer_correction_radians) < math.pi / 4:
            turn = -0.5
        else:
            turn = -1.0
    elif steer_correction_radians < -0.1:
        if abs(steer_correction_radians) < math.pi / 4:
            turn = 0.5
        else:
            turn = 1.0
    else:
        turn = 0

    agent.controller_state.throttle = 1.0
    agent.controller_state.steer = turn
    agent.controller_state.handbrake = False
    # print(car_location.real_distance(ball_location))
    # print(ball_velocity.z)
    if (ball_location.z < 150) and abs(ball_velocity.z) < 200:
        if (car_location.real_distance(ball_location) < 1500):
            if (abs(steer_correction_radians) < math.pi / 6):
                agent.controller_state.boost = True
            elif (abs(steer_correction_radians) < math.pi / 2):
                agent.controller_state.boost = False
            else:
                agent.controller_state.boost = False
                agent.controller_state.throttle = 0.5
                agent.controller_state.handbrake = True
        elif (car_location.real_distance(ball_location) < 3000):
            if (abs(steer_correction_radians) <= math.pi / 4) and my_car.boost > 50:
                agent.controller_state.boost = True
            elif abs(steer_correction_radians) > math.pi / 4:
                agent.controller_state.boost = False
                agent.controller_state.handbrake = True
            else:
                agent.controller_state.boost = False
        else:
            if (abs(steer_correction_radians) > math.pi * 0.5):
                agent.controller_state.handbrake = True
                agent.controller_state.boost = False
            else:
                agent.controller_state.boost = True
    else:
        agent.controller_state.boost = False
        if (car_location.real_distance(ball_location) > 3000) and (abs(steer_correction_radians) < math.pi / 4) and my_car.boost > 50:
            agent.controller_state.boost = True
    
    # Rendering path to ballchase
    # ball_location and car_location is a Vector3 object, and class Vector3 has function tuple.
    # To get tuple of a Vector3 object, you just need to put vec3object.tuple(), since tuple is a function of a class (Vector3)
    agent.renderer.draw_line_3d(ball_location.tuple(), car_location.tuple(), agent.renderer.create_color(255, 255, 255, 0))
