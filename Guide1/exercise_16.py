"""
Ejercicio 16: Crear un programa que cree un diccionario vacío y lo vaya llenado con información
sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le
pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""


name = ""
age = ""
gender = ""
telephone = ""
email = ""

usuarios = {}

name = input(f"Name?: {name}")
usuarios["Name"] = name
print(usuarios)
age = input(f"Age?: {age}")
usuarios["Age"] = age
print(usuarios)
gender = input(f"Gender?: {gender}")
usuarios["Gender"] = gender
print(usuarios)
telephone = input(f"Telephone? {telephone}")
usuarios["Telephone"] = telephone
print(usuarios)
email = input(f"Email? {email}")
usuarios["Email"] = email
print(usuarios)

