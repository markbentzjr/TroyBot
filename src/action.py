# Decision function

from kickoff import check_kickoff
from position_ballchase import check_positionballchase
from shooting import check_shooting

def check_action(agent, packet):
    # For 1 opponent
    own_car = packet.game_cars[agent.index]

    if check_kickoff(agent, packet) == True:
        agent.action = 0
    elif (own_car.boost == 0.0):
        agent.action = 3
    elif check_shooting(agent, packet) == True:
        agent.action = 2
    else:
        if check_positionballchase(agent, packet) == True:
            agent.action = 95
        else:
            agent.action = 99
    # print(self.check_kickoff(packet))
    # print(self.action)
    # For 2 opponents
    # For 3/4 opponents
