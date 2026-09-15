from collections import deque

def jugada_sophia(monedas: deque, jugadas: list):

    if monedas[0] > monedas[-1]:
        eleccion = monedas.popleft()
        jugadas.append(eleccion)
        
    else:
        eleccion = monedas.pop()
        jugadas.append(eleccion)
    return eleccion
        
        

def jugada_mateo(monedas: deque, jugadas: list):
    if monedas[0] < monedas[-1]:
        eleccion = monedas.popleft()
        jugadas.append(eleccion)
        
    else:
        eleccion = monedas.pop()
        jugadas.append(eleccion)
    return eleccion

def jugar(monedas: deque, turno: str , mostrar_seguimiento: bool):

    sophia = []
    mateo = []
    sum_sophia = 0
    sum_mateo = 0
    mostrar = print if mostrar_seguimiento else (lambda *a, **k: None)
    mostrar(f"Estado inicial: {list(monedas)}")
    while monedas:
        mostrar(f"--------------------------------")
        if turno == "Sophia":
            eleccion = jugada_sophia(monedas, sophia)
            sum_sophia += eleccion
            mostrar(f"Turno: {turno:6}, Elección: {eleccion:4}, Puntaje Acumulado: {sum_sophia:4},\nEstado actual: {list(monedas)}")
            turno = "Mateo"
        else:
            eleccion = jugada_mateo(monedas, mateo)
            sum_mateo += eleccion
            mostrar(f"Turno: {turno:6}, Elección: {eleccion:4}, Puntaje Acumulado: {sum_mateo:4},\nEstado actual: {list(monedas)}")
            turno = "Sophia"
    mostrar(f"Puntaje Sophia: {sum_sophia:4} , Puntaje Mateo: {sum_mateo:4}")
    return [sophia, mateo]

