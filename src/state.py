# Clears bot controller state
def clear_state(agent):
    # Read https://github.com/RLBot/RLBotPythonExample/wiki/Input-and-Output-Data for full documentation
    agent.controller_state.throttle = 0
    agent.controller_state.steer = 0
    agent.controller_state.pitch = 0
    agent.controller_state.yaw = 0
    agent.controller_state.roll = 0
    agent.controller_state.boost = False
    agent.controller_state.jump = False
    agent.controller_state.handbrake = False
