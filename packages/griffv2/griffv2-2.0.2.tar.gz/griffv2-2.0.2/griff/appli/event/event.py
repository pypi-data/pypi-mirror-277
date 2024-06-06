from abc import ABC

from griff.appli.message.message import Message
from pydantic import computed_field


class Event(Message, ABC):
    @computed_field
    def event_name(self) -> str:  # pragma: no cover
        return self.short_classname()
