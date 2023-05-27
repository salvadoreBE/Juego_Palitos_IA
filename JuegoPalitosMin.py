import random

def palitos(n):
    print("Palitos: " + "|" * n)

def player_turn(n):
    while True:
        choice = input("¿Cuántos palitos quieres retirar? (1-3): ")
        if choice.isdigit() and int(choice) in [1, 2, 3]:
            choice = int(choice)
            if choice > n:
                print("No puedes retirar más palitos de los que hay en total.")
            else:
                n = n - choice
                palitos(n)
                return n
        else:
            print("Ingresa un número válido.")

def IA_turno(n):
    if n == 1:
        print("Ganaste")
        return 0

    best_choice = None
    best_value = float("inf")

    for choice in [1, 2, 3]:
        if n - choice >= 1:
            value = minimax(n - choice, False)
            if value < best_value:
                best_value = value
                best_choice = choice

    print("La IA quita", best_choice, "palitos.")
    n = n - best_choice
    palitos(n)
    return n

def minimax(n, is_maximizing):
    if n == 1:
        return 1 if is_maximizing else -1

    if is_maximizing:
        best_value = float("-inf")
        for choice in [1, 2, 3]:
            if n - choice >= 1:
                value = minimax(n - choice, False)
                best_value = max(best_value, value)
        return best_value
    else:
        best_value = float("inf")
        for choice in [1, 2, 3]:
            if n - choice >= 1:
                value = minimax(n - choice, True)
                best_value = min(best_value, value)
        return best_value

def jugar():
    n = random.randint(20, 23)
    palitos(n)

    while n > 0:
        n = player_turn(n)
        if n == 0:
            print("La IA gano")
            break
        n = IA_turno(n)

jugar()
