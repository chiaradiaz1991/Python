
"""
formas de imprimir un string que contenga 1 o más variables

"""

name = "Name_var"

print("hi", name)
print("hi {}".format(name))
print("hi {0}".format(name))
print("hi {first}".format(first = name))
print("hi %s" %(name))
print(f"hi {name}")


# funciones

def sum(a, b):
    return a +b

sum(2, 2)

print(sum(1,2))

#parametros indefinidos

def resta(*args):
    restar= 2
    for a in args:
        restar -= a
    return restar

print(resta(6,5,9,8))

# lamnda

suma = lambda a, b : a + b

print(suma(1, 4))

reverse = lambda string : string[::-1]

print(reverse("hola"))