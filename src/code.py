import math
import time # For timings

from rlbot.agents.base_agent import BaseAgent, SimpleControllerState
from rlbot.utils.structures.game_data_struct import GameTickPacket

# Personal codes (classes)
from position import Vector3

class TroyBot(BaseAgent):

    def initialize_agent(self):
        # This state is initialized once before the bot starts up
        self.controller_state = SimpleControllerState()
        self.clear_state()
        
        # Game state
        self.action = 0
        

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

        return self.controller_state
