from abc import ABC

from griff.appli.message.message_handler import MessageResponse, MessageErrorResponse
from griff.infra.registry.meta_endpoint_controller_registry import (
    MetaEndpointControllerRegistry,
)
from griff.utils.inspect_utils import find_bound_method_to_object
from starlette.responses import JSONResponse


class ApiController(ABC, metaclass=MetaEndpointControllerRegistry):
    def __init__(self):
        """
        Auto register endpoint in fastApi router
        """
        endpoint_list = MetaEndpointControllerRegistry.get_endpoint_registry()[
            type(self)
        ]
        self._endpoints = list()
        for endpoint in endpoint_list:
            endpoint_route = MetaEndpointControllerRegistry.get_full_route_for_endpoint(
                controller=self, endpoint=endpoint
            )
            if endpoint_route is None:  # pragma: no cover
                continue
            self._endpoints.append(
                {
                    "route": endpoint_route,
                    "method": endpoint.http_method,
                    "func": find_bound_method_to_object(self, endpoint.endpoint),
                    "return_code": endpoint.http_success_code,
                }
            )

    def get_endpoints(self):
        return self._endpoints

    @staticmethod
    def prepare_response(
        response: MessageResponse | MessageErrorResponse,
    ) -> MessageResponse | JSONResponse:  # pragma: no cover
        if response.is_success:
            return response
        return JSONResponse(
            status_code=response.code,
            content=response.error.model_dump(),  # type: ignore
        )
