class Optimizer:
    """Placeholder optimizer that does nothing for now."""

    def optimize(self, room, validator):
        """Run validator and return the validation result."""
        return validator.validate(room)
