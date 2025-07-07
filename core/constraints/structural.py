from .base import Constraint


class StructuralConstraint(Constraint):
    """Ensure equipment is within room bounds."""

    def check(self, room):
        violations = []
        for name, info in room.equipment.items():
            x, y, z = info["position"]
            equip = info["instance"]
            if not room.grid.in_bounds(x, y, z):
                violations.append(name)
            elif not room.grid.in_bounds(x + equip.size[0] - 1,
                                        y + equip.size[1] - 1,
                                        z + equip.size[2] - 1):
                violations.append(name)
        return violations
