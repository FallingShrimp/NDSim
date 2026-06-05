from engine.bus.event_bus import RoboMasterEventBus
from engine.bus.network_bus import RoboMasterNetworkBus
from engine.thread.handle_action import HandleActionThread
from engine.thread.parse_command import ParseCommandThread
from engine.thread.receive_message import ReceiveMessageThread
import sys


class RoboMaster:
    def __init__(
        self, events: RoboMasterEventBus, network: RoboMasterNetworkBus
    ) -> None:
        self.events = events
        self.network = network
        self.receive_message_thread = ReceiveMessageThread(events, network)
        self.parse_command_thread = ParseCommandThread(events, network)
        self.handle_action_thread = HandleActionThread(events, network)

    def start(self):
        self.receive_message_thread.start()
        self.parse_command_thread.start()
        self.handle_action_thread.start()
        try:
            print(f"正在{self.network.socket_port}上运行")
            while True:
                pass
        except KeyboardInterrupt:
            self.receive_message_thread.stop()
            self.parse_command_thread.stop()
            self.handle_action_thread.stop()
            self.network.socket.close()
            sys.exit(0)
