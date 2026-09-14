import time
import unittest
from collections import deque

from src import jugar, check_file
from pruebas import generar_entradas, eliminar_entradas, obtener_ruta

def calcular_suma(s, m):
	'''Retorna la suma de los elemntos de `s`, y la suma de los elementos de `m`'''
	return sum(s), sum(m)


class TestJugar(unittest.TestCase):


	def test_una_moneda_sophia_primero(self):
		'''Con una sola moneda, Sophia la toma y Mateo no tiene ninguna'''
		monedas = deque([5])
		s, m = jugar(monedas, "Sophia")
		sum_s, sum_m = calcular_suma(s, m)
		self.assertEqual(sum_s, 5)
		self.assertEqual(sum_m, 0)

	def test_dos_monedas_sophia_toma_mayor(self):
		'''Sophia toma la mayor entre dos monedas'''
		monedas = deque([3, 7])
		s, m = jugar(monedas, "Sophia")
		sum_s, sum_m = calcular_suma(s, m)
		self.assertGreaterEqual(sum_s, sum_m)
		self.assertEqual(sum_s + sum_m, 10)

	def test_sophia_siempre_gana_o_empata(self):
		'''Sophia gana en diferentes casos'''
		casos = [
			[1, 2, 3, 4],
			[4, 3, 2, 1],
			[1, 100, 2],
			[5, 5, 5, 5],
			[10, 1, 10, 1],
			[3, 1, 4, 1, 5, 9, 2, 6],
		]
		for caso in casos:
			with self.subTest(monedas=caso):
				s, m = jugar(deque(caso), "Sophia")
				sum_s, sum_m = calcular_suma(s, m)
				self.assertGreaterEqual(sum_s, sum_m,
					f"Sophia perdió con monedas={caso}: Sophia={sum_s}, Mateo={sum_m}")

	def test_suma_total_conservada(self):
		'''La suma de monedas de Sophia y Mateo debe ser igual a la suma total de monedas'''
		monedas = [3, 1, 4, 1, 5, 9]
		s, m = jugar(deque(monedas), "Sophia")
		sum_s, sum_m = calcular_suma(s, m)
		self.assertEqual(sum_s + sum_m, sum(monedas))

	def test_empate_solo_con_monedas_iguales(self):
		'''Sophia y Mateo empatan con monedas iguales'''
		monedas = deque([7, 7, 7, 7])
		s, m = jugar(monedas, "Sophia")
		sum_s, sum_m = calcular_suma(s, m)
		self.assertEqual(sum_s, sum_m)

	def test_turno_inicial_mateo(self):
		'''Si empieza Mateo, Sophia igual no debe perder'''
		monedas = deque([4, 2, 3, 1])
		s, m = jugar(monedas, "Mateo")
		sum_s, sum_m = calcular_suma(s, m)
		self.assertGreaterEqual(sum_s, sum_m)


class TestCheckFile(unittest.TestCase):

	def setUp(self):
		self.ruta = obtener_ruta("caso_01.txt")

	def tearDown(self):
		eliminar_entradas("caso_01.txt")

	def _escribir_archivo(self, contenido: str):
		self.ruta.parent.mkdir(parents=True, exist_ok=True)
		self.ruta.write_text(contenido)

	def test_archivo_invalido(self):
		'''Archivo inexistente retorna None'''
		resultado = check_file("/ruta/que/no/existe.txt")
		self.assertIsNone(resultado)

	def test_una_linea(self):
		'''Archivo con una línea genera un juego'''
		self._escribir_archivo("1 2 3 4\n")
		juegos = check_file(self.ruta)
		self.assertEqual(len(juegos), 1)
		self.assertEqual(list(juegos[0]), [1, 2, 3, 4])

	def test_multiples_lineas(self):
		'''Cada línea del archivo es un juego independiente'''
		self._escribir_archivo("1 2 3\n4 5 6\n7 8 9\n")
		juegos = check_file(self.ruta)
		self.assertEqual(len(juegos), 3)

	def test_valores_correctos(self):
		'''Los valores numéricos se parsean correctamente'''
		self._escribir_archivo("10 20 30\n")
		juegos = check_file(self.ruta)
		self.assertEqual(list(juegos[0]), [10, 20, 30])

	def test_archivo_vacio(self):
		'''Archivo vacío retorna lista vacía'''
		self._escribir_archivo("")
		juegos = check_file(self.ruta)
		self.assertEqual(juegos, [])


