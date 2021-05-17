def run():
    print("""Conversor de millas a kilometros y viceversa.
    1.- Convertir de millas a kilometros
    2.- Convertir de kilometros a millas
    Escriba su selección
    """)
    op = int(input())

    if op == 1:
        millas= float(input('Escriba el numero de millas a convertir: '))
        print(str(millas) + ' millas son ' + str(millas_a_kilometros(millas)) + ' kilometros')
    elif op == 2:
        km = float(input('Escriba el numero de kiloemtros a convertir: '))
        print(str(km) + ' kilometros son ' + str(kilometros_a_millas(km)) + ' millas')
    else:
        print('Opción incorrecta')


def millas_a_kilometros(millas):
    return millas*1.609344


def kilometros_a_millas(km):
    return km/1.609344

if __name__ == '__main__':
    run()