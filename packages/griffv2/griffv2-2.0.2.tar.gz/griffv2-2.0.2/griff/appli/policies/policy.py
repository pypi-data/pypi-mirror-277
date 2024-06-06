from abc import ABC, abstractmethod
from typing import Any

from griff.utils.errors import BaseError
from returns.result import Result


class Policy(ABC):
    @abstractmethod
    async def verify(self, *args, **kwargs) -> Result[Any, BaseError]:
        ...
