from typing import List
from fastapi import WebSocket, APIRouter

router = APIRouter()


class ConnectionManager:
    def __init__(self):
        self.active: List[WebSocket] = []
        self.room = None
        self.engine = None
        self.validator = None

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active.remove(websocket)

    async def broadcast(self, message):
        for ws in list(self.active):
            await ws.send_json(message)


manager = ConnectionManager()


@router.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await manager.connect(ws)
    try:
        while True:
            await ws.receive_text()
    except Exception:
        pass
    finally:
        manager.disconnect(ws)
