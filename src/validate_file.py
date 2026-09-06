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
        juegos.append(monedas)
        line = file.readline()

    file.close()

    return juegos
