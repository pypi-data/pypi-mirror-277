from typing import Type, Any

from griff.runtime.components.abstract_runtime_component import (
    RuntimeComponent,
    InjectBindable,
)
from injector import Binder

Injectable = Any | Type[Any]


class InjectRuntimeComponent(InjectBindable, RuntimeComponent):
    def __init__(self, klass: Any, to: Injectable):
        self.klass = klass
        self.to = to

    def configure(self, binder: Binder) -> None:
        binder.bind(self.klass, to=self.to)
