
diccionario = {
    'Euro':'€',
    'Dollar':'$',
    'Yen':'¥',
}

divisa = ""

print(input(f"Indique la divisa: {divisa}"))


if divisa == diccionario["Euro"]:
    print(diccionario["Euro"])
elif divisa == diccionario["Dollar"]:
    print(diccionario["Dollar"])
elif divisa == diccionario["Yen"]:
    print(diccionario["Yen"])
else:
    print("no se encuentra la divisa")