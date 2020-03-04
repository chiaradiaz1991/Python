# coding=utf-8

for i in range(10):
    print(i)

if True:
    print("hello")

# entrada y salida de datos

variable_1= 5
variable_2 = int(input("ingrese un número: ")) #entrada por teclado

print(variable_1)
print(variable_2)
print(type(variable_2))

lista = [1, 2, 3, 4]
valores = ["hola", "chau", "buen día", "buenas noches"]

mi_diccionario = dict(zip(lista, valores))
print(mi_diccionario)

diccionario = {"hola": [1, 1]}
print(diccionario)
print(lista[0])
print(mi_diccionario[2])
print(mi_diccionario.keys()) #para imprimir las keys de un diccionario

tupla = 1, 2, 3
print(tupla)

help("keywords")
