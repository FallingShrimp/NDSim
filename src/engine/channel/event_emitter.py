from collections.abc import Callable
from typing import Any

EventSubscriber = Callable[..., None]


class EventEmitter:
    def __init__(self) -> None:
        self.subscribers: list[EventSubscriber] = []

    def subscribe(self, subscriber: EventSubscriber):
        self.subscribers.append(subscriber)

    def emit(self, *data: Any):
        for subscriber in self.subscribers:
            subscriber(*data)
