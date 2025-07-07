from fastapi import APIRouter
from ..mcp.handlers import router as mcp_router

router = APIRouter()
router.include_router(mcp_router)
