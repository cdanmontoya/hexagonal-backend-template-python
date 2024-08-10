import asyncio
import logging
import os
from asyncio import AbstractEventLoop
from collections.abc import Callable

from aio_pika import connect_robust
from aio_pika.abc import (
    AbstractIncomingMessage,
    AbstractRobustConnection,
    AbstractRobustChannel,
    AbstractRobustQueue,
    ExchangeType,
)

from src.app.ports.input.events.event_consumer import EventConsumer
from src.infrastructure.acl.dto.events.integration_event import IntegrationEvent
from src.infrastructure.adapters.input.events.python_template.account_inserted import (
    AccountInsertedProcessor,
)
from src.infrastructure.adapters.input.events.python_template.account_not_deleted import (
    AccountNotDeletedProcessor,
)

logger = logging.getLogger(__name__)


class RabbitMqEventConsumer(EventConsumer):
    _loop: AbstractEventLoop
    _connection: AbstractRobustConnection
    _chanel: AbstractRobustChannel
    _queue: AbstractRobustQueue

    def __init__(self):
        self._loop = asyncio.get_event_loop()
        self._connection: AbstractRobustConnection = None
        self._channel: AbstractRobustChannel = None
        self._queue: AbstractRobustQueue = None
        self._event_handlers: dict[str, Callable[IntegrationEvent, None]] = {
            "python_template.AccountNotDeleted": AccountNotDeletedProcessor().handle_event,
            "python_template.AccountInserted": AccountInsertedProcessor().handle_event,
        }

    async def connect(self):
        logger.info("Connecting to RabbitMQ...")
        self._connection = await connect_robust(
            host="localhost", login="guest", password="guest"
        )
        self._channel = await self._connection.channel()
        self._queue = await self._channel.declare_queue(
            os.getenv("APP_NAME", "undefined")
        )

    async def consume(self):
        for handler_name in self._event_handlers.keys():
            await self._channel.declare_exchange(handler_name, type=ExchangeType.FANOUT)
            await self._queue.bind(handler_name)

        await self._queue.consume(self.on_message)

    def process_event(self, event: IntegrationEvent):
        handler = self._event_handlers.get(f"{event.event.source}.{event.event.name}")
        return handler(event)

    async def on_message(self, message: AbstractIncomingMessage) -> None:
        async with message.process():
            integration_event = IntegrationEvent.model_validate_json(
                message.body.decode("utf-8")
            )
            logger.info(f"Processing event: {integration_event}")
            await self.process_event(integration_event)

    async def run(self):
        await self.connect()
        await self.consume()
