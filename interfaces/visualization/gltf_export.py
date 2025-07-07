"""Placeholder for GLTF export."""


def export(room):
    return {"objects": to_threejs(room)}


from .threejs_bridge import to_threejs
