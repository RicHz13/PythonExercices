#Una lista es una secuencia de elementos
#Cuando se asigna a una variable, permite agrupar varios elementos en un solo lugar
#Se crean con los corchetes [] o con la keyword list
#Ejemplos:
    #supermercado = ['apio', 'tomate', 'queso']

#Acceso a elementos:
#Se puede acceder a los elementos de una lista con su índice.
#Los índices se comienzan a contar desde 0
    #supermercado = ['apio', 'tomate', 'queso']
    #índices         0         1        2
    #supermercado[0] nos traería 'apio'

def average_temps(temps):
    sum_of_temps = 0
    for temp in temps:
        sum_of_temps += temp

    return sum_of_temps / len(temps)

if __name__ == '__main__':
    temps = [21, 26, 25, 20, 30, 22, 24]

    average = average_temps(temps)
    print('El promedio de las temperaturas es: {}'.format(average))