# Función que revisa si es seguro colocar una reina
def es_posicion_segura(tablero, fila, columna, n):

    # Revisar si hay una reina en la misma columna
    # Solo revisamos las filas de arriba porque las de abajo aún están vacías
    for i in range(fila):
        if tablero[i][columna] == 1:
            return False   # No es seguro

    # Revisar la diagonal superior izquierda
    # Nos movemos hacia arriba y hacia la izquierda
    i, j = fila - 1, columna - 1
    while i >= 0 and j >= 0:
        if tablero[i][j] == 1:
            return False   # Hay una reina atacando en diagonal
        i -= 1
        j -= 1

    # Revisar la diagonal superior derecha
    # Nos movemos hacia arriba y hacia la derecha
    i, j = fila - 1, columna + 1
    while i >= 0 and j < n:
        if tablero[i][j] == 1:
            return False   # Hay una reina atacando en diagonal
        i -= 1
        j += 1

    # Si pasó todas las revisiones, la posición es segura
    return True


# Función principal que intenta colocar las N reinas
def n_reinas(tablero, fila, n):

    # Caso base: si ya llegamos a la fila n,
    # significa que colocamos todas las reinas
    if fila == n:
        for r in tablero:
            print(r)   # Mostrar solución encontrada
        print()
        return

    # Probar colocar una reina en cada columna de la fila actual
    for columna in range(n):

        # Verificar si se puede colocar una reina en esta posición
        if es_posicion_segura(tablero, fila, columna, n):

            # Colocar la reina
            tablero[fila][columna] = 1

            # Llamada recursiva para intentar colocar la siguiente reina
            # en la siguiente fila
            n_reinas(tablero, fila + 1, n)

            # BACKTRACKING:
            # Si no funcionó continuar con esta configuración,
            # quitamos la reina y probamos otra columna
            tablero[fila][columna] = 0


# Tamaño del tablero (N reinas)
n = 4

# Crear el tablero NxN lleno de ceros
tablero = [[0]*n for _ in range(n)]

# Iniciar el algoritmo desde la fila 0
n_reinas(tablero, 0, n)