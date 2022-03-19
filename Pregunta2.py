import os
horasTrabajadas = 0
limiteDeHoras = 40
limiteDeHorasExtra = 8
pagoPorHora = 10  # 10 dólares
horasExtras = 0
pagoTotal = 0
horasExtrasDemás = 0

exceptionMessage = "El valor que ingresaste debe ser mayor a 0 o ser un número entero...\n"
os.system("cls")
while(True):
    try:
        print('\n>>> Ingresa el número de horas trabajadas: ')
        horasRegistradas = int(input())
        if horasRegistradas <= 0:
            raise ValueError()
        horasTrabajadas = horasRegistradas
        os.system("cls")
        break
    except ValueError:
        print(exceptionMessage)

if(horasTrabajadas <= limiteDeHoras):
    pagoTotal = horasTrabajadas*pagoPorHora
    print(">>> Tu pago es: $", pagoTotal)
if(horasTrabajadas-limiteDeHoras > 0):
    horasExtras = horasTrabajadas-limiteDeHoras
    if(horasExtras <= limiteDeHorasExtra):
        pagoTotal = limiteDeHoras*pagoPorHora + horasExtras*(pagoPorHora*2)
        if(horasExtras == 1):
            print(">>> Tu pago por tu hora extra es: $", pagoTotal)
        else:
            print(">>> Tu pago por tus ", horasExtras,
                  " horas extras es: $", pagoTotal)
    elif(horasExtras > limiteDeHorasExtra):
        horasExtrasDemás = horasExtras-limiteDeHorasExtra
        pagoTotal = limiteDeHoras*pagoPorHora + limiteDeHorasExtra * \
            (pagoPorHora*2)+horasExtrasDemás*(pagoPorHora*3)
        print(">>> Tu pago por tus ", horasExtras,
              " horas extras es: $", pagoTotal)
