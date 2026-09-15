from pruebas import generar_entradas, obtener_semilla, TAMANIOS, REPETICIONES_POR_TAMANIO, CARPETA_CASOS

def main():
    semilla = obtener_semilla()
    for n in TAMANIOS:
        generar_entradas(n, REPETICIONES_POR_TAMANIO, f"{CARPETA_CASOS}/caso_n{n:06d}.txt", semilla)
        print(f"Generado: caso_n{n:06d}.txt")

if __name__ == "__main__":
    main()
