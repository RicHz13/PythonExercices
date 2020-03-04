#NOTA: el archvo que queremos abrir, debe estar en el mismo directorio donde está el archivo de python

def run():
    counter = 0
    with open('aleph.txt', encoding = 'utf8') as f:
        for line in f:
            counter += line.count('Beatriz')
    print('Beatriz se encuentra {} en el texto'.format(counter))

if __name__ == '__main__':
    run()
