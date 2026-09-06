import sys
from validate_file import check_file
from logic import jugar

def main():
    argc = len(sys.argv)
    if argc < 1:
        return 1
    juegos = check_file(sys.argv[1])
    if juegos == None:
        print("Error: No hay juegos en el archivo dado")
        return 1
    
    if len(sys.argv) == 3:
        primer_jugador = sys.argv[2]
    else:
        primer_jugador = "Sophia"

    for juego in juegos:
        print(jugar(juego, primer_jugador))


if __name__ == "__main__":
    main()