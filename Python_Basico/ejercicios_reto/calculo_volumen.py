import math

def run():
    figura = int(input("""Calculo del volumenes
    ¿De cual figura quieres calcular el volumen?
    1.- Cilindro
    2.- Cubo
    3.- Prisma Rectangular
    4.- Esfera
    """))
    
    if figura == 1:
        radio=float(input('Escribe el radio del cilindro: '))
        altura=float(input('Escribe la altura del cilindro: '))
        print('El volumen del cilindro es ' + str(volumen_cilindro(radio,altura)))
    elif figura == 2:
        lado=float(input('Escribe el valor del lado: '))
        print('El volumen del cubo es ' + str(volumen_cubo(lado)))
    elif figura == 3:
        ancho=float(input('Escribe ancho de la base: '))
        largo=float(input('Escribe el largo la base: '))
        altura=float(input('Escribe la altura del prisma: '))
        print('El volumen del prisma es ' + str(volumen_prisma(largo,ancho,altura)))
    elif figura == 4:
        radio=float(input('Escribe el radio de la esfera: '))
        print('El volumen de la esfera es ' + str(volumen_esfera(radio)))

        
def volumen_cilindro(radio, altura):
    return math.pi*(radio*radio)*altura


def volumen_cubo(lado):
    return lado**3


def volumen_prisma(largo,ancho,altura):
    return (largo*ancho)*altura


def volumen_esfera(radio):
    return (4/3)*math.pi*(radio**3)



if __name__ == '__main__':
    run()

