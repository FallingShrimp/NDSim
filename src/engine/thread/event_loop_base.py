from abc import ABC, abstractmethod
from threading import Thread

from nd_sim import EventBus


class EventLoopBase(Thread, ABC):
    def __init__(self, events: EventBus) -> None:
        self.events = events
        self.running = False

    def run(self) -> None:
        self.running = True
        while self.running:
            if not self.loop():
                break
        self.running = False

    def stop(self):
        self.running = False

    @abstractmethod
    def spawn(self) -> None:
        pass

    @abstractmethod
    def loop(self) -> bool:
        pass
