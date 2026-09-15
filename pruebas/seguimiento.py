from collections import deque

from src import logica

# def mostrar_seguimiento(turno , estado_actual , eleccion , puntaje):
#     print(f"Turno: {turno}, Elección: {eleccion}, Puntaje Acumulado: {puntaje}")


# def jugar_con_seguimiento( monedas:deque ,  turno: str):
#     sophia = []
#     mateo = []
#     sum_sophia = 0
#     sum_mateo = 0
#     print(f"Estado inicial: {monedas} , Puntaje acumulado Sophia: {sum_sophia}, Puntaje acumulado Mateo: {sum_mateo}")
#     while monedas:
#         if turno == "Sophia":
#             eleccion = logica.jugada_sophia(monedas, sophia)
#             sum_sophia += eleccion
#             mostrar_seguimiento(turno, monedas, eleccion, sum_sophia)
#             turno = "Mateo"
#         else:
#             eleccion = logica.jugada_mateo(monedas, mateo)
#             sum_mateo += eleccion
#             mostrar_seguimiento(turno , monedas , eleccion , sum_mateo)
#             turno = "Sophia"
#     print(f"Puntaje final Sophia: {sum_sophia}, Puntaje final Mateo: {sum_mateo}")
#     return [sophia, mateo]

def seguimiento():