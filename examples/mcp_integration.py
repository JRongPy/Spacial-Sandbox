import uvicorn

from core.spatial.room import Room
from core.placement.engine import PlacementEngine
from core.constraints.validator import Validator
from core.constraints.clearance import ClearanceConstraint
from core.constraints.structural import StructuralConstraint
from interfaces.mcp.server import create_app

room = Room(10, 10, 3)
engine = PlacementEngine(room)
validator = Validator([StructuralConstraint(), ClearanceConstraint()])

app = create_app(room, engine, validator)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
