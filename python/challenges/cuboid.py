def cuboid(x: int, y: int, z: int, n: int) -> None:
    return [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in
            range(z + 1) if ((i + j + k) != n)]
