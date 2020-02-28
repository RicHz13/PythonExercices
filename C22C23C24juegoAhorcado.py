#juego de ahorcado
import random

IMAGES = ['''

    +---+

    |   |

        |

        |

        |

        |

        =========''', '''

    +---+

    |   |

    O   |

        |

        |

        |

        =========''', '''

    +---+

    |   |

    O   |

    |   |

        |

        |

        =========''', '''

    +---+

    |   |

    O   |

   /|   |

        |

        |

        =========''', '''

    +---+

    |   |

    O   |

   /|\  |

        |

        |

        =========''', '''

    +---+

    |   |

    O   |

   /|\  |

    |   |

        |

        =========''', '''

    +---+

    |   |

    O   |

   /|\  |

    |   |

   /    |

        =========''', '''

    +---+

    |   |

    O   |

   /|\  |

    |   |

   / \  |

        =========''', '''

''']

words = [
    'bolsa',
    'teclado',
    'dinero',
    'laptop',
    'termo',
    'celular',
    'cargador',
    'llamada',
    'hielo',
    'escritorio',
    'domingo',
    'domino'
]

def random_word():
    idx = random.randint(0, len(words) - 1)
    return words[idx]

def display_board(hidden_word, tries, letter_fails):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- * ---')
    if tries > 0:
        print('Letras utilizadas fallidas: {}'.format(letter_fails))

def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    letter_fails = []
    count_repeat = 0
    tries = 0

    while True:
        display_board(hidden_word, tries, letter_fails)
        current_letter = str(input('Escoge una letra: '))

        letter_indexes = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)

        if len(letter_indexes) == 0:
            if len(letter_fails) == 0:
                letter_fails.append(current_letter)
            else:
                for i in range(len(letter_fails)):
                    if letter_fails[i] == current_letter:
                        count_repeat += 1
                if count_repeat < 1:
                    letter_fails.append(current_letter)
            
            tries += 1
            count_repeat = 0

            if tries == 7:
                display_board(hidden_word, tries, letter_fails)
                print('')
                print('Perdiste! La palabra correcta era {}'.format(word))
                break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter

            letter_indexes = []

        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print('¡Felicidades! Ganaste. La palabra es: {}'.format(word))
            break

if __name__ == '__main__':

    print('B I E N V E N I D O S  A  A H O R C A D O S')

    run()

