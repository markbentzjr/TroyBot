# Opponent and friends counter
def check_opponents(agent, packet):
    agent.opponents = 0
    for i in packet.num_cars:
        if packet.game_cars[i] != packet.game_cars[agent.index]:
            agent.opponents += 1


def check_friends(agent, packet):
    agent.friends = 0
    for i in packet.num_cars:
        if (packet.game_cars[i] == packet.game_cars[agent.index]) and (
                i != agent.index):
            agent.friends += 1
