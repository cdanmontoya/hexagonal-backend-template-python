import uvicorn
from fastapi import FastAPI

from python_template.infrastructure.server import endpoints


def create_app() -> FastAPI:
    application = FastAPI()
    application.include_router(endpoints.router)

    return application


app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "python_template.infrastructure.server.application:app",
        port=5001,
        host="0.0.0.0",
        reload=True,
    )
