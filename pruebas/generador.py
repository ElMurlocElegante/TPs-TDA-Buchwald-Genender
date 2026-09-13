import random
from pathlib import Path

def obtener_ruta():
	'''
	Obtiene la ruta absoluta para el archivo de entrada de testeo.
	'''
	dir_script = Path(__file__).resolve().parent
	ruta_archivo = dir_script / "../inputs/test.txt"
	ruta_archivo.parent.mkdir(parents=True, exist_ok=True)
	return ruta_archivo

def generar_entradas(r):
	'''
	Genera un archivo de entrada de testeo aleatorio.\n
	El archivo tendrá `r` monedas, cada una con un valor entero entre 1 y 100.
	'''
	ruta = obtener_ruta()
	file = open(ruta, "w+")
	for _ in range(r):
		moneda = random.randint(1, 100)
		file.write(f"{moneda} ")

	file.seek(file.tell() - 1)
	file.truncate()
	file.close()

def eliminar_entradas():
	'''
	Elimina el archivo de entrada de testeo.
	'''
	ruta = obtener_ruta()
	ruta.unlink(missing_ok=True)

if __name__ == '__main__':
	generar_entradas(1000)