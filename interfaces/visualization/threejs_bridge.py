"""Placeholder for Three.js bridge."""


def to_threejs(room):
    data = []
    for name, info in room.equipment.items():
        x, y, z = info["position"]
        w, d, h = info["instance"].size
        data.append({"name": name, "position": [x, y, z], "size": [w, d, h]})
    return data
