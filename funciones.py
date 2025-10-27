import random


tablero = [[" "," "," "],[" "," "," "],[" "," "," "]]
def menu():
    print("Modos de juego del tres en raya:")
    print("JUGADOR vs JUGADOR")
    print("JUGADOR vs MÁQUINA")
    print("MÁQUINA vs MÁQUINA")
    opcion=int(input("Elige el modo de juego(1, 2 o 3) "))
    #print("Empiezan siempre X")
    return opcion

def imprimir(tablero):
    print("  1   2   3")
    for i in range(1, len(tablero)+1):
        print(i, end=" ")
        print(f" | ".join(tablero[i-1]))
        if i<3:
            print("  ----------")

def turnoJugador(ficha):
    print(f"Turno: {ficha}")
    condicion = True
    while condicion:
        columna = int(input("Introduce la columna (1-3): "))
        fila = int(input("Introduce la fila (1-3): "))
        if not (1 <= columna <= 3):
            print("La columna debe estar entre 1 y 3.")
            continue
        if not (1 <= fila <= 3):
            print("La fila debe estar entre 1 y 3.")
            continue
        if tablero[fila-1][columna-1] != " ":
            print("Esa casilla ya está ocupada. Elige otra.")
            continue
        tablero[fila-1][columna-1] = ficha
        condicion = False
    return tablero

def turnoMaquina(ficha):
    fila= random.randint(0,2)
    columna= random.randint(0,2)
    while tablero[fila][columna] != " ":
        fila = random.randint(0,2)
        columna = random.randint(0,2)
    tablero[fila][columna]=ficha
    
                    
    


def comprobarGanador():
    ganador = None
    while ganador is None:
        for i in range(len(tablero)):
            if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
                ganador = tablero[i][0] 
                return ganador
            if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
                ganador = tablero[0][i]
                return ganador
        if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
            ganador = tablero[0][0]
            return ganador
        if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
            ganador = tablero[0][2]
            return ganador

def comprobarEmpate():
    for i in tablero:
        for j in i:
            if j == " ":
                return False
    return True

            
def jugadorVSjugador():
    ganador = None
    while ganador is None:
        imprimir(tablero)
        turno_actual="X"
        turnoJugador(turno_actual)
        if turno_actual == "X":
            turno_actual = "O"
        else:
            turno_actual = "X"
        ganador = comprobarGanador()
    imprimir(tablero)
    if ganador:
        print(f"¡Ha ganado el jugador '{ganador}'!")
    elif comprobarEmpate():
        print("Tablero lleno ¡Ha habido un Empate!")

def jugadorVSmaquina():
    # Decidir quién empieza
    quien_empieza = ""
    while quien_empieza not in ["M", "J"]:
        quien_empieza = input("(La primera ficha es la X) ¿Quién empieza? (M/J): ").upper()

    turno_actual = "X" # 'X' siempre empieza
    ganador = None

    # Bucle principal del juego
    while ganador is None:
        imprimir(tablero)
        
        # Determinar a quién le toca mover en este turno
        if (quien_empieza == "J" and turno_actual == "X") | (quien_empieza == "M" and turno_actual == "O"):
            # Turno del jugador
            turnoJugador(turno_actual)
        else:
            # Turno de la máquina
            turnoMaquina(turno_actual)
    
        # Comprobar el estado del juego
        ganador = comprobarGanador()
        if ganador:
            print(f"¡Ha ganado el jugador '{ganador}'!")
        elif comprobarEmpate():
            print("Tablero lleno ¡Ha habido un Empate!")
        # Cambiar de ficha para el siguiente turno
        if turno_actual == "X":
            turno_actual = "O"
        else:
            turno_actual = "X"
    # Mostrar el resultado final
    imprimir(tablero)


        

def maquinaVSmaquina():
    i =0

#A mejorar, hacer funciones que se puedan usar directamente en el menú, sin que haya logica(jugadorVSjugador, jugaadorVSmaquina y maquinaVSmaquina)
#Crear funcion que te permita jugar otra partida
# Separar la logica de las funciones turnoMAquina y turnoJugador y juntar ganarYtablero lleno, para que este solo en ganar