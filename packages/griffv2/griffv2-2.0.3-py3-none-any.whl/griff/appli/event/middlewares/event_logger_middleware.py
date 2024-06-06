from griff.appli.event.event import Event
from griff.appli.event.event_handler import EventResponse
from griff.appli.event.event_middleware import EventMiddleware
from griff.appli.message.message_middleware import MessageContext
from loguru import logger


class EventLoggerMiddleware(EventMiddleware):
    async def dispatch(
        self, message: Event, context: MessageContext | None = None
    ) -> EventResponse:
        logger.info(f"dispatch event: {message.short_classname()}")
        logger.debug(message.model_dump())
        response = await self._next.dispatch(message, context)
        logger.debug(response.model_dump())
        return response
