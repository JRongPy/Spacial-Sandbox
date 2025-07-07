from .base import Equipment


class Chiller(Equipment):
    """Simple chiller definition."""

    def __init__(self, name="Chiller", size=(2, 2, 2)):
        super().__init__(name, size)
