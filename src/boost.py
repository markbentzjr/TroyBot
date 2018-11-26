from position import *
# Action 3: Boost

def goto_boost(agent, packet):
    #print("Going for boost")
    boost_location = []
    pads = agent.field_info.boost_pads
    for i in range(len(pads)):
        if (pads[i].is_full_boost == True) and (
                packet.game_boosts[i].is_active == True):
            # if (i.is_full_boost == True):
            boost_location.append(
                Vector3(pads[i].location.x, pads[i].location.y,
                        pads[i].location.z))

    own_car = packet.game_cars[agent.index]
    own_car_location = Vector3(own_car.physics.location.x,
                               own_car.physics.location.y,
                               own_car.physics.location.z)
    #print(own_car.physics.location.x, own_car.physics.location.y, own_car.physics.location.z)
    if len(boost_location) == 0:
        return 0

    boost_choose_location = boost_location[0]
    distance = own_car_location.real_distance(boost_choose_location)
    for i in range(len(boost_location)):
        boost = boost_location[i]
        """ print(i)
            print(own_car_location.real_distance(boost))
            print("\n") """
        if (own_car_location.real_distance(boost) < distance):
            distance = own_car_location.real_distance(boost_location[i])
            boost_choose_location = boost_location[i]

    own_dir = facing(own_car)
    #print(boost_choose.x, boost_choose.y, boost_choose.z)
    car_to_target = boost_choose_location - own_car_location
    #print(car_to_target.x, car_to_target.y)
    rad = own_dir.correction_2D(car_to_target)
    # print(rad)

    agent.controller_state.handbrake = False
    if rad > 0.1:
        turn = -1.0
    elif rad < -0.1:
        turn = 1.0
    else:
        turn = 0
    """ if abs(rad) > (math.pi * 1/3):
            self.controller_state.handbrake = True
        else:
            self.controller_state.handbrake = False """

    agent.controller_state.throttle = 1.0
    if abs(rad) > math.pi / 2 and distance > 500:
        agent.controller_state.handbrake = True
        agent.controller_state.throttle = 0.6

    agent.controller_state.steer = turn
    #self.tick += 1
    return len(boost_location)
