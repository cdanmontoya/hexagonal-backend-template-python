from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
import uuid
from contextvars import ContextVar

# Create a context variable for the correlation ID
correlation_id_ctx_var = ContextVar("correlation_id", default=None)


class CorrelationIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Extract correlation ID from the request headers or generate a new one
        correlation_id = request.headers.get("X-Correlation-ID", str(uuid.uuid4()))
        # Set the correlation ID in the context variable
        correlation_id_ctx_var.set(correlation_id)

        # Pass the request to the next middleware or route handler
        response = await call_next(request)

        # Add the correlation ID to the response headers
        response.headers["X-Correlation-ID"] = correlation_id

        return response

