from .chiller import Chiller


CATALOG = {
    "chiller": Chiller,
}


def create_equipment(equip_type, *args, **kwargs):
    cls = CATALOG.get(equip_type)
    if not cls:
        raise ValueError(f"Unknown equipment type: {equip_type}")
    return cls(*args, **kwargs)
