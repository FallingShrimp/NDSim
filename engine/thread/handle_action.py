from engine.thread.event_loop_base import EventLoopBaseThread


class HandleActionThread(EventLoopBaseThread):
    def spawn(self) -> None:
        self.action_stack: list[tuple[str, list]] = []
        self.events.command_parsed.subscribe(
            lambda main, args: self.action_stack.append((main, args))
        )

    def loop(self) -> bool:
        if len(self.action_stack) > 0:
            self.events.do_action.emit(*self.action_stack.pop())
        return True
