from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class PlaceRequest(BaseModel):
    equip_type: str
    name: str
    x: int
    y: int
    z: int


@router.post("/place")
async def place(req: PlaceRequest):
    equip = router.engine.place(req.equip_type, req.name, (req.x, req.y, req.z))
    validation = router.validator.validate(router.room)
    await router.manager.broadcast(validation)
    return {"placed": equip.name, "validation": validation}
