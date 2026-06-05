from engine.thread.event_loop_base import EventLoopBaseThread


class ReceiveMessageThread(EventLoopBaseThread):
    def spawn(self) -> None:
        return

    def loop(self) -> bool:
        try:
            msg, ip = self.network.socket.recvfrom(1024)
            if msg:
                command = msg.decode("utf8")
                if command:
                    self.network.last_receive_ip = ip
                    self.events.message_received.emit(command)
            return True
        except OSError:
            return False
