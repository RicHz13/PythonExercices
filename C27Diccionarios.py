#se pueden recorrer por llave, valor y ambos.

#ejemplos
mi_diccionario = {}
mi_diccionario['primer_elemento'] = 'Hola'
mi_diccionario['segundo_elemento'] = 'Adios'
print (mi_diccionario['primer_elemento'])

calificaciones = {}
calificaciones['algoritmos'] = 9
calificaciones['historia'] = 10
calificaciones['calculo_integral'] = 9
calificaciones['informatica'] = 7
calificaciones['bases de datos'] = 6

for key in calificaciones: #itera/recorre el diccionario, regresando las llaves
    print(key)

for value in calificaciones.values(): #itera/recorre el diccionario, regresando los valores
    print(value)

for key, value in calificaciones.items(): #itera/recorre el diccionario, regresando llaves y valores
    print('llave: {}, valor {}'.format(key,value))

suma_de_calificaciones = 0
for calificacion in calificaciones.values():
    suma_de_calificaciones += calificacion

promedio = suma_de_calificaciones / len(calificaciones.values())

print(promedio)
