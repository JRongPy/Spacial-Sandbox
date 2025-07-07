from .grid import Grid


class Room:
    """Simple room containing equipment placed on a grid."""

    def __init__(self, width, depth, height):
        self.grid = Grid(width, depth, height)
        self.equipment = {}

    def add_equipment(self, name, equipment, position):
        x, y, z = position
        if self.grid.get(x, y, z):
            raise ValueError("Cell already occupied")
        self.grid.set(x, y, z, name)
        self.equipment[name] = {
            "instance": equipment,
            "position": position,
        }

    def remove_equipment(self, name):
        info = self.equipment.pop(name, None)
        if info:
            x, y, z = info["position"]
            self.grid.set(x, y, z, None)

    def get_equipment(self, name):
        return self.equipment.get(name)