class TestConGeneradorAleatorio(unittest.TestCase):

	def tearDown(self):
		eliminar_entradas("caso_01.txt")

	def resultado(self, n, l):
		generar_entradas(n, l, "caso_01.txt")
		juegos = check_file(obtener_ruta("caso_01.txt"))
		self.assertIsNotNone(juegos)
		for monedas in juegos:
			s, m = jugar(deque(monedas), "Sophia")
			sum_s, sum_m = calcular_suma(s, m)
			self.assertGreaterEqual(sum_s, sum_m)

	def test_sophia_gana_con_entrada_aleatoria_000100(self):
		'''Sophia Gana/Empata en un set de 100 monedas aleatorias'''
		self.resultado(100, 1)

	def test_sophia_gana_con_entrada_aleatoria_001000(self):
		'''Sophia Gana/Empata en un set de 1000 monedas aleatorias'''
		self.resultado(1000, 1)

	def test_sophia_gana_con_entrada_aleatoria_010000(self):
		'''Sophia Gana/Empata en un set de 10000 monedas aleatorias'''
		self.resultado(10000, 1)

	def test_sophia_gana_con_entrada_aleatoria_050000(self):
		'''Sophia Gana/Empata en un set de 50000 monedas aleatorias'''
		self.resultado(50000, 1)

	def test_sophia_gana_con_entrada_aleatoria_100000(self):
		'''Sophia Gana/Empata en un set de 100000 monedas aleatorias'''
		self.resultado(100000, 1)


class ColorRunner(unittest.TextTestRunner):
	'''Diseño y Coloreo para la impresion de pruebas'''
	VERDE = "\033[92m"
	ROJO = "\033[91m"
	AMARILLO = "\033[93m"
	AZUL = "\033[94m"
	GRIS = "\033[90m"
	RESET = "\033[0m"
	NEGRITA = "\033[1m"

	class ColorResult(unittest.TextTestResult):

		VERDE = "\033[92m"
		ROJO = "\033[91m"
		AMARILLO = "\033[93m"
		GRIS = "\033[90m"
		RESET = "\033[0m"
		NEGRITA = "\033[1m"

		def startTest(self, test):
			self._start_time = time.time()
			super(unittest.TextTestResult, self).startTest(test)

		def _elapsed(self):
			return time.time() - self._start_time

		def addSuccess(self, test):
			super(unittest.TextTestResult, self).addSuccess(test)
			nombre = test.shortDescription() or test._testMethodName
			self.stream.write(f"  {self.VERDE}✔{self.RESET}  {nombre} {self.GRIS}({self._elapsed():.6f}s){self.RESET}\n")

		def addFailure(self, test, err):
			super(unittest.TextTestResult, self).addFailure(test, err)
			nombre = test.shortDescription() or test._testMethodName
			self.stream.write(f"  {self.ROJO}✘{self.RESET}  {nombre} {self.GRIS}({self._elapsed():.6f}s){self.RESET}\n")

		def addError(self, test, err):
			super(unittest.TextTestResult, self).addError(test, err)
			nombre = test.shortDescription() or test._testMethodName
			self.stream.write(f"  {self.AMARILLO}!{self.RESET}  {nombre} {self.GRIS}({self._elapsed():.6f}s){self.RESET}\n")

		def printErrors(self):
			if self.failures or self.errors:
				self.stream.write(f"\n{self.NEGRITA}Detalles:{self.RESET}\n")
			super().printErrors()

	def run(self, suite):
		clases = {}
		for test in suite:
			for caso in test:
				nombre_clase = type(caso).__name__
				clases.setdefault(nombre_clase, []).append(caso)

		result = self.ColorResult(self.stream, self.descriptions, self.verbosity)
		start = time.time()

		for nombre_clase, tests in clases.items():
			self.stream.write(f"\n{self.AZUL}{self.NEGRITA}{nombre_clase}{self.RESET}\n")
			for test in tests:
				test(result)

		elapsed = time.time() - start
		total = result.testsRun
		fallos = len(result.failures) + len(result.errors)
		ok = total - fallos

		self.stream.write(f"\n{'─' * 40}\n")
		if fallos == 0:
			self.stream.write(f"{self.VERDE}{self.NEGRITA}✔ {ok}/{total} tests pasaron{self.RESET} {self.GRIS}({elapsed:.6f}s){self.RESET}\n")
		else:
			self.stream.write(f"{self.ROJO}{self.NEGRITA}✘ {fallos}/{total} tests fallaron{self.RESET} {self.GRIS}({elapsed:.6f}s){self.RESET}\n")

		result.printErrors()
		return result


if __name__ == "__main__":
	unittest.main(testRunner=ColorRunner, verbosity=2)