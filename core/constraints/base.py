class Constraint:
    """Base class for constraints."""

    def check(self, room):
        raise NotImplementedError
