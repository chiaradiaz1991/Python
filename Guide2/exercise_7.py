"""
Ejercicio 7: Crear un diccionario con 5 estudiantes y sus respectivas notas. Imprimir por pantalla los
alumnos que aprobaron y su nota (no en forma de diccionario, si no con nombre : nota). Tener en cuenta
que para aprobar el alumno debe sacarse una nota mayor o igual a 7 y menor o igual a 10.
"""

alumnos={
    "Rosa": 8,
    "Luisa": 3,
    "Olivia": 9,
    "Mariana": 7,
    "Paula": 2,
}

mesesMod = {}
for key, value in alumnos.items():
    mesesMod[value] = key


print(mesesMod)