from engine.thread.event_loop_base import EventLoopBaseThread


class ReceiveMessageThread(EventLoopBaseThread):
    def spawn(self) -> None:
        return

    def loop(self) -> bool:
        msg = self.events.socket.recv(1024)
        if msg:
            command = msg.decode("utf8")
            if command:
                self.events.message_received.emit(command)
        return True
