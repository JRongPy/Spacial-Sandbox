"""Build a scene representation from the room."""

from .threejs_bridge import to_threejs


def build_scene(room):
    return {"scene": to_threejs(room)}
