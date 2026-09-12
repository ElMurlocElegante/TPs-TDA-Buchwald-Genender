import sys
from validate_file import *
from logic import jugar

def imprimir_resultados(juego, primer_jugador):
    [s , m]  = jugar(juego, primer_jugador)
    puntos_s = sum(s)
    puntos_m = sum(m)
    print(f"Sophia\n Jugadas: {s}\n Total: {puntos_s}")
    print(f"Mateo\n Jugadas: {m}\n Total: {puntos_m}")
    if puntos_s > puntos_m:
        print(f"----Ganador: Sophia----")
    elif puntos_m > puntos_s:
        print(f"----Ganador: Mateo-----")
    else:
        print("---------Empate---------") 

def main():
    argc = len(sys.argv)
    if argc < 1:
        return 1
    juegos = check_file(sys.argv[1])
    if juegos == None:
        print("Error: No hay juegos en el archivo dado")
        return 1

    primer_jugador = detectar_jugador(sys.argv, argc)
    for i in range(0, len(juegos)):
        print(f"-----Resultados Juego {i}-----")        
        imprimir_resultados(juegos[i], primer_jugador)



if __name__ == "__main__":
    main()