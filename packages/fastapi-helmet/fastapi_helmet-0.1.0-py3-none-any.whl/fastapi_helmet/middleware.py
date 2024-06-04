# fastapi_helmet/middleware.py
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from core import HelmetCore


class HelmetMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, **options):
        super().__init__(app)
        self.helmet = HelmetCore(**options)

    async def dispatch(self, request: Request, call_next):
        response: Response = await call_next(request)
        self.helmet.set_headers(response)
        return response
