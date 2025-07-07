class Grid:
    """Simple 3D voxel grid."""

    def __init__(self, width, depth, height):
        self.width = width
        self.depth = depth
        self.height = height
        self.cells = {}

    def set(self, x, y, z, value):
        if not self.in_bounds(x, y, z):
            raise ValueError("Position out of bounds")
        self.cells[(x, y, z)] = value

    def get(self, x, y, z):
        return self.cells.get((x, y, z))

    def in_bounds(self, x, y, z):
        return 0 <= x < self.width and 0 <= y < self.depth and 0 <= z < self.height
