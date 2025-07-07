from core.spatial.room import Room
from core.placement.engine import PlacementEngine
from core.constraints.validator import Validator
from core.constraints.clearance import ClearanceConstraint
from core.constraints.structural import StructuralConstraint


def test_validator_no_violations():
    room = Room(5, 5, 3)
    engine = PlacementEngine(room)
    validator = Validator([StructuralConstraint(), ClearanceConstraint()])
    engine.place('chiller', 'c1', (0, 0, 0))
    result = validator.validate(room)
    assert all(not v for v in result.values())
