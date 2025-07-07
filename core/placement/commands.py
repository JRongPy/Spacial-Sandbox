class PlaceCommand:
    def __init__(self, engine, equip_type, name, position):
        self.engine = engine
        self.equip_type = equip_type
        self.name = name
        self.position = position

    def execute(self):
        return self.engine.place(self.equip_type, self.name, self.position)
