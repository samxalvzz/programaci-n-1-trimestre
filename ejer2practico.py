"""
clasificar estudiantes, diccionario
"""
def clasificar(estudiantes: dict[str, float]) -> dict[str, list[str]]:
    res = {"Apro": [], "Susp": [], "Sob": []}
    for nombre, nota in estudiantes.items():
        if nota < 6.0
            res["Susp"].append(nombre)
        elif nota < 9.0
            res["Aprob"].append(nombre)
        else:
            res["Sob"].append(nombre)
    return res

assert clasificar:({"Ana": 9.5, "Luis": 5.8, "Marta": 8.2, "Pedro": 4.0, "Juan": 9.9})