import math
import time  # For timings

from rlbot.agents.base_agent import BaseAgent, SimpleControllerState
from rlbot.utils.structures.game_data_struct import GameTickPacket


# Personal codes (classes)
from position import *
from counter import *
from quickchat import quick_chat
from state import clear_state
from action import check_action
from boost import goto_boost
from kickoff import *
from ballchase import execute_ballchase
from position_ballchase import execute_properballchase
from demo import demo
from team import team_check
from prediction import execute_prediction

class TroyBot(BaseAgent):
    def initialize_agent(self):
        # Controller state is initialized once before the bot starts up and cleared
        self.controller_state = SimpleControllerState()
        clear_state(self)

        # False when tick is not started, else True
        self.init = False

        # Team code
        self.team = -1

        # Opponents and friends count ingame
        self.opponents = 0
        self.friends = 0

        # Chat ticker
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

    def get_output(self, packet: GameTickPacket) -> SimpleControllerState:
        clear_state(self)
        self.renderer.begin_rendering()

        execute_prediction(self, packet)
        
        if self.init == False:
            check_opponents(self, packet)
            check_friends(self, packet)
            team_check(self, packet)
            self.init = True

        check_action(self, packet)
        action = self.action
        # print(action)
        if action == 0:
            kickoff(self, packet)
            # print("Not going to boost")
        elif action == 3:
            if goto_boost(self, packet) == 0:
                # print("ballchase")
                execute_ballchase(self, packet)
            # print("Going to boost")
        elif action == 4:
            demo(self, packet)
        elif action == 99:
            execute_ballchase(self, packet)
        elif action == 95:
            execute_properballchase(self, packet)

        quick_chat(self)

        self.renderer.end_rendering()

        return self.controller_state
