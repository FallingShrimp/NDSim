from engine.channel.event_emitter import EventEmitter
from socket import AddressFamily, SocketKind, socket


class EventBus:
    def __init__(self, *, socket_port: int) -> None:
        self.socket = socket(AddressFamily.AF_INET, SocketKind.SOCK_DGRAM)
        self.socket.bind(("127.0.0.1", socket_port))
        self.message_received = EventEmitter()
        self.command_parsed = EventEmitter()
