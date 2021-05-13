def run():
    print('Calculemos el area de un triangulo')
    base = float(input('Escribe el valor de la base: '))
    altura = float(input('Escribe el valor de la altura: '))
    A = area_triangulo(base,altura)
    print('El area de tu triangulo es: ' + str(A))

    decision = input('¿Quieres saber que tipo de triangulo que tienes? 1.- Si    2.- No  ')

    if int(decision) == 1:
        print('Tu primer lado mide ' + str(base))
        lado2 = input('Escribe el valor de tu segundo lado: ')
        lado3 = input('Escribe el valor de tu tercer lado: ')
        tipo_triangulo(base,float(lado2),float(lado3))
    else:
        print('Hasta Luego!')

def area_triangulo(b,h):
    return (b*h)/2

def tipo_triangulo(l1,l2,l3):
    if l1 == l2 and l2 == l3:
        print('Tu triangulo es un equilatero')
    elif (l1 == l2 and l1 != l3) or (l2==l3 and l2 != l1) or (l1 == l3 and l1 != l2):
        print('Tu triangulo es isoceles')
    elif l1 != l2 and l1 != l3:
        print('Tu triangulo es escaleno')


if __name__ == '__main__':
    run()


# a = ''
# for i in range(0,5,1):
#     for j in range(0,20-i,1):
#         a = a + '-'
#     print(a)
#     a= ''
