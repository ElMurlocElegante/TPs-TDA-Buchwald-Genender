import generador
from collections import deque
from src import logica, validar_archivo

def main():
	generador.generar_entradas()
	juegos: deque = validar_archivo.check_file(generador.obtener_ruta())
	
	generador.eliminar_entradas()