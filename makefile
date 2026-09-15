.PHONY: run run_mateo pruebas test venv requirements init clean

venv:
	python3 -m venv venv

requirements: venv
	./venv/bin/pip install -r requirements.txt

init: requirements

run:
	python3 src/main.py inputs/entrada1.txt

run_mateo:
	python3 src/main.py inputs/entrada1.txt Mateo

pruebas:
	python3 -m pruebas.generador_pruebas
	python3 -m pruebas.medicion_complejidad

test:
	python3 -m pruebas.tests

clean:
	rm -rf venv pruebas/casos pruebas/resultados