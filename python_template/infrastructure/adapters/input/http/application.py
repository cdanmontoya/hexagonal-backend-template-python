import uvicorn
from fastapi import FastAPI

from python_template.infrastructure.adapters.input.http.account_controller import (
    AccountController,
)


def create_app() -> FastAPI:
    application = FastAPI()
    application.include_router(AccountController().router)

    return application


app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "python_template.infrastructure.adapters.input.http.application:app",
        port=15000,
        host="0.0.0.0",
        reload=True,
    )
