from griff.appli.event.event import Event
from griff.appli.event.event_dispatcher import EventDispatcher
from griff.appli.event.event_handler import EventResponse, EventHandler
from griff.appli.message.message_bus import MessageBus
from injector import inject


class EventBus(MessageBus[Event, EventResponse, EventHandler]):
    @inject
    def __init__(self, dispatcher: EventDispatcher) -> None:
        super().__init__(dispatcher)
