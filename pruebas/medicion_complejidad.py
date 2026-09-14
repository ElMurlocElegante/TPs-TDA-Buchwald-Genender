import glob
import os
import sys
import time

# sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from collections import deque

from src import jugar, check_file


CARPETA_CASOS = "pruebas/casos"
CARPETA_RESULTADOS = "pruebas/resultados"
TIEMPO_MINIMO_POR_MEDICION = 0.05
JUGADOR_INICIAL = "Sophia"


def medir_tiempo_promedio(juego, tiempo_minimo=TIEMPO_MINIMO_POR_MEDICION):
    iteraciones = 0
    total = 0.0
    while total < tiempo_minimo:
        copia = deque(juego)
        inicio = time.perf_counter()
        jugar(copia, JUGADOR_INICIAL)
        total += time.perf_counter() - inicio
        iteraciones += 1
    return total / iteraciones


def medir_carpeta(carpeta):
    archivos = sorted(glob.glob(os.path.join(carpeta, "*.txt")))
    if not archivos:
        raise SystemExit(f"No se encontraron archivos .txt en '{carpeta}'")

    tiempos_por_n = {}
    for archivo in archivos:
        juegos = check_file(archivo)
        if not juegos:
            continue
        for juego in juegos:
            n = len(juego)
            tiempo = medir_tiempo_promedio(juego)
            tiempos_por_n.setdefault(n, []).append(tiempo)
            print(f"n={n:>6}  tiempo={tiempo:.6e} s  archivo={os.path.basename(archivo)}")

    n_valores = np.array(sorted(tiempos_por_n))
    tiempo_promedio = np.array([np.mean(tiempos_por_n[n]) for n in n_valores])
    return n_valores, tiempo_promedio


def ajustar_cuadrados_minimos(x, y, funciones_base):
    A = np.column_stack([f(x) for f in funciones_base])
    AtA = A.T @ A
    Atb = A.T @ y
    c = np.linalg.solve(AtA, Atb)
    prediccion = A @ c
    error_cuadratico_total = float(np.sum((prediccion - y) ** 2))
    return c, error_cuadratico_total, prediccion


def graficar(n_valores, tiempos, coeficientes, prediccion, carpeta_salida):
    os.makedirs(carpeta_salida, exist_ok=True)
    n_fino = np.linspace(n_valores.min(), n_valores.max(), 300)
    f = lambda n: coeficientes[0] * n + coeficientes[1]

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.plot(n_valores, tiempos, "o", color="tab:blue", label="Medición")
    ax.plot(n_fino, f(n_fino), "--", color="tab:red",
            label=f"Ajuste O(n) = {coeficientes[0]:.3e}*n + {coeficientes[1]:.3e}")
    ax.set_title("Tiempo de ejecución de jugar() vs. cantidad de monedas")
    ax.set_xlabel("Cantidad de monedas (n)")
    ax.set_ylabel("Tiempo de ejecución (s)")
    ax.legend()
    fig.tight_layout()
    ruta1 = os.path.join(carpeta_salida, "ajuste_cuadrados_minimos.png")
    fig.savefig(ruta1, dpi=150)

    fig2, ax2 = plt.subplots(figsize=(9, 5.5))
    error_abs = np.abs(prediccion - tiempos)
    ax2.plot(n_valores, error_abs, "o-", color="tab:red")
    ax2.set_title("Error absoluto del ajuste O(n), por tamaño")
    ax2.set_xlabel("Cantidad de monedas (n)")
    ax2.set_ylabel("Error absoluto (s)")
    fig2.tight_layout()
    ruta2 = os.path.join(carpeta_salida, "error_ajuste.png")
    fig2.savefig(ruta2, dpi=150)

    return ruta1, ruta2


def main():
    print(f"Midiendo tiempos de ejecución a partir de '{CARPETA_CASOS}' ...")
    n_valores, tiempos = medir_carpeta(CARPETA_CASOS)

    os.makedirs(CARPETA_RESULTADOS, exist_ok=True)
    with open(os.path.join(CARPETA_RESULTADOS, "tiempos.csv"), "w") as f:
        f.write("n,tiempo_promedio_s\n")
        for n, t in zip(n_valores, tiempos):
            f.write(f"{n},{t}\n")

    funciones_base = [lambda n: n.astype(float), lambda n: np.ones_like(n, dtype=float)]
    coeficientes, error_cuadratico_total, prediccion = ajustar_cuadrados_minimos(
        n_valores, tiempos, funciones_base
    )

    print(f"\nAjuste O(n): f(n) = {coeficientes[0]:.6e}*n + {coeficientes[1]:.6e}")
    print(f"Error cuadrático total: {error_cuadratico_total:.6e}")

    ruta1, ruta2 = graficar(n_valores, tiempos, coeficientes, prediccion, CARPETA_RESULTADOS)
    print(f"\nGráficos guardados en:\n  {ruta1}\n  {ruta2}")
    print(f"Datos guardados en: {os.path.join(CARPETA_RESULTADOS, 'tiempos.csv')}")


if __name__ == "__main__":
    main()