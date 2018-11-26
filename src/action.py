# Decision function


def check_action(agent, packet):
    # For 1 opponent
    own_car = packet.game_cars[agent.index]

    if agent.check_kickoff(packet) == True:
        agent.action = 0
    elif (own_car.boost == 0.0):
        agent.action = 3
    else:
        if agent.check_position(packet) == True:
            agent.action = 95
        else:
            agent.action = 99
    # print(self.check_kickoff(packet))
    # print(self.action)
    # For 2 opponents
    # For 3/4 opponents
