import sys
import os

sys.path.append(os.getcwd())
from engine.bus.network_bus import NetworkBus
from rmtt_simulator import EventBus, RoboMaster

events = EventBus()
network = NetworkBus(socket_port=8889)


@events.on
def do_action(main, *args):
    match main:
        case "command":
            network.response("ok")


simulator = RoboMaster(events, network)
simulator.start()
