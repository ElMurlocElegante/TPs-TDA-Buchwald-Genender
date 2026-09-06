import sys
from validate_file import check_file
import logic

def main():
    argc = len(sys.argv)
    if argc < 1:
        return 1
    juegos = check_file(sys.argv[1])
    if juegos == None:
        print("Error: No hay juegos en el archivo dado")
        return 1
    print("Todo OK")
    print(sys.argv)
    for juego in juegos:
        print(juego)

if __name__ == "__main__":
    main()