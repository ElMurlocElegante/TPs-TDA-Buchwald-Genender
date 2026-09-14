import os
import random

from pruebas import generar_entradas, obtener_ruta, obtener_semilla

CARPETA_CASOS = "pruebas/casos"

TAMANIOS = [200, 1000, 2000, 4000, 6000, 8000, 10000, 15000, 20000,
            25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000]

REPETICIONES_POR_TAMANIO = 8

def main():
    semilla = obtener_semilla()
    for n in TAMANIOS:
        generar_entradas(n, REPETICIONES_POR_TAMANIO, f"caso_n{n:06d}.txt", semilla)
        print(f"Generado: caso_n{n:06d}.txt")

if __name__ == "__main__":
    main()
