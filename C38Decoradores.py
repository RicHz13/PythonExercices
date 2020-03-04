#Un decorador es una función que recibe otra función y regresa una 3er función
#Para reconocer un decorador, puedes ver que tiene un arroba sobre la declaración de una función
#Útil para definir si una función debe ejecutarse o no.
    #Por ejemplo:
    #En servidores web, existen ciertas funciones que nada más deben ejecutarse si un usuario
    #se encuentra autenticado
#NOTA: buscar más información de docoradores

def protected(func):
    def wrapper(password):
        if password == 'platzi':
            return func()
        else:
            print('La contraseña es incorrecta')
    
    return wrapper


@protected
def protected_func():
    print('Tu contraseña es correcta')

if __name__ == '__main__':
    password = str(input('Ingresa tu contraseña: '))

    protected_func(password)