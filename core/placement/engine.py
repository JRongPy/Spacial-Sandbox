from ..equipment.catalog import create_equipment


class PlacementEngine:
    """Simple engine that places equipment via commands."""

    def __init__(self, room):
        self.room = room

    def place(self, equip_type, name, position):
        equip = create_equipment(equip_type, name=name)
        self.room.add_equipment(name, equip, position)
        return equip
