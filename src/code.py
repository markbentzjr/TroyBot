import math
import time  # For timings

from rlbot.agents.base_agent import BaseAgent, SimpleControllerState
from rlbot.utils.structures.game_data_struct import GameTickPacket


# Personal codes (classes)
from position import *
from counter import *
from quickchat import quick_chat

class TroyBot(BaseAgent):
    def initialize_agent(self):
        # This state is initialized once before the bot starts up
        self.controller_state = SimpleControllerState()
        self.clear_state()
        self.opponents = 0
        self.friends = 0
        self.chat = 0
        # Game state
        self.action = -1

        # Action -1: AFK
        # Action  0: Kickoff
        # Action  1: Defend post
        # Action  2: Attack
        # Action  3: Collect boost
        # Action  4: Demo
        # Action 95: Get into position to ballchase
        # Action 99: Ballchase

        #self.tick = 0
        self.target = None

        self.field_info = self.get_field_info()

    # Clears bot controller state
    def clear_state(self):
        # Read https://github.com/RLBot/RLBotPythonExample/wiki/Input-and-Output-Data for full documentation
        self.controller_state.throttle = 0
        self.controller_state.steer = 0
        self.controller_state.pitch = 0
        self.controller_state.yaw = 0
        self.controller_state.roll = 0
        self.controller_state.boost = False
        self.controller_state.jump = False
        self.controller_state.handbrake = False

    def get_output(self, packet: GameTickPacket) -> SimpleControllerState:
        self.clear_state()

        # self.check_opponents(packet)
        # self.check_friends(packet)

        action = self.check_action(packet)

        if action == 0:
            self.kickoff(packet)
            # print("Not going to boost")
        elif action == 3:
            self = self.goto_boost(packet)
            # print("Going to boost")
        elif action == 4:
            self = self.demo(packet)
        elif action == 99:
            self = self.ballchase(packet)
        elif action == 95:
            self = self.positioning_ballchase(packet)

        quick_chat(self)

        return self.controller_state

# Decision function

    def check_action(self, packet):
        # For 1 opponent
        own_car = packet.game_cars[self.index]

        if self.check_kickoff(packet) == True:
            self.action = 0
        elif (own_car.boost == 0.0):
            self.action = 3
        else:
            if self.check_position(packet) == True:
                self.action = 95
            else:
                self.action = 99
        #print(self.check_kickoff(packet))
        #print(self.action)
        # For 2 opponents
        # For 3/4 opponents
        return self.action



# Action 3: Boost

    def goto_boost(self, packet):
        #print("Going for boost")
        boost_location = []
        pads = self.field_info.boost_pads
        for i in range(len(pads)):
            if (pads[i].is_full_boost == True) and (
                    packet.game_boosts[i].is_active == True):
                # if (i.is_full_boost == True):
                boost_location.append(
                    Vector3(pads[i].location.x, pads[i].location.y,
                            pads[i].location.z))

        own_car = packet.game_cars[self.index]
        own_car_location = Vector3(own_car.physics.location.x,
                                   own_car.physics.location.y,
                                   own_car.physics.location.z)
        #print(own_car.physics.location.x, own_car.physics.location.y, own_car.physics.location.z)

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
        #print(rad)

        self.controller_state.handbrake = False
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

        self.controller_state.throttle = 1.0
        if abs(rad) > math.pi / 2 and distance > 500:
            self.controller_state.handbrake = True
            self.controller_state.throttle = 0.6

        self.controller_state.steer = turn
        #self.tick += 1
        return self

# Action 0: Kickoff

    def check_kickoff(self, packet):
        ball = packet.game_ball.physics
        #print(ball.velocity.x, ball.velocity.y, ball.velocity.z)
        Condition0Loc = Vector3(0, 0, 93)
        Condition0Vel = Vector3(0, 0, 0)
        Location = Vector3(ball.location.x, ball.location.y,
                           math.ceil(ball.location.z))
        Velocity = Vector3(ball.velocity.x, ball.velocity.y, ball.velocity.z)
        if Location.real_distance(
                Condition0Loc) < 1 and Velocity.real_distance(
                    Condition0Vel) < 1:
            return True
        return False

    def kickoff(self, packet):
        self = self.ballchase(packet)
        self.controller_state.boost = True
        return self

# Action 99: Ballchase

    def ballchase(self, packet):
        ball_location = Vector3(packet.game_ball.physics.location.x,
                                packet.game_ball.physics.location.y,
                                packet.game_ball.physics.location.z)
        ball_velocity = Vector3(packet.game_ball.physics.velocity.x,
                                packet.game_ball.physics.velocity.y,
                                packet.game_ball.physics.velocity.z)
        my_car = packet.game_cars[self.index]
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

        self.controller_state.throttle = 1.0
        self.controller_state.steer = turn
        self.controller_state.handbrake = False
        #print(car_location.real_distance(ball_location))
        #print(ball_velocity.z)
        if (ball_location.z < 150) and abs(ball_velocity.z) < 200:
            if (car_location.real_distance(ball_location) <
                1500) and (abs(steer_correction_radians) < math.pi / 4):
                self.controller_state.boost = True
            else:
                if (abs(steer_correction_radians) < math.pi / 2):
                    self.controller_state.handbrake = True
                self.controller_state.boost = False
        else:
            self.controller_state.boost = False
        return self

# Action 4: Demolitions

    def demo(self, packet):
        return self


# Action 95: Get into position to ballchase

    def positioning_ballchase(self, packet):
        #car = packet.game_cars[self.index]
        #goto self.target
        return self

    def check_position(self, packet):
        # if ball is 'behind', then go to position
        # If not, is it possible to hit the ball from closer direction
        car = packet.game_cars[self.index]
        if car.team == 0:
            # Team 0
            self.target
        else:
            self.target

        return False

    def ball_section(self, packet):
        pass
