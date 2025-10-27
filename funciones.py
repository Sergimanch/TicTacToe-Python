import random

tablero = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def reiniciar_tablero():
    global tablero
    tablero = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def menu():
    print("\n--- Tres en Raya ---")
    print("1. JUGADOR vs JUGADOR")
    print("2. JUGADOR vs MÁQUINA")
    print("3. MÁQUINA vs MÁQUINA")
    opcion = int(input("Elige el modo de juego(1, 2 o 3) "))
    return opcion

def imprimir(tab):
    print("  1   2   3")
    for i in range(1, len(tab)+1):
        print(i, end=" ")
        print(f" | ".join(tab[i-1]))
        if i<3:
            print("  ----------")

def turnoJugador(ficha):
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
        return None
    
def comprobarEmpate():
    for i in tablero:
        for j in i:
            if j == " ":
                return False
    return True
           
def jugadorVSjugador():
    reiniciar_tablero()
    turno_actual = "X"
    
    while True:
        imprimir(tablero)
        turnoJugador(turno_actual)
        
        ganador = comprobarGanador()
        if ganador:
            imprimir(tablero)
            print(f"¡Ha ganado el jugador '{ganador}'!")
            break
            
        if comprobarEmpate():
            imprimir(tablero)
            print("¡Es un empate!")
            break

        if turno_actual == "X":
            turno_actual = "O"
        else:
            turno_actual = "X"

def jugadorVSmaquina():
    reiniciar_tablero()
    quien_empieza = ""
    while quien_empieza not in ["J", "M"]:
        quien_empieza = input("¿Quién empieza? (J para jugador / M para máquina): ").upper()

    turno_actual = "X"
    while True:
        imprimir(tablero)
        
        es_turno_jugador = (quien_empieza == "J" and turno_actual == "X") or (quien_empieza == "M" and turno_actual == "O")
        
        if es_turno_jugador:
            turnoJugador(turno_actual)
        else:
            turnoMaquina(turno_actual)
            
        ganador = comprobarGanador()
        if ganador:
            imprimir(tablero)
            print(f"¡Ha ganado '{ganador}'!")
            break

        if comprobarEmpate():
            imprimir(tablero)
            print("¡Es un empate!")
            break
            
        if turno_actual == "X":
            turno_actual = "O"
        else:
            turno_actual = "X"
        

def maquinaVSmaquina():
    reiniciar_tablero()
    turno_actual = "X"
    while True:
        imprimir(tablero)
        ganador = comprobarGanador()
        turnoMaquina(turno_actual)
        if ganador:
            imprimir(tablero)
            print(f"¡Ha ganado '{ganador}'!")
            break

        if comprobarEmpate():
            imprimir(tablero)
            print("¡Es un empate!")
            break
            
        if turno_actual == "X":
            turno_actual = "O"
        else:
            turno_actual = "X"


#A mejorar, hacer funciones que se puedan usar directamente en el menú, sin que haya logica(jugadorVSjugador, jugaadorVSmaquina y maquinaVSmaquina)
#Crear funcion que te permita jugar otra partida
# Separar la logica de las funciones turnoMAquina y turnoJugador y juntar ganarYtablero lleno, para que este solo en ganar