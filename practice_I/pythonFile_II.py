
lista = ["Chiara", 28, "Argentina", True, [0, 0]]
print(lista)

print(len(lista)) #metodo para saber la cantidad de elementos

print(lista[0])
print(lista[2])
print(lista[3])
print(lista[3])
print(lista[4])


lista[0] = "Ely" #reemplazo
print(lista)
lista[1:4] = [0, 0, 0] #va a cambiar los elementos desde el 0 hasta el 3 inclusive, el 4 es un limite

print(lista)

tupla = ("Chiara", 28, "Argentina", True, [0, 0])
print(type(tupla))
tupla = list(tupla) #para hacerla un tipo de dato mutable hay que transformarla a una lista
print(tupla)

print(tupla.__sizeof__())
print(lista.__sizeof__())

mis_datos = {
    "Nombre": "Chiara",
    "Apellido": "Diaz",
    "Edad": 28,
}
'''
mis_datos2 = {
    "Apellido": "Diaz",
    "Edad": 28,
    "Nombre": "Chiara",
}


print(mis_datos == mis_datos2)
'''

mis_datos["Edad"] = 29

print(mis_datos)

del mis_datos["Edad"] #elimina la clave Edad

print(mis_datos)

lista1 = ["Chiara", 28, "Argentina"]
lista2 = ["Ludmila", 27, "Brasilera"]

mis_datos2 = dict(zip(lista1, lista2)) #con dict lo convierto a diccionario y zip itera sobre los otros dos objetos iterables

print(mis_datos2)

numero = 5
numero2 = 7
print(numero)
print(numero + 10)


nombre = input("Ingrese su nombre: ")
apellido= "Diaz"
print(f'Mi nombre es {nombre} {apellido}') #f es para poder crear string que tengan incluidas variables, las variables van en corchetes
print("Mi nombre es {}".format(nombre))
print("Mi nombre es {0} {1}".format(nombre, apellido))


## control structures

num = 5

if num < 10:
    if num < 8:
        if num == 5:
            print("yes")
        else:
            print("no")

condition = True

while condition:
    print(num)
    rta = input("Desea seguir? responde por si o por no ").lower()
    if rta == "si":
        condition = True
    elif rta == "no":
        condition = False
    else:
        break


while num > 0:
    print(num)
    num -= 1 #para evitar el loop infinito

for i in [0, 1, 2, 3]:
    print(i)

for i in range(10): #rango de 0 a 9
    print(i)

# range(start, stop, step) donde empieza, donde termina y de a cuantos saltos

for i in range(0, 20, 2):
    print(i)

# break termina el bucle
# continue continua el bucle