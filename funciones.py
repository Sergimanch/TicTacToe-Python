import random

def cara_cruz():
    arr = ["cara", "cruz"]
    choice = random.choice(arr)
    return choice

def presentacion():
    jugador = input("Introduce tu nombre: ")
    edad = int(input("Introduce tu edad: "))
    ficha = input("Introduce una ficha para jugar: ")
    print(f"Hola, {jugador}, ({edad}). Juegas con la ficha: {ficha})")
    return ficha
def menu():
    # Muestra el menú de opciones y devuelve la selección del usuario
    print("\n--- Tres en Raya ---")
    print("1. JUGADOR vs JUGADOR")
    print("2. JUGADOR vs MÁQUINA")
    print("3. MÁQUINA vs MÁQUINA")
    opcion = int(input("Elige el modo de juego(1, 2 o 3) "))
    return opcion


def dimensiones():
    num = int(input("Introduce las dimensiones del tablero "))
    return num
N = dimensiones()

# Inicializa el tablero vacío como una matriz NxN con espacios en blanco
tablero = [[" " for _ in range(N)] for _ in range(N)]

def reiniciar_tablero():
    global tablero
    tablero = [[" " for _ in range(N)] for _ in range(N)]

def imprimir(tab):
    # Imprime encabezado de columnas
    print("   " + "   ".join(str(i+1) for i in range(len(tab))))
    for i in range(len(tab)):
        print(i+1, end="  ")
        print(" | ".join(tab[i]))
        if i < len(tab) - 1:
            print("   " + "-" * (4 * len(tab) - 3))

def turnoJugador(ficha):
    condicion = True
    while condicion:
        columna = int(input(f"Introduce la columna (1-{N}): "))
        fila = int(input(f"Introduce la fila (1-{N}): "))
        if not (1 <= columna <= N):
            print(f"La columna debe estar entre 1 y {N}.")
            continue
        if not (1 <= fila <= N):
            print(f"La fila debe estar entre 1 y {N}.")
            continue
        if tablero[fila-1][columna-1] != " ":
            print("Esa casilla ya está ocupada. Elige otra.")
            continue
        tablero[fila-1][columna-1] = ficha
        condicion = False
    return tablero

def turnoMaquina(ficha):
    global tablero
    fila = random.randint(0, N-1)
    columna = random.randint(0, N-1)
    while tablero[fila][columna] != " ":
        fila = random.randint(0, N-1)
        columna = random.randint(0, N-1)
    tablero[fila][columna] = ficha

def comprobarGanador():
    # Comprueba filas
    for i in range(N):
        if tablero[i][0] != " " and all(tablero[i][j] == tablero[i][0] for j in range(1, N)):
            return tablero[i][0]

    # Comprueba columnas
    for j in range(N):
        if tablero[0][j] != " " and all(tablero[i][j] == tablero[0][j] for i in range(1, N)):
            return tablero[0][j]

    # Diagonal principal
    if tablero[0][0] != " " and all(tablero[i][i] == tablero[0][0] for i in range(1, N)):
        return tablero[0][0]

    # Diagonal secundaria
    if tablero[0][N-1] != " " and all(tablero[i][N-1-i] == tablero[0][N-1] for i in range(1, N)):
        return tablero[0][N-1]

    # Si no hay ganador
    return None

def comprobarEmpate():
    for fila in tablero:
        for casilla in fila:
            if casilla == " ":
                return False
    return True

def jugadorVSjugador():
    j1 = presentacion()
    j2 = presentacion()
    # Controla el modo de juego jugador contra jugador
    reiniciar_tablero()
    turno = cara_cruz()
    if turno == "cara":
        turno_actual = j2
        print(f"Ha salido cara empiezan {j1}")
    else:
        turno_actual = j1
        print(f"Ha salido cruz empiezan {j2}")
    
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

        # Alterna turnos entre X y O
        if turno_actual == j1:
            turno_actual = j2
        else:
            turno_actual = j1

def jugadorVSmaquina():
    # Controla el juego jugador contra máquina, pregunta quién empieza
    reiniciar_tablero()
    turno = cara_cruz()
    if turno == "Cara":
        turno_actual = "O"
        quien_empieza = "J"
        print("Ha salido cara empiezan O")
    else:
        turno_actual = "X"
        print("Ha salido cruz empiezan X")
        quien_empieza =="M"
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
            
        # Cambia el turno
        if turno_actual == "X":
            turno_actual = "O"
        else:
            turno_actual = "X"

def maquinaVSmaquina():
    # Controla el juego máquina contra máquina, movimientos aleatorios de ambos
    reiniciar_tablero()
    turno = cara_cruz()
    if turno == "Cara":
        turno_actual = "O"
        print("Ha salido cara empiezan O")
    else:
        turno_actual = "X"
        print("Ha salido cruz empiezan X")
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
