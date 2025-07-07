from core.spatial.room import Room
from core.placement.engine import PlacementEngine
from core.constraints.validator import Validator
from core.constraints.clearance import ClearanceConstraint
from core.constraints.structural import StructuralConstraint


def test_clearance_violation():
    room = Room(5, 5, 3)
    engine = PlacementEngine(room)
    validator = Validator([StructuralConstraint(), ClearanceConstraint(clearance=1)])
    engine.place('chiller', 'c1', (0, 0, 0))
    engine.place('chiller', 'c2', (1, 0, 0))
    result = validator.validate(room)
    assert result['ClearanceConstraint']
