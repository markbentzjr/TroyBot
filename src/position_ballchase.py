# Action 95: Get into position to ballchase


def execute_properballchase(agent, packet):
    #car = packet.game_cars[self.index]
    # goto self.target
    pass

# action.py Dependent


def check_positionballchase(agent, packet):
    # if ball is 'behind', then go to position
    # If not, is it possible to hit the ball from closer direction
    car = packet.game_cars[agent.index]
    if car.team == 0:
        # Team 0
        agent.target
    else:
        agent.target

    return False


def ball_section(agent, packet):
    pass
