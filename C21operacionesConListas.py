#las operaciones con listas son similares a las que se pueden hacer con números
#Por ejemplo sumar listas:
mi_lista_1 = [1, 2, 3, 4]
mi_lista_2 = [5, 6, 7]
mi_lista_3 = mi_lista_1 + mi_lista_2

print('Esta es la unión de las listas 1 y 2: ', mi_lista_3)

#multiplicación de listas
mi_lista_4 = ['a', 'b']
print('esta es una multiplicación de la lista 4', mi_lista_4 * 5)

#rebanar listas

print('Este es un pedazo de lista ingresando los índices deseados y salto que queremos', mi_lista_3[2:5:1])

#reemplazo de valor en una lista
mi_lista_3[6] = 9

print('aquí reemplazamos el valor del índice 6, cambiando de 7 a 9: ', mi_lista_3)

#Eliminar el último elemento de una lista

mi_lista_3 = mi_lista_3.pop()

print('Eliminamos el último elemento de la lista: ', mi_lista_3)

#ordenar una lista con sorted

mi_lista_5 = [5, 3, 7, 2, 4, 1, 6]

mi_lista_5 = sorted(mi_lista_5)

print('lista ordenada con la función sorted: ', mi_lista_5)

#ampliar una lista

mi_lista_6 = ['ab', 'cd', 'ef']

mi_lista_7 = [10, 11, 12, 13]

mi_lista_6.extend(mi_lista_7)

print('lista 3 extendida con la lista 5: ', mi_lista_6)

#eliminar un elemento de la lista

del mi_lista_6[0]

print('Borramos el índice 0 de la lista, que correspondía a "ab": ', mi_lista_6)

#una cadena de texto se puede convertir una lista

persona = 'betsy'
list_betsy = list(persona)
print('creamos una lista a partir de una cadena de texto:', list_betsy)

#recostruir cadena de texto a partir de una lista
rec_word = ''.join(list_betsy)
print('recostrucción de la cadena de texto a partir la lista: ', rec_word)