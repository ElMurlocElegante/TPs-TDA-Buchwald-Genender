from collections import deque

def detectar_jugador(argv, argc):
    if argc != 3:
        return "Sophia"
    if argv[2] != "Sophia" and argv[2] != "Mateo":
        return None
    return argv[2]

def check_file(file_route):
    try:
        file = open(file_route)
    except:
        print("Error: Archivo inválido")
        return None
    
    line = file.readline()
    juegos = []
    while line != "":
        monedas = line.split()
        monedas = deque(int(x) for x in monedas) 
        juegos.append(monedas)
        line = file.readline()

    file.close()

    return juegos

