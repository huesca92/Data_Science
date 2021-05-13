def run():
    print('Juguemos Piedra, Papel o Tijera. Se llevara la victoria quien gane 2 de 3 partidas.')
    ganados_1=0
    ganados_2=0
    
    while (ganados_1 < 2 and ganados_2 < 2):
        p1 = input('Jugador 1: Escriba Piedra, papel o tijera: ')
        p2 = input('Jugador 2: Escriba Piedra, papel o tijera: ')
        ganador = ppt(p1.capitalize(),p2.capitalize())

        if ganador == 1:
            ganados_1 += 1
            print('Punto para el Jugador1')
        elif ganador == 2:
            ganados_2 += 1
            print('Punto para el jugador2')
        else:
            print('Empate')

    if ganados_1 > ganados_2:
        print('Tenemos un ganador!!! Felicidades Jugador1')
    else:
        print('Tenemos un ganador!!! Felicidades Jugador2')
    
    
def ppt(jugador1,jugador2):
    if jugador1 == 'Piedra':
        if jugador2 == 'Papel':
            return 2
        elif jugador2 == 'Tijera':
            return 1
        else:
            return 0
    elif jugador1 == 'Papel':
        if jugador2 == 'Tijera':
            return 2
        elif jugador2 == 'Piedra':
            return 1
        else:
            return 0
    elif jugador1 == 'Tijera':
        if jugador2 == 'Papel':
            return 1
        elif jugador2 == 'Piedra':
            return 2
        else:
            return 0


if __name__ == '__main__':
    run()