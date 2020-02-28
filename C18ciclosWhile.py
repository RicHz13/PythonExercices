#Es similar a un for loop; pero en lugar de recorrer una secuencia, se ejecuta hasta que una condición
#se convierta en falsa
#Hay que tener cuidado de no caer en un infinite loop

#i = 10
#while i > 0:
#    print(i)
#    i -= 1
import random

def run():
    number_found = False
    limit = int(input('Hasta que número quieres llegar: '))
    #random_number = random.randint(0, 20)
    random_number = random.randint(0, limit)

    while not number_found:
        number = int(input('Intenta un número: '))

        if number == random_number:
            print('Felicidades encontraste el número')
            number_found = True
        elif number > random_number:
            print('El número es más pequeño')
        else:
            print('El número es más grande')

if __name__ == '__main__':
    run()



