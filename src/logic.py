def jugada_sophia(monedas: list, jugadas: list):

    if monedas[0] > monedas[-1]:
        jugadas.append(monedas[0])
        monedas.pop(0)
    else:
        jugadas.append(monedas[-1])
        monedas.pop()
    

def jugada_mateo(monedas: list, jugadas: list):
    if monedas[0] < monedas[-1]:
        jugadas.append(monedas[0])
        monedas.pop(0)
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
        else:
            jugada_mateo(monedas, mateo)
        cant -= 1
    return [sophia, mateo] 