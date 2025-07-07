from typing import Tuple


class AABB:
    """Axis-aligned bounding box."""

    def __init__(self, position: Tuple[int, int, int], size: Tuple[int, int, int]):
        self.x, self.y, self.z = position
        self.w, self.d, self.h = size

    def intersects(self, other: 'AABB') -> bool:
        return (
            self.x < other.x + other.w and
            self.x + self.w > other.x and
            self.y < other.y + other.d and
            self.y + self.d > other.y and
            self.z < other.z + other.h and
            self.z + self.h > other.z
        )
