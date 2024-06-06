from griff.appli.event.event import Event
from griff.appli.event.event_handler import EventResponse
from griff.appli.message.message_dispatcher import MessageDispatcher


class EventDispatcher(MessageDispatcher[Event, EventResponse]):
    ...
