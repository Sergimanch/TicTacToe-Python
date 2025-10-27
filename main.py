import funciones

match funciones.menu():
    case 1:
        print("Jugador ⚔️ Jugador")
        funciones.jugadorVSjugador()
    case 2:
        print("Jugador ⚔️ Máquina")
        funciones.jugadorVSmaquina()
    case 3:
        print("Máquina ⚔️ Máquina")
