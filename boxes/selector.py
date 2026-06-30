import json
from pathlib import Path

CATALOG_PATH = Path(__file__).resolve().parent / "boxes.json"


def load_catalog():
    with open(CATALOG_PATH) as f:
        return json.load(f)


CATALOG = load_catalog()


def _volume(d):
    return d["length"] * d["width"] * d["height"]


def _fits(item, box):
    item_dims = sorted([item["length"], item["width"], item["height"]], reverse=True)
    box_dims = sorted([box["length"], box["width"], box["height"]], reverse=True)
    return all(i <= b for i, b in zip(item_dims, box_dims))


def select_box(items, catalog=None):
    if catalog is None:
        catalog = CATALOG

    if not items:
        raise ValueError("select_box requires at least one item")

    total_weight = sum(i["weight"] * i["quantity"] for i in items)
    total_volume = sum(_volume(i) * i["quantity"] for i in items)
    anchor_item = max(items, key=_volume)  # largest single item - must physically fit

    candidates = []
    weight_fail = dim_fail = 0
    for box in catalog:
        ok_weight = box["max_weight"] >= total_weight
        ok_volume = box["length"] * box["width"] * box["height"] >= total_volume
        ok_dims = _fits(anchor_item, box)
        if not ok_weight:
            weight_fail += 1
        if not ok_dims:
            dim_fail += 1
        if ok_weight and ok_volume and ok_dims:
            candidates.append(box)

    if not candidates:
        if weight_fail == len(catalog):
            reason = f"no box has max_weight >= total order weight ({total_weight:g}kg)"
        elif dim_fail == len(catalog):
            reason = f"no box is large enough to fit the largest item ('{anchor_item['name']}')"
        else:
            reason = "no single box satisfies weight, volume, and dimension constraints together"
        return {"selected_box": None, "total_weight": total_weight, "total_volume": total_volume, "reason": reason}

    best = min(candidates, key=lambda b: (b["cost"], _volume(b)))
    return {
        "selected_box": best,
        "total_weight": total_weight,
        "total_volume": total_volume,
        "reason": "lowest-cost box satisfying weight, volume, and dimension constraints",
    }
