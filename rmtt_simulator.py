from engine.bus.event_bus import EventBus
from engine.thread.handle_action import HandleActionThread
from engine.thread.parse_command import ParseCommandThread
from engine.thread.receive_message import ReceiveMessageThread
import sys


class RoboMaster:
    def __init__(self, events: EventBus) -> None:
        self.events = events
        self.receive_message_thread = ReceiveMessageThread(events)
        self.parse_command_thread = ParseCommandThread(events)
        self.handle_action_thread = HandleActionThread(events)

    def start(self):
        self.receive_message_thread.start()
        self.parse_command_thread.start()
        self.handle_action_thread.start()
        try:
            print(f"正在{self.events.socket_port}上运行")
            while True:
                pass
        except KeyboardInterrupt:
            self.receive_message_thread.stop()
            self.parse_command_thread.stop()
            self.handle_action_thread.stop()
            self.events.socket.close()
            sys.exit(0)
