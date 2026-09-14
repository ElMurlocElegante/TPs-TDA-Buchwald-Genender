from collections import deque

def detectar_jugador(argc, argv):
    '''
    Detecta Qué jugador debe tomar el primer turno.
    - Si no se provió un nombre, se asume que `Sophia` empieza primero.
    - Si `argv` contiene `Sophia` o `Mateo`, lo devuelve. 
    - Si el parametro enviado es inválido, retorna `None`
    '''
    if argc != 3:
        return "Sophia"
    if argv[2] != "Sophia" and argv[2] != "Mateo":
        return None
    return argv[2]



def check_file(file_route):
    '''
    Valida un archivo dirigido por `file_route` y extrae sus datos formateados.\n
    Devuelve una `deque` en caso de éxito, o `None` en caso de error.
    '''
    try:
        file = open(file_route)
    except:
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

