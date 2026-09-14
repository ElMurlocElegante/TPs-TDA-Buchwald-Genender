import os
import random

CARPETA_CASOS = "pruebas/casos"

TAMANIOS = [200, 1000, 2000, 4000, 6000, 8000, 10000, 15000, 20000,
            25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000]

REPETICIONES_POR_TAMANIO = 8
VALOR_MIN, VALOR_MAX = -10000, 10000
SEED = 12345


def generar_juego(n, rng):
    return [rng.randint(VALOR_MIN, VALOR_MAX) for _ in range(n)]


def main():
    rng = random.Random(SEED)
    os.makedirs(CARPETA_CASOS, exist_ok=True)
    for n in TAMANIOS:
        ruta = os.path.join(CARPETA_CASOS, f"caso_n{n:06d}.txt")
        with open(ruta, "w") as f:
            for _ in range(REPETICIONES_POR_TAMANIO):
                juego = generar_juego(n, rng)
                f.write(" ".join(str(v) for v in juego) + "\n")
        print(f"Generado {ruta}")


if __name__ == "__main__":
    main()
