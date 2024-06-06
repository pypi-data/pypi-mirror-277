from abc import ABC, abstractmethod

from griff.appli.event.event import Event
from griff.appli.event.event_handler import EventResponse
from griff.appli.message.message_middleware import MessageMiddleware, MessageContext


class EventMiddleware(MessageMiddleware[Event, EventResponse], ABC):
    @abstractmethod
    async def dispatch(
        self, message: Event, context: MessageContext | None = None
    ) -> EventResponse:
        pass
