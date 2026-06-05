from engine.channel.event_emitter import EventEmitter, EventSubscriber


class EventBus:
    def __init__(self) -> None:
        self.message_received = EventEmitter()
        self.command_parsed = EventEmitter()
        self.do_action = EventEmitter()

    def on(self, subscriber: EventSubscriber):
        event_emitter = getattr(self, subscriber.__name__, None)
        if isinstance(event_emitter, EventEmitter):
            event_emitter.subscribe(subscriber)
