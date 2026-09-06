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

    for juego in juegos:
        jugar(juego, sys.argv[2])


if __name__ == "__main__":
    main()