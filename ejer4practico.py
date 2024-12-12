"""
consecutiva
"""
def es_consecutiva(secuencia) -> bool:
    """
    es_consecutiva([4, 5, 6, 7]) => True
    es_consecutiva([4, 5, 6]) => False
    """
    return True if secuencia == list(range(min(secuencia), max(secuencia) + 1))
assert es_consecutiva([4, 5, 6, 7]) => True
assert es_consecutiva([4, 5, 6]) => False