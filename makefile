.PHONY: run run_mateo pruebas

run:
	python3 src/main.py inputs/entrada1.txt

run_mateo:
	python3 src/main.py inputs/entrada1.txt mateo

pruebas:
	python3 pruebas/pruebas.py
	python3 pruebas/medicion_complejidad.py
test:
	python3 -m pruebas.tests
