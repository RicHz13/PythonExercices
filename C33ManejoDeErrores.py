#Cuando se avienta (throw) un error, si el error no se "atrapa", entonces el programa se detiene
#hay veces que queremos evitar este comportamiento porque sabemos como arreglar el error.
#Para manejar el error se utilizan los keywords "try/except"
#Consta de 4 partes:
    # 1 Try: es el código que se tratará de ejecutar y que estará protegido si se produce un error.
    # 2 Except: Es el código que se ejecutará si el código del "try" genera un error.
    # 3 Else: Si no se produce un error en el "try", la ejecución del código seguirá adelante
    # 4 Finally: Se ejecutará sin importar si se produce o no un error.

coutries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31
}

while True:
    country = str(input('Escribe el nombre de un país: ')).lower()

    try:
        print('La población de {} es: {} millones'.format(country, coutries[country]))
    except KeyError:
        print('No tenemos el dato de la población de {}'.format(country))
