def run():

    bandera = 0
    print('Rangos cambiantes')
    inferior = int(input('Escribe el limite inferior: '))
    superior = int(input('Escribe el limite superior: '))

    while bandera == 0:
        # inferior = int(input('Escribe el limite inferior: '))
        # superior = int(input('Escribe el limite superior: '))
        valor = int(input('Escribe el valor de comparación: '))

        if valor > inferior and valor < superior:
            print('El numero ' + str(valor) + ' esta en el intervalo')
            bandera = 1
        else:
            print('Valor fuera del rango, intentemos de nuevo')

            

if __name__ == '__main__':
    run()