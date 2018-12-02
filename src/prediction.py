from position import *


def execute_prediction(agent, packet):
    ball_prediction = agent.get_ball_prediction_struct()
    my_car = packet.game_cars[agent.index]

    # Same as this one
    car_location = [my_car.physics.location.x,
                    my_car.physics.location.y,
                    my_car.physics.location.z]

    if ball_prediction is not None:
        for i in range(0, ball_prediction.num_slices):
            if i < 70 and i > 68:
                prediction_slice = ball_prediction.slices[i]
                predicted_location = prediction_slice.physics.location
           # agent.logger.info("At time {}, the ball will be at ({}, {}, {})"
           #                  .format(prediction_slice.game_seconds, location.x, location.y, location.z))
        agent.renderer.draw_line_3d(predicted_location, car_location, agent.renderer.create_color(255, 0, 255, 0))

        return predicted_location
