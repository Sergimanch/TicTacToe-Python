import funciones

comprobar = True
while comprobar:
    match funciones.menu():
        case 1:
            print("Jugador ⚔️  Jugador")
            funciones.jugadorVSjugador()
            comprobar = False
        case 2:
            print("Jugador ⚔️  Máquina")
            funciones.jugadorVSmaquina()
            comprobar = False
        case 3:
            print("Máquina ⚔️  Máquina")
            funciones.maquinaVSmaquina()
            comprobar = False
        case _:
            print ()
            print("Opcion incorrecta")