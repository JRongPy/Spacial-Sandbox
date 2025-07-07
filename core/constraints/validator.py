class Validator:
    """Validate room against a set of constraints."""

    def __init__(self, constraints):
        self.constraints = constraints

    def validate(self, room):
        result = {}
        for constraint in self.constraints:
            result[constraint.__class__.__name__] = constraint.check(room)
        return result
