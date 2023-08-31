# Creado por Leroy Ortiz Ríos 
#2 de junio de 2023

import random

#3 Variables 
piedra = 1      

papel = 2

tijera = 3

salir = 4

# Contadores de puntos
contadorPuntosJugador = 0
contadorPuntosBot = 0

# Sigue corriendo el algoritmo hasta que entre en brake
while True:

    #resJugador = int (input("Escoja piedra (1) , papel (2) , tijera (3) o presiona el numero 4 para salir: "))

    resJugador = input("Escoja piedra (1), papel (2), tijera (3) o presiona el número 4 para salir: ")

    if resJugador.isdigit():
        resJugador = int(resJugador)
    else:
        print("Entrada inválida. Debes ingresar un número válido.")    
    #---------------------------------------------------------------

    
    # if not resJugador:
    #     print("")
    #     print("Has escogido una respuesta no valida, intenta nuevamente.")
    #     print("")

    

    #Variable entera, int o integer 
    bot = random.randint(1,3)
    
    if (bot == 1):
        print("Bot ha escogido piedra")
        print("")
    
    elif (bot == 2):
        print("Bot ha escogido papel")
        

    elif (bot == 3):

        print("Bot ha escogido tijera")
        
    # Verifica si jugador gana la ronda 
    if(resJugador == 1 and bot == 3) or (resJugador == 2 and bot == 1) or (resJugador == 3 and bot == 2):
        print("Has ganado la partida Round 1. YOU WIN!")
        #print("Has escogido",resJugador, "y Bot ha escogido", bot)
        print("")
        contadorPuntosJugador +=1
        #print("Puntos Jugador 1:",contadorPuntosJugador)

    # Verifica si quedamos empate    
    elif (bot == resJugador):
        print("-----------------------------------------------------")
        print("Empate, Bot y jugador ha escogido la misma respuesta.")
        print("Has escogido",resJugador, "y Bot ha escogido", bot)
        print("")
    # Verifica si perdimos la ronda
    else:
        print("")
        print("Has perdido la partida Round 1. YOU LOST!")
        #print("Has escogido",resJugador, "y Bot ha escogido", bot)
        print("")

        #Le sumamos 1 punto al bot
        contadorPuntosBot +=1
        #print("Puntos Bot:",contadorPuntosBot)
    
    # Verifica si ingresamos una respuesta invalida
    if (resJugador > 4):
        print("")
        print("Has escogido una respuesta no valida, intenta nuevamente.")
        print("")

    

    print("Jugador:",contadorPuntosJugador, "puntos")
    print("Bot:",contadorPuntosBot, "puntos")
    print("------------------------------------------------------------")

