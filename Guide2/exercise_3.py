
number1 = ""
number2 = ""



numero1 = int((input(f"Ingrese un número?: {number1}")))
numero2 = int(input(f"Ingrese un segundo número?: {number2}"))


print(numero1)
print(numero2)

def resta(a, b):
    return a - b

def sum(a, b):
    return a + b

def prod(a, b):
    return a * b

if numero1 < numero2:
    print(resta(numero2, numero1))
elif numero1 > numero2:
    print(sum(numero1, numero2))
elif numero1 == numero2:
    print(prod(numero1, numero2))
