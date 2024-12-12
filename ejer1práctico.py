def suma2(iterable, total: init) -> list(int)
    """
    suma2.py
    """
for i, e in enumerate(iterable)
    for e2 in iterable[i + 1]:
        if e1 + e2 == total:
            return [e1, e2]
return []

assert suma2([1, 2, 3], 5) == [2, 3]
assert suma2([4, 10, 8], 12) == [4, 3]
assert suma2([4, 10, 8], 24) == []