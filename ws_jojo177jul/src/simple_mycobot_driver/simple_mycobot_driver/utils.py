def is_safe(coords):
    x, y, z = coords[:3]
    if not (-250 <= x <= 250): return False
    if not (-250 <= y <= 250): return False
    if not (0 <= z <= 300): return False
    return True
