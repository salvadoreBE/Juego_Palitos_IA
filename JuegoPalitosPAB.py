import math

def minimax_alpha_beta(palitos, alpha, beta, es_turno_max):
    if palitos == 0:
        if es_turno_max:
            return -1  
        else:
            return 1   

    if es_turno_max:
        valor_max = -math.inf
        for i in range(1, 4):
            if palitos >= i:
                valor = minimax_alpha_beta(palitos - i, alpha, beta, False)
                valor_max = max(valor_max, valor)
                alpha = max(alpha, valor_max)
                if alpha >= beta:
                    break
        return valor_max
    else:
        valor_min = math.inf
        for i in range(1, 4):
            if palitos >= i:
                valor = minimax_alpha_beta(palitos - i, alpha, beta, True)
                valor_min = min(valor_min, valor)
                beta = min(beta, valor_min)
                if beta <= alpha:
                    break
        return valor_min

def jugar_palitos():
    palitos_totales = 13  # Número total de palitos
    turno_max = True  # Indica si es el turno del jugador Max

    while palitos_totales > 0:
        print("Palitos restantes:", palitos_totales)

        if turno_max:
            print("Turno del jugador humano")
            palitos_retirados = int(input("Ingresa el número de palitos que deseas retirar (1-3): "))
            if not (1 <= palitos_retirados <= 3 and palitos_retirados <= palitos_totales):
                print("Movimiento inválido. Intenta nuevamente.")
                continue
        else:
            print("Turno de la máquina")
            palitos_retirados = minimax_alpha_beta(palitos_totales, -math.inf, math.inf, True)
            print("La máquina retira", palitos_retirados)

        palitos_totales -= palitos_retirados
        turno_max = not turno_max

    if turno_max:
        print("Ganaste!")
    else:
        print("La IA ganó")
        
jugar_palitos()
