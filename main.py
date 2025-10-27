import funciones

tablero = [[" "," "," "],[" "," "," "],[" "," "," "]]
match funciones.menu():
    case 1:
        print("Jugador vs Jugador")
        funciones.imprimir(tablero)
        jugador = "X"
        condicion = True
        while condicion:
            funciones.turno(tablero, jugador)
            funciones.imprimir(tablero)
            if funciones.ganar(tablero):
                print(f"¡Ha ganado {funciones.ganar(tablero)}!")
                condicion = False
            if not funciones.tableroLLeno(tablero):
                print("¡Empate!")
                condicion = False
            if jugador == "X":
                jugador = "O"
            else:
                jugador = "X"
    case 2:
        print("Jugador vs Máquina")
        funciones.imprimir(tablero)
        condicion = True
        ficha = input("Introduce la ficha de la máquina (X/O)")
        while condicion:
            funciones.turnoMaquina(tablero, ficha)
            funciones.imprimir(tablero)
            if funciones.ganar(tablero):
                print(f"¡Ha ganado {funciones.ganar(tablero)}!")
                condicion = False
            if not funciones.tableroLLeno(tablero):
                print("¡Empate!")
                condicion = False
            
    case 3:
        print("Máquina vs Máquina")
