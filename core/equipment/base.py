class Equipment:
    """Base class for all equipment."""

    def __init__(self, name, size):
        self.name = name
        self.size = size  # (w, d, h)

    @property
    def footprint(self):
        return self.size[0], self.size[1]
