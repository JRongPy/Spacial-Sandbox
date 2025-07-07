from .base import Constraint
from ..spatial.collision import AABB


class ClearanceConstraint(Constraint):
    """Ensure equipment has clearance around it."""

    def __init__(self, clearance=1):
        self.clearance = clearance

    def check(self, room):
        violations = []
        for name, info in room.equipment.items():
            equip = info["instance"]
            x, y, z = info["position"]
            aabb = AABB((x - self.clearance, y - self.clearance, z),
                        (equip.size[0] + 2 * self.clearance,
                         equip.size[1] + 2 * self.clearance,
                         equip.size[2]))
            for other_name, other_info in room.equipment.items():
                if other_name == name:
                    continue
                ox, oy, oz = other_info["position"]
                other_equip = other_info["instance"]
                other_aabb = AABB((ox, oy, oz), other_equip.size)
                if aabb.intersects(other_aabb):
                    violations.append((name, other_name))
        return violations
