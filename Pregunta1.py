import os
triangulo = []
exceptionMessage = "El valor que ingresaste debe ser mayor a 0 o ser un número entero...\n"
os.system("cls")
while(True):
    try:
        print('\n>>> Ingresa la longitud (A) del primer lado del triangulo: ')
        lado1 = int(input())
        if lado1 <= 0:
            raise ValueError()
        triangulo.append(lado1)
        os.system("cls")
        break
    except ValueError:
        print(exceptionMessage)
while(True):
    try:
        print('\n>>> Ingresa la longitud (B) del segundo lado del triangulo: ')
        lado2 = int(input())
        if lado2 <= 0:
            raise ValueError()
        triangulo.append(lado2)
        os.system("cls")
        break
    except ValueError:
        print(exceptionMessage)
while(True):
    try:
        print('\n>>> Ingresa la longitud (C) del tercer lado del triangulo: ')
        lado3 = int(input())
        if lado3 <= 0:
            raise ValueError()
        triangulo.append(lado3)
        os.system("cls")
        break
    except ValueError:
        print(exceptionMessage)

A = triangulo[0]
B = triangulo[1]
C = triangulo[2]


def encontrarLadosIguales(triangulo):
    ladosRepetidos = []
    ladoÚnico = []
    for lado in triangulo:
        if(triangulo.count(lado) == 2):
            ladosRepetidos.append(lado)
        else:
            ladoÚnico = lado

    return ladosRepetidos[0], ladoÚnico


def esEquilátero(triangulo):
    print("\n>>> El triangulo es Equilátero.\n")
    print(">>> La suma de sus lados es: ", sum(triangulo))


def esEscaleno(triangulo):
    ladoMenor = sorted(triangulo)[0]
    print("\n>>> El triangulo es Escaleno.\n")
    print(">>> Su lado menor es: ", ladoMenor)


def esIsósceles(triangulo):
    lados = encontrarLadosIguales(triangulo)
    LadosIguales = lados[0]
    LadoDiferente = lados[1]
    print("\n>>> El triangulo es Isósceles.\n")
    print(">>> La diferencia entre el producto de los dos lados iguales y el otro lado es: ",
          LadosIguales*LadosIguales-LadoDiferente)


print("Lados del triangulo \n")
print("A: ", A)
print("B: ", B)
print("C: ", C)

if(A == B == C):
    esEquilátero(triangulo)
elif(A == B or A == C or C == B):
    esIsósceles(triangulo)
else:
    esEscaleno(triangulo)
