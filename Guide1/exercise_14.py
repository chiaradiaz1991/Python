
name= ""
address = ""
age = ""
tel = ""


name = input(f"Cuál es tu nombre?: ")
address = input(f"Cuál es tu dirección?: {address}")
age = input(f"Cuál es tu edad?: {age}")
tel = input(f"Cuál es tu teléfono {tel}")

usuarios = {}

usuarios["Nombre"] = name
usuarios["Dirección"] = address
usuarios["Edad"] = age
usuarios["teléfono"] = tel


print(usuarios)