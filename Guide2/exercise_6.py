

operacion = int((input("seleccionar la operacion: 1. resta 2.suma 3.división 4.multiplicación")))

print("ingrese 2 numeros:")
numero1 = int(input())
numero2 = int(input())
if operacion == 1:
    print(numero1 - numero2)
elif operacion == 2:
    print(numero1 + numero2)
elif operacion == 3:
    print(numero1 / numero2)
elif operacion == 4:
    print(numero1 * numero2)
else:
    print('hola')
