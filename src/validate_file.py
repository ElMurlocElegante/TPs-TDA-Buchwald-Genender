def check_file(file_route):
    juegos = [[]]
    try:
        file = open(file_route)
    except:
        print("Error: Archivo inválido")
        return None
    
    line = file.readline()

    while line:
        monedas = line.split()
        juegos.append(monedas)
        line = file.readline()

    file.close()

    return juegos
