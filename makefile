.PHONY: run run_mateo pruebas

run:
	python3 src/main.py inputs/entrada1.txt

run_mateo:
	python3 src/main.py inputs/entrada1.txt mateo

pruebas:
	python3 -m pruebas.generador_pruebas
	python3 -m pruebas.medicion_complejidad
test:
	python3 -m pruebas.tests
