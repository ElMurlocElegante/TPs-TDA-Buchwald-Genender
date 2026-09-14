import random
from pathlib import Path

VALOR_MIN, VALOR_MAX = 1, 100

def semilla():
	'''
	Obtiene la semilla generadora.
	'''
	return random.Random(12345)

def obtener_ruta(archivo):
	'''
	Obtiene la ruta absoluta para el `archivo` de entrada de testeo.
	'''
	dir_script = Path(__file__).resolve().parent
	ruta_archivo = dir_script / f"../pruebas/casos/{archivo}"
	ruta_archivo.parent.mkdir(parents=True, exist_ok=True)
	return ruta_archivo

def eliminar_entradas(archivo):
	'''
	Elimina el archivo de entrada de testeo.
	'''
	ruta = obtener_ruta(archivo)
	ruta.unlink(missing_ok=True)

def generar_juego(m, semilla):
	'''
	Genera un juego de `m` monedas.
	'''
	return [semilla.randint(VALOR_MIN, VALOR_MAX) for _ in range(m)]

def generar_entradas(m, l, archivo):
	'''
	Genera un archivo de entrada de testeo aleatorio.\n
	El archivo tendrá `l` lineas, cada una con `m` monedas de un valor entero entre 1 y 100.
	'''
	ruta = obtener_ruta(archivo)
	file = open(ruta, "w+")
	for _ in range(l):
		juego = generar_juego(m, semilla())
		file.write(" ".join(str(v) for v in juego) + "\n")
	file.close()