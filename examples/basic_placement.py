from core.spatial.room import Room
from core.placement.engine import PlacementEngine
from core.constraints.validator import Validator
from core.constraints.clearance import ClearanceConstraint
from core.constraints.structural import StructuralConstraint


room = Room(10, 10, 3)
engine = PlacementEngine(room)
validator = Validator([StructuralConstraint(), ClearanceConstraint()])

engine.place('chiller', 'c1', (1, 1, 0))
print(validator.validate(room))
