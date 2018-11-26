# Opponent and friends counter
def check_opponents(agent, packet):
    agent.opponents = 0
    i = 0
    while i < packet.num_cars:
        if packet.game_cars[i] != packet.game_cars[agent.index]:
            agent.opponents += 1
        i += 1


def check_friends(agent, packet):
    agent.friends = 0
    i = 0
    while i < packet.num_cars:
        if (packet.game_cars[i] == packet.game_cars[agent.index]) and (
                i != agent.index):
            agent.friends += 1
        i += 1
