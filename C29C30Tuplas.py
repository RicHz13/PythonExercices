#Son una secuencia de valores indexada por enteros.
#son inmutables (no se pueden cambiar)

#ejemplo:
#mi_tupla = (1, 2, 3, 4)
#print(mi_tupla)

def first_not_repeating_char(char_sequence):
    seen_letters = {}

    for idx, letter in enumerate(char_sequence):
        if letter not in seen_letters:
            seen_letters[letter] = (idx, 1)
        else:
            seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1)

    final_letter = []
    for key, value in seen_letters.items():
        if value[1] == 1:
            final_letter.append((key, value[0]))

    not_repeated_letters = sorted(final_letter, key=lambda value: value[1])

    if not_repeated_letters:
        return not_repeated_letters[0][0]
    else:
        return '_'



if __name__ == '__main__':
    char_sequence = str(input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_sequence)

    if result == '_':
        print('Todos los caracteres se repiten')
    else:
        print('El primer caracter no repetido es: {}'.format(result))
