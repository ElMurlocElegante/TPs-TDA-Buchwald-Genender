from collections import deque

def jugada_sophia(monedas: deque, jugadas: list):

    if monedas[0] > monedas[-1]:
        jugadas.append(monedas.popleft())
        
    else:
        jugadas.append(monedas.pop())
        
        

def jugada_mateo(monedas: deque, jugadas: list):
    if monedas[0] < monedas[-1]:
        jugadas.append(monedas.popleft())
        
    else:
        jugadas.append(monedas.pop())
        

def jugar(monedas: deque, turno: str):

    sophia = []
    mateo = []

    while monedas:
        if turno == "Sophia":
            jugada_sophia(monedas, sophia)
            turno = "Mateo"
        else:
            jugada_mateo(monedas, mateo)
            turno = "Sophia"
    return [sophia, mateo] 