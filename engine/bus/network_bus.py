from socket import AddressFamily, SocketKind, socket


class NetworkBus:
    def __init__(self, *, socket_port: int) -> None:
        self.socket_port = socket_port
        self.socket = socket(AddressFamily.AF_INET, SocketKind.SOCK_DGRAM)
        self.socket.bind(("127.0.0.1", socket_port))
        self.last_receive_ip: tuple[str, int] = ("", 0)

    def response(self, msg: str):
        self.socket.sendto(msg.encode("utf8"), self.last_receive_ip)
