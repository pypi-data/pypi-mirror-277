from abc import ABC

from pydantic import BaseModel


class ApiSchema(BaseModel, ABC):  # pragma: no cover
    ...
