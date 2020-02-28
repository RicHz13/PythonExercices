def foreign_exchange_calculator(ammount):
    mex_to_us_rate = 19.08

    return ammount / mex_to_us_rate

def run():
    print('Calculadora de divisas')
    print('Convierte pesos mexicanos a dolares')
    print('')

    ammount = float(input('Ingresa la cantidad de pesos mexicanos que quieres convertir: '))

    result = foreign_exchange_calculator(ammount)

    print('${} pesos mexicanos son ${} dólares'.format(ammount, result))
    print('')

if __name__ == '__main__':
    run()
    print('Final {}')