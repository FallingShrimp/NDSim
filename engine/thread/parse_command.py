from engine.thread.event_loop_base import EventLoopBase


class ParseCommandThread(EventLoopBase):
    def spawn(self) -> None:
        self.events.message_received.subscribe(self.parse)

    def loop(self) -> bool:
        return True

    def parse(self, msg: str):
        parts = msg.split(" ")
        main = parts[0]
        args = parts[1:]
        self.events.command_parsed.emit(main, args)
