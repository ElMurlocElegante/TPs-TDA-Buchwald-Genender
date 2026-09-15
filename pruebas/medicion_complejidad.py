import time
from collections import deque
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from src import jugar, check_file
from pruebas import obtener_ruta, TAMANIOS, CARPETA_CASOS, CARPETA_RESULTADOS

TIEMPO_MINIMO_POR_MEDICION = 0.05
JUGADOR_INICIAL = "Sophia"


def medir_tiempo_promedio(juego, tiempo_minimo=TIEMPO_MINIMO_POR_MEDICION):
	'''
	Calcula el tiempo promedio (en ms) de completar un determinado `juego`.
	Repite el mismo juego múltiples veces hasta alcanzar el `tiempo_minimo`, calculando así el promedio de ejecución para el caso. 
	'''
	iteraciones = 0
	total = 0.0
	while total < tiempo_minimo:
		copia = deque(juego)
		inicio = time.perf_counter()
		jugar(copia, JUGADOR_INICIAL , False)
		total += time.perf_counter() - inicio
		iteraciones += 1
	return (total / iteraciones) * 1000.0


def _rutas_casos(carpeta: str) -> list[Path]:
	'''
	Devuelve las rutas de los archivos de casos para cada tamaño en TAMANIOS.
	'''
	return [obtener_ruta(f"{carpeta}/caso_n{n:06d}.txt") for n in TAMANIOS]


def _medir_archivo(archivo: Path) -> dict[int, list[float]]:
	'''
	Mide el tiempo promedio de cada juego en `archivo`. Devuelve {n: [tiempos_ms]}.
	'''
	tiempos = {}
	juegos = check_file(archivo)
	if not juegos:
		return tiempos
	for juego in juegos:
		n = len(juego)
		t = medir_tiempo_promedio(juego)
		tiempos.setdefault(n, []).append(t)
		print(f"  n={n:>6}  tiempo={t:.6f} ms  archivo={archivo.name}")
	return tiempos


def medir_carpeta(carpeta: str):
	'''
	Mide tiempos de todos los casos en `carpeta`. Devuelve (n_valores, tiempos_promedio_ms).
	'''
	rutas = _rutas_casos(carpeta)
	if not rutas:
		raise SystemExit(f"No se encontraron archivos en '{carpeta}'")

	tiempos_por_n: dict[int, list[float]] = {}
	for archivo in rutas:
		for n, ts in _medir_archivo(archivo).items():
			tiempos_por_n.setdefault(n, []).extend(ts)

	n_valores = np.array(sorted(tiempos_por_n))
	tiempos = np.array([np.mean(tiempos_por_n[n]) for n in n_valores])
	return n_valores, tiempos


def ajustar_cuadrados_minimos(x, y, funciones_base):
	'''
	Calculo de Cuadrados Mínimos.
	'''
	A = np.column_stack([f(x) for f in funciones_base])
	AtA = A.T @ A
	Atb = A.T @ y
	c = np.linalg.solve(AtA, Atb)
	prediccion = A @ c
	error_cuadratico_total = float(np.sum((prediccion - y) ** 2))
	return c, error_cuadratico_total, prediccion


def _graficar_ajuste(ax, n_valores, tiempos, coeficientes):
	'''
	Grafica las mediciones y la curva de ajuste O(n).
	'''
	n_fino  = np.linspace(n_valores.min(), n_valores.max(), 300)
	y_ajuste = coeficientes[0] * n_fino + coeficientes[1]
	label   = f"Ajuste O(n): {coeficientes[0]:.3e}·n + {coeficientes[1]:.3e}"

	ax.plot(n_valores, tiempos,  "o",  color="tab:blue", label="Medición")
	ax.plot(n_fino, y_ajuste, "--", color="tab:red",  label=label)
	ax.set_title("Tiempo de ejecución de jugar() vs. cantidad de monedas")
	ax.set_xlabel("Cantidad de monedas (n)")
	ax.set_ylabel("Tiempo (ms)")
	ax.legend()


def _graficar_error(ax, n_valores, tiempos, prediccion):
	'''
	Grafica el error absoluto del ajuste por tamaño.
	'''
	error = np.abs(prediccion - tiempos)
	ax.plot(n_valores, error, "o-", color="tab:red")
	ax.set_title("Error absoluto del ajuste O(n) por tamaño")
	ax.set_xlabel("Cantidad de monedas (n)")
	ax.set_ylabel("Error absoluto (ms)")


def graficar(n_valores, tiempos, coeficientes, prediccion, carpeta_salida) -> tuple[Path, Path]:
	'''
	Genera y guarda los gráficos de ajuste y error. Devuelve las rutas guardadas.
	'''
	fig1, ax1 = plt.subplots(figsize=(9, 5.5))
	_graficar_ajuste(ax1, n_valores, tiempos, coeficientes)
	fig1.tight_layout()
	ruta1 = obtener_ruta(f"{carpeta_salida}/ajuste_cuadrados_minimos.png")
	fig1.savefig(ruta1, dpi=150)

	fig2, ax2 = plt.subplots(figsize=(9, 5.5))
	_graficar_error(ax2, n_valores, tiempos, prediccion)
	fig2.tight_layout()
	ruta2 = obtener_ruta(f"{carpeta_salida}/error_ajuste.png")
	fig2.savefig(ruta2, dpi=150)

	return ruta1, ruta2


def main():
	print(f"Midiendo tiempos de ejecución a partir de '{CARPETA_CASOS}' ...")
	n_valores, tiempos = medir_carpeta(CARPETA_CASOS)

	ruta = obtener_ruta(f"{CARPETA_RESULTADOS}/tiempos.csv")
	with open(ruta, "w") as f:
		f.write("n,tiempo_promedio_ms\n")
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
	print(f"Datos guardados en: {ruta}")


if __name__ == "__main__":
	main()