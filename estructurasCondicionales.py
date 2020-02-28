#operadores relacionales
# == es igual a
# != es diferente a
# > mayor que
# >= mayor igual que
# < menor que
# <= menor igual que

#Operadores lógicos
# and
# or
# not


def say_hello(age):
    age = int(input('¿Cuál es tu edad?: '))
    if age > 18:
        print('hola adulto')
    else:
        print('hola niño')

say_hello(45)