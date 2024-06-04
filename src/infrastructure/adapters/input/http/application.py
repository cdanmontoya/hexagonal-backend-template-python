import uvicorn
from fastapi import FastAPI
from injector import Injector

from src.infrastructure.adapters.input.http.account_controller import (
    AccountController,
)
from src.infrastructure.injector.injector import create_injector


class Application:
    __account_controller: AccountController

    def __init__(self, injector: Injector) -> None:
        self.__account_controller = injector.get(AccountController)

    def create_app(self) -> FastAPI:
        application = FastAPI()
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
