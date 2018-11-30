from position import Vector3

def closest(agent, packet):
    # Returns the closest car to the ball
    # Ideally returns the fastest car to hit the ball
    distance = 9999
    ball = Vector3(packet.game_ball.physics.location.x, packet.game_ball.physics.location.y, packet.game_ball.physics.location.z)
    closest = None
    i = 0
    while i < packet.num_cars:
        car = packet.game_cars[i]
        car_position = Vector3(car.physics.location.x, car.physics.location.y, car.physics.location.z)
        if car != packet.game_cars[agent.index] and car_position.real_distance(ball) < distance:
            distance = car_position.real_distance(ball)
            closest = car
        i += 1
    return closest