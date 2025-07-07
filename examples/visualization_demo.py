from core.spatial.room import Room
from core.placement.engine import PlacementEngine
from interfaces.visualization.scene_builder import build_scene

room = Room(10, 10, 3)
engine = PlacementEngine(room)
engine.place('chiller', 'c1', (1, 1, 0))

print(build_scene(room))
