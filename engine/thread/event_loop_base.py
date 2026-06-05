from abc import ABC, abstractmethod
from threading import Thread

from engine.bus.event_bus import EventBus
from engine.bus.network_bus import NetworkBus


class EventLoopBaseThread(Thread, ABC):
    def __init__(self, events: EventBus, network: NetworkBus) -> None:
        super().__init__()
        self.events = events
        self.network = network
        self.running = False

    def run(self) -> None:
        self.running = True
        self.spawn()
        while self.running:
            if not self.loop():
                break

    def stop(self):
        self.running = False

    @abstractmethod
    def spawn(self) -> None:
        pass

    @abstractmethod
    def loop(self) -> bool:
        pass
