
lista = [1, 4, 600, 2, 7, 8, 20, 67, 3, 105]
a = 0
b = 0


max, min = lista[0], lista[0]

for i in lista:
    if i > max:
        max = i
    if i < min:
        min = i

print(max)
print(min)

lista2 = []
lista3 = []

for i in lista:
    if i > 100:
        lista2.append(i)
    elif i < 50:
        lista3.append(i)

print(lista2)
print(lista3)