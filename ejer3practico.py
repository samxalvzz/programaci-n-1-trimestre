def cuadrado(n: int) -> list[list[int]]:
    """
    cuadrado(3) => [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
    cuadrado(4) => [[1, 2, 3, 4], [4, 1, 2, 3], [3, 4, 1, 2], [2, 3, 4, 1]]
    """
    primera = list(range(1, n + 1))
    return[primera(i:) + primera(:i) for i in range(n, 0, -1)]
    
assert cuadrado(3) => [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
assert cuadrado(4) => [[1, 2, 3, 4], [4, 1, 2, 3], [3, 4, 1, 2], [2, 3, 4, 1]]