import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from alembic import command
from alembic.config import Config
from fastapi import FastAPI
from injector import Injector

from src.infrastructure.adapters.input.http.account_controller import AccountController


class Application:
    __account_controller: AccountController
    __logger: logging.Logger

    def __init__(self, injector: Injector) -> None:
        self.__logger = logging.getLogger(__name__)
        self.__account_controller = injector.get(AccountController)

    @staticmethod
    def __run_migrations() -> None:
        alembic_cfg = Config("alembic.ini")
        command.upgrade(alembic_cfg, "head")

    @asynccontextmanager
    async def lifespan(self, app_: FastAPI) -> AsyncGenerator:
        # TODO: improve the lifespan method to ensure all logs are shown
        self.__logger.info("Starting up...")
        self.__logger.info("run alembic upgrade head...")
        self.__run_migrations()
        yield
        self.__logger.info("Shutting down...")

    def create_app(self) -> FastAPI:
        application = FastAPI()
        application.include_router(self.__account_controller.router)

        return application
