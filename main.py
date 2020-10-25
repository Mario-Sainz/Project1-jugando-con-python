import random

oportunidades = 0
print('Buenas, ¿cual es el nombre de la persona que va a intentar ganarme?')
nombre_jugador = input()

número_elegido_ordenador = random.randint(1, 100)
print('Vale perfecto ' + nombre_jugador + ', estoy pensando en un número del 1 al 100.')
while oportunidades < 6:
    print('Ánimo! Intenta adivinarlo.')
    num_jugador = input()
    num_jugador = int(num_jugador)
    oportunidades = oportunidades + 1
    if num_jugador < número_elegido_ordenador:
        print('El número es muy bajo.')
    if num_jugador > número_elegido_ordenador:
        print('El número es muy alto.')
    if num_jugador == número_elegido_ordenador:
        break
if num_jugador == número_elegido_ordenador:
    oportunidades = str(oportunidades)
    print('No me lo creo ' + nombre_jugador + '!! Has logrado adivinar mi número en ' + oportunidades + ' oportunidades!')
if num_jugador != número_elegido_ordenador:
    número_elegido_ordenador = str(número_elegido_ordenador)
    print('Vaya ... ¡¡has perdido!! mi número era el ' + number)