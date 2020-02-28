#range nos permite generar un rango a partir de un número. Al igual que el corte de las cadenas (ver notas clase 16)
#podemos decir de a partir de que número, hasta que número y cada cuanto), en donde no son obligatorios todos los
#parámetros

a = range(3, 30, 3)
a = list(a)
print(a)

for i in range(5):
    print(i)

#for loop
    #se puede utilizar para recorrer strings (una string es una secuencia)
    #Se necesita el keyword in
    #Si se requiere salir antes de una iteración se utiliza el keyword "break"
    #Si se requiere pasar a la siguiente iteración se utiliza el keyword "continue"

string = 'ricardo'

for letter in string:
    print(letter)

for r in range(30):  #ejemplo de "continue"
    if r % 3 != 0:
        continue
    else:
        print(r**2)

for b in range(30):  #ejemplo de "break"
    if b % 3 == 0:
        print(b)
    elif b == 22:
        break

