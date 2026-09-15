# TPs-TDA-Buchwald-Genender
Repositorio de Trabajos Prácticos de TDA.
El grupo está conformado por:
- Aaguss28: Agustín Leguizamón (111534)
- riceem: Ezequiel Meier (112916)
- ElMurlocElegante: Luciano Celano (112096)

# Ejecucion
Se cuenta con un Makefile para correr el TP.

```
    make init
```
Se encarga de la creacion del entorno de Python (venv) y la instalacion de dependencias dada por requirements.txt

```
    source venv/bin/activate
```
Entra en el entorno virtual de Python con sus dependencias


```
    make run
```
Ejecuta el TP con las entradas dadas en la carpeta '/inputs/*.txt"


```
    make pruebas
```
Genera un set de pruebas aleatorio guardado en /pruebas/casos y mide el tiempo de ejecucion entre juegos, muestra en consola f(n), su error cuadratico total y genera los graficos para su analisis en la carpeta /pruebas/resultados


```
    make test
```
Hace pruebas de los componentes en codigo con casos borde y muestra en consola su tiempo de ejecucion 


# Commits
Los commits deben seguir la siguiente estructura:
> ["PREFIX"] "title"
> 
> "summary"

EJ:
> [ADD] Contador de Letras
> - Creada la funcion para contar letras.
> - Cuenta letras en la palabra enviada.
## Prefijos
Se tiene que tomaru no de los siguientes prefijos, o múltiples si es que aplica.
- ADD: Nueva estructura o funcionalidad del proyecto.
- FIX: Bug fixes y otras cosas.
- REFACTOR: Cambio de una feature ya integrada para mejorar su funcionalidad.
- TEST: Adición/Modificación de testeos
- DOCS: Cambios de Documentación o Informe
- STYLE: Formateo.