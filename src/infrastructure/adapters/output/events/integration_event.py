from typing import Any

from pydantic import BaseModel

from src.domain.events.event import Event
from src.infrastructure.adapters.input.http.correlation_id.correlation_id import (
    correlation_id_ctx_var,
)


class IntegrationEvent(BaseModel):
    event: Any
    correlation_id: str


def to_json(event: Event) -> str:
    return IntegrationEvent(
        event=event, correlation_id=correlation_id_ctx_var.get()
    ).json()
