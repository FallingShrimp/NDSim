from engine.bus.event_bus import EventBus
from engine.thread.handle_action import HandleActionThread
from engine.thread.parse_command import ParseCommandThread
from engine.thread.receive_message import ReceiveMessageThread


class NDSimulator:
    def __init__(self, events: EventBus) -> None:
        self.events = events
        self.receive_message_thread = ReceiveMessageThread(events)
        self.parse_command_thread = ParseCommandThread(events)
        self.handle_action_thread = HandleActionThread(events)

    def start(self):
        self.receive_message_thread.start()
        self.parse_command_thread.start()
        self.handle_action_thread.start()
