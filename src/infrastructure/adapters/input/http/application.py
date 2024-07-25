import logging
import os
from contextlib import asynccontextmanager

import uvicorn
from alembic import command
from alembic.config import Config
from dotenv import load_dotenv
from fastapi import FastAPI
from injector import Injector

from src.infrastructure.adapters.input.http.account_controller import (
    AccountController,
)
from src.infrastructure.injector.injector import create_injector

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("uvicorn")


class Application:
    __account_controller: AccountController

    def __init__(self, injector: Injector) -> None:
        self.__account_controller = injector.get(AccountController)

    @staticmethod
    def __run_migrations():
        alembic_cfg = Config("alembic.ini")
        command.upgrade(alembic_cfg, "head")

    @asynccontextmanager
    async def lifespan(self, app_: FastAPI):
        # TODO: improve the lifespan method to ensure all logs are shown
        logger.info("Starting up...")
        logger.info("run alembic upgrade head...")
        self.__run_migrations()
        yield
        logger.info("Shutting down...")

    def create_app(self) -> FastAPI:
        #application = FastAPI(lifespan=self.lifespan)
        application = FastAPI()
        application.include_router(self.__account_controller.router)

        return application


app = Application(create_injector()).create_app()

if __name__ == "__main__":
    load_dotenv()
    uvicorn.run(
        "src.infrastructure.adapters.input.http.application:app",
        port=int(os.getenv("APP_PORT", 8080)),
        host="0.0.0.0",
        reload=True,
    )
