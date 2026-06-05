import sys
import os

sys.path.append(os.getcwd())
from engine.bus.network_bus import RoboMasterNetworkBus
from rmtt_simulator import RoboMasterEventBus, RoboMaster

events = RoboMasterEventBus()
network = RoboMasterNetworkBus(socket_port=8889)


@events.on
def do_action(main, *args):
    print(main, args)
    match main:
        case "command":
            network.response("ok")


simulator = RoboMaster(events, network)
simulator.start()
