import uvicorn
from fastapi import FastAPI

from python_template.infrastructure.adapters.input.http.account_controller import (
    AccountController,
)
from python_template.infrastructure.injector.injector import injector


class Application:
    __account_controller: AccountController

    def __init__(self, account_controller: AccountController):
        self.__account_controller = account_controller

    def create_app(self) -> FastAPI:
        application = FastAPI()
        application.include_router(self.__account_controller.router)

        return application


app = Application(injector.get(AccountController)).create_app()

if __name__ == "__main__":
    uvicorn.run(
        "python_template.infrastructure.adapters.input.http.application:app",
        port=15000,
        host="0.0.0.0",
        reload=True,
    )
