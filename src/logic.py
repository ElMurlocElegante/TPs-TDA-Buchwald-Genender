from collections import deque

def jugada_sophia(monedas: deque, jugadas: list):

    if monedas[0] > monedas[-1]:
        jugadas.append(monedas[0])
        monedas.popleft()
    else:
        jugadas.append(monedas[-1])
        monedas.pop()
    

def jugada_mateo(monedas: deque, jugadas: list):
    if monedas[0] < monedas[-1]:
        jugadas.append(monedas[0])
        monedas.popleft()
    else:
        jugadas.append(monedas[-1])
        monedas.pop()

def jugar(monedas: list, turno):

    sophia = []
    mateo = []

    cant = len(monedas)
    while cant != 0:
        if turno == "Sophia":
            jugada_sophia(monedas, sophia)
            turno = "Mateo"
        else:
            jugada_mateo(monedas, mateo)
            turno = "Sophia"
        cant -= 1
    return [sophia, mateo] 