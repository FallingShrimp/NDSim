import sys
import os

sys.path.append(os.getcwd())
from rmtt_simulator import EventBus, RoboMaster

events = EventBus(socket_port=8889)


@events.on
def do_action(main, *args):
    print(main, args)


simulator = RoboMaster(events)
simulator.start()
