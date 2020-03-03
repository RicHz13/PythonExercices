#Pytohn permite crear e inicializar listas y diccionarios con una sintanxis más natural
#Convierte una secuecia en otra
#En resumén sirve para evitar declarar funciones que se pueden realizar en una declaración, haciendo
#que el código sea más legible.
#Esto es conocido como Sintactic Sugar o Azúcar Sintáctico

pares = [x for x in range(100) if x % 2 == 0]
print(pares)

nones = [x for x in range(100) if x % 2 != 0]
print(nones)

cuadrados = {x: x**2 for x in range(100)}
print(cuadrados)