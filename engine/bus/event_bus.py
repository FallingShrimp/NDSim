from engine.channel.event_emitter import EventEmitter, EventSubscriber
from socket import AddressFamily, SocketKind, socket


class EventBus:
    def __init__(self, *, socket_port: int) -> None:
        self.socket_port = socket_port
        self.socket = socket(AddressFamily.AF_INET, SocketKind.SOCK_DGRAM)
        self.socket.bind(("127.0.0.1", socket_port))
        self.message_received = EventEmitter()
        self.command_parsed = EventEmitter()
        self.do_action = EventEmitter()

    def on(self, subscriber: EventSubscriber):
        def wrapper():
            subscriber()

        event_emitter = getattr(self, subscriber.__name__, None)
        if isinstance(event_emitter, EventEmitter):
            event_emitter.subscribe(wrapper)
