import math
import time

from rlbot.utils.structures.quick_chats import QuickChats

# Quickchat
def quick_chat(agent):
    #print(math.floor(time.time()))
    if (math.floor(time.time()) % 32 == 0) and math.floor(
            time.time()) != agent.chat:
        agent.send_quick_chat(QuickChats.CHAT_EVERYONE,
                             QuickChats.Reactions_Siiiick)
        agent.chat = math.floor(time.time())
    elif (math.floor(time.time()) % 32 == 8) and math.floor(
            time.time()) != agent.chat:
        agent.send_quick_chat(QuickChats.CHAT_EVERYONE,
                             QuickChats.Apologies_Sorry)
        agent.chat = math.floor(time.time())
    elif (math.floor(time.time()) % 32 == 16) and math.floor(
            time.time()) != agent.chat:
        agent.send_quick_chat(QuickChats.CHAT_EVERYONE,
                             QuickChats.PostGame_EverybodyDance)
        agent.chat = math.floor(time.time())
    elif (math.floor(time.time()) % 32 == 24) and math.floor(
            time.time()) != agent.chat:
        agent.send_quick_chat(QuickChats.CHAT_EVERYONE,
                             QuickChats.Compliments_Thanks)
        agent.chat = math.floor(time.time())
