#Juego Pedra Papel o Tijera

import random

def juego():

    opciones = ('Piedra', 'Papel', 'Tijera')

    rounds = 3
    computer_wins = 0 
    user_wins = 0

    for _ in range(rounds): #Inicia un bucle para el número de rondas especificado.
        while True: # Inicia un bucle que continúa hasta que el jugador ingrese una opción válida.
            jugador = input(f'Elige una opción {opciones}: ').capitalize()
            if jugador in opciones:
                break
            else:
                print('Opción no válida. Inténtalo de nuevo.')

        computadora = random.choice(opciones)

        print('Tu opción => ', jugador)
        print('Opción del computador => ', computadora)

        if jugador == computadora:
            print('Empate')
        elif ganador(jugador, computadora):
            print('Ganaste')
            user_wins += 1
        else:
            print('Perdiste')
            computer_wins += 1

    print('\nResultados finales:')
    print(f'Jugador gana {user_wins} veces')
    print(f'Computadora gana {computer_wins} veces')

def ganador(jugador, computadora):
    if (jugador == 'Piedra' and computadora == 'Tijera') or (jugador == 'Papel' and computadora == 'Piedra') or (jugador == 'Tijera' and computadora == 'Papel'):
        return True
    return False

juego()