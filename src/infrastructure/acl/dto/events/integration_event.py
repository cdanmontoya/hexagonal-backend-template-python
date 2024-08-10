from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel

from src.domain.events.event import Event
from src.infrastructure.adapters.input.http.correlation_id.correlation_id import (
    correlation_id_ctx_var,
)


class EventDto(BaseModel):
    id: UUID
    occurred_on: datetime
    source: str
    name: str
    version: str
    data: Any


class IntegrationEvent(BaseModel):
    event: EventDto
    correlation_id: str | None


def to_json(event: Event) -> str:
    event_dto = EventDto(
        id=event.id,
        occurred_on=event.occurred_on,
        source=event.source,
        name=event.name,
        version=event.version,
        data=event.data,
    )

    return IntegrationEvent(
        event=event_dto, correlation_id=correlation_id_ctx_var.get()
    ).model_dump_json()
