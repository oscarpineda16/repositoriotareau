import math

# Representación del tablero (lista de 9 posiciones)
def imprimir_tablero(tablero):
    for i in range(0, 9, 3):
        print(tablero[i], tablero[i+1], tablero[i+2])
    print()

# Verificar si hay un ganador
def verificar_ganador(tablero, jugador):
    combinaciones = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(tablero[a] == tablero[b] == tablero[c] == jugador for a, b, c in combinaciones)

# Algoritmo Minimax
def minimax(tablero, profundidad, es_max):
    if verificar_ganador(tablero, "X"):
        return 10 - profundidad
    if verificar_ganador(tablero, "O"):
        return profundidad - 10
    if " " not in tablero:
        return 0  # Empate

    if es_max:  # Turno de la IA (X)
        mejor_valor = -math.inf
        for i in range(9):
            if tablero[i] == " ":
                tablero[i] = "X"
                valor = minimax(tablero, profundidad + 1, False)
                tablero[i] = " "
                mejor_valor = max(mejor_valor, valor)
        return mejor_valor
    else:  # Turno del jugador (O)
        peor_valor = math.inf
        for i in range(9):
            if tablero[i] == " ":
                tablero[i] = "O"
                valor = minimax(tablero, profundidad + 1, True)
                tablero[i] = " "
                peor_valor = min(peor_valor, valor)
        return peor_valor

# La IA encuentra la mejor jugada
def mejor_movimiento(tablero):
    mejor_valor = -math.inf
    mejor_mov = -1
    for i in range(9):
        if tablero[i] == " ":
            tablero[i] = "X"
            valor = minimax(tablero, 0, False)
            tablero[i] = " "
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_mov = i
    return mejor_mov

# Juego
tablero = [" "] * 9
turno_jugador = True

while True:
    imprimir_tablero(tablero)

    if verificar_ganador(tablero, "X"):
        print("¡La IA gana! 😎")
        break
    if verificar_ganador(tablero, "O"):
        print("¡Ganaste! 🎉")
        break
    if " " not in tablero:
        print("¡Empate! 🤝")
        break

    if turno_jugador:
        mov = int(input("Tu turno (0-8): "))
        if tablero[mov] == " ":
            tablero[mov] = "O"
            turno_jugador = False
    else:
        print("Turno de la IA...")
        mov = mejor_movimiento(tablero)
        tablero[mov] = "X"
        turno_jugador = True
