import logging
from contextlib import asynccontextmanager

import uvicorn
from alembic import command
from alembic.config import Config
from fastapi import FastAPI
from injector import Injector

from src.infrastructure.adapters.input.http.account_controller import (
    AccountController,
)
from src.infrastructure.injector.injector import create_injector


class Application:
    log = logging.getLogger("uvicorn")
    __account_controller: AccountController

    def __init__(self, injector: Injector) -> None:
        self.__account_controller = injector.get(AccountController)

    @staticmethod
    def __run_migrations():
        alembic_cfg = Config("alembic.ini")
        command.upgrade(alembic_cfg, "head")

    @asynccontextmanager
    async def lifespan(self, app_: FastAPI):
        self.log.info("Starting up...")
        self.log.info("run alembic upgrade head...")
        self.__run_migrations()
        yield
        self.log.info("Shutting down...")

    def create_app(self) -> FastAPI:
        application = FastAPI(lifespan=self.lifespan)
        application.include_router(self.__account_controller.router)

        return application


app = Application(create_injector()).create_app()

if __name__ == "__main__":
    uvicorn.run(
        "src.infrastructure.adapters.input.http.application:app",
        port=15000,
        host="0.0.0.0",
        reload=True,
    )
