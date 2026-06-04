from engine.thread.event_loop_base import EventLoopBase


class HandleActionThread(EventLoopBase):
    def spawn(self) -> None:
        self.action_stack: list[tuple[str, list]] = []
        self.events.command_parsed.subscribe(
            lambda main, args: self.action_stack.append((main, args))
        )

    def loop(self) -> bool:
        main, args = self.action_stack.pop()
        match main:
            case "takeoff":
                print(1)
            case "forward":
                print("f", args)
        return True
