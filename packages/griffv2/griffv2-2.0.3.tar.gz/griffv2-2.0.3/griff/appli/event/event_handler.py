from abc import ABC
from typing import TypeVar, Generic

from griff.appli.event.event import Event
from griff.appli.message.message_handler import (
    MessageHandler,
    MessageResponse,
    MessageErrorResponse,
)
from griff.infra.registry.meta_registry import MetaEventHandlerRegistry


class EventSuccessResponse(MessageResponse, ABC):
    pass


class EventErrorResponse(MessageErrorResponse, ABC):
    pass


EventResponse = EventSuccessResponse | EventErrorResponse

EM = TypeVar("EM", bound=Event)
ER = TypeVar("ER", bound=EventResponse)


class EventHandler(
    Generic[EM, ER], MessageHandler[EM, ER], ABC, metaclass=MetaEventHandlerRegistry
):
    ...
