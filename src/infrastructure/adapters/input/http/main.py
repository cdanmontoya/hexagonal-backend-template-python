import asyncio
import os

import uvicorn
from dotenv import load_dotenv

from src.infrastructure.adapters.input.events.rabbit_mq_event_consumer import (
    RabbitMqEventConsumer,
)
from src.infrastructure.adapters.input.http.application import Application
from src.infrastructure.config.injector.injector import create_injector

app = Application(create_injector()).create_app()


@app.on_event("startup")
async def startup_event():
    loop = asyncio.get_running_loop()
    task = loop.create_task(RabbitMqEventConsumer().run())
    await task


if __name__ == "__main__":
    load_dotenv()

    uvicorn.run(
        "src.infrastructure.adapters.input.http.main:app",
        port=int(os.getenv("APP_PORT", 8080)),
        host="0.0.0.0",
        reload=True,
    )
