#Con el algoritmo de búsqueda binaria partimos de la lista ordenada, nosotros sabemos que hay números mayores
#y menores que el que estamos buscando.
#Seleccionamos un número aleatorio para dividir la lista, puedes escoger cualquier número
#en éste caso sumanos el primer y el último índice de la lista, los sumamos y dividimos en dos (por eso se llama
# binario), luego compraramos el número que está en el índice, de esta manera ya eliminamos la mitad de las opciones.
#Podemos continuar dividiendo la lista y comparando hasta que lleguemos al resultado esperado

#Implementación CLASE 26

def binary_search(numbers, number_to_find, low, high):
    if low > high:
        return False

    mid = (low + high) // 2

    if numbers[mid] == number_to_find:
        return True
    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low, mid - 1)
    else:
        return binary_search(numbers, number_to_find, mid + 1, high)



if __name__ == '__main__':
    #numbers = [1, 3, 4, 5, 6 , 9, 10, 11, 25, 27, 28, 34, 36, 49, 51]

    numbers = [9, 3, 78, 15, 98, 100, 34, 423, 16, 88, 2, 77, 1000]

    numbers.sort()

    #numbers_des = [9, 3, 78, 15, 98, 100, 34, 423, 16, 88, 2, 77, 1000]

    #numbers = sorted(numbers_des)

    number_to_find = int(input('ingresa un número: '))

    result = binary_search(numbers, number_to_find, 0, len(numbers) - 1)

    if result is True:
        print('El número si está en la lista'),
        print(numbers)
    else:
        print('El número no está en la lista')