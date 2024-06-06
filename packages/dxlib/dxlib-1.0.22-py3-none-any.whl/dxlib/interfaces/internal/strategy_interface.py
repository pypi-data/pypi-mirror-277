from __future__ import annotations

from .internal_interface import InternalInterface
from ..servers.endpoint import Endpoint, Method, EndpointScheme
from ...core import Strategy


class StrategyInterface(InternalInterface):
    def __init__(self, strategy, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.strategy: Strategy = strategy

    @Endpoint.http(Method.POST, "/execute", "Executes a single observation and returns the result")
    async def execute(self, observation: any, position, history):
        return self.strategy.execute(observation, position, history)

    @property
    def endpoints(self, endpoint_scheme=EndpointScheme.HTTP):
        return self.get_endpoints(endpoint_scheme)
