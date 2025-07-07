from fastapi import FastAPI
from pydantic import BaseModel

from ..api.websocket import manager
from ..api.rest import router as api_router
from .handlers import router as mcp_router


def create_app(room, engine, validator):
    app = FastAPI()

    app.include_router(api_router)

    @app.on_event("startup")
    async def startup_event():
        manager.room = room
        manager.engine = engine
        manager.validator = validator
        # expose engine and validator to handlers
        mcp_router.room = room
        mcp_router.engine = engine
        mcp_router.validator = validator
        mcp_router.manager = manager

    return app
