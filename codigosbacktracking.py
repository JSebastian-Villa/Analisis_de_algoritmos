# Generar todas las cadenas binarias de longitud n 
# donde no haya 1s consecutivos.

#Ejemplo n = 3
# 001, 000, 010, 100, 101 


def generar_cadenas(n):
    resultado = []

    def backtrack(cadena_actual):
        # Caso base: si ya tiene longitud n
        if len(cadena_actual) == n:
            resultado.append(cadena_actual)
            return
        
        # Opción 1: agregar '0' (siempre permitido)
        backtrack(cadena_actual + '0')
        
        # Opción 2: agregar '1' (solo si el anterior no es '1')
        if len(cadena_actual) == 0 or cadena_actual[-1] != '1':
            backtrack(cadena_actual + '1')
    
    backtrack("")
    return resultado

#===================================================

# Ejemplo
print(generar_cadenas(3))  


# Generar todas las cadenas con 'a' y 'b' de longitud n 
# donde no haya mas de 2 consecutivos.

# si por ejemplo n = 3. (aab, aba, abb, baa)

def generar_cadenas(n):
    resultado = []  # Lista donde guardamos las soluciones

    def backtrack(cadena_actual):
        # CASO BASE:
        # Si ya alcanzamos longitud n, guardamos la cadena
        if len(cadena_actual) == n:
            resultado.append(cadena_actual)
            return
        
        # OPCIÓN 1: agregar 'a'
        # Solo podemos agregar 'a' si no forma "aaa"
        if len(cadena_actual) < 2 or not (
            cadena_actual[-1] == 'a' and cadena_actual[-2] == 'a'
        ):
            backtrack(cadena_actual + 'a')
        
        # OPCIÓN 2: agregar 'b'
        # Solo podemos agregar 'b' si no forma "bbb"
        if len(cadena_actual) < 2 or not (
            cadena_actual[-1] == 'b' and cadena_actual[-2] == 'b'
        ):
            backtrack(cadena_actual + 'b')

    # Iniciamos con cadena vacía
    backtrack("")

    return resultado


# Ejemplo
print(generar_cadenas(3))

#==============================================================


def resolver_laberinto(laberinto):
    filas = len(laberinto)
    columnas = len(laberinto[0])
    
    # Movimientos posibles: abajo, arriba, derecha, izquierda
    movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    visitado = set()  # Para no repetir posiciones
    camino = []       # Para guardar el camino actual

    def backtrack(fila, col):
        # ❌ Fuera de límites
        if fila < 0 or fila >= filas or col < 0 or col >= columnas:
            return False
        
        # ❌ Es una pared o ya visitado
        if laberinto[fila][col] == 1 or (fila, col) in visitado:
            return False
        
        # Agregamos la posición al camino
        camino.append((fila, col))
        visitado.add((fila, col))
        
        # ✅ Caso base: llegamos al destino
        if fila == filas - 1 and col == columnas - 1:
            return True
        
        # Exploramos las 4 direcciones
        for df, dc in movimientos:
            if backtrack(fila + df, col + dc):
                return True
        
        # 🔙 Backtracking: deshacemos el movimiento
        camino.pop()
        visitado.remove((fila, col))
        
        return False

    # Ejecutamos desde (0,0)
    if backtrack(0, 0):
        return camino
    else:
        return None


# Ejemplo
laberinto = [
    [0, 0, 1],
    [1, 0, 0],
    [1, 1, 0]
]

print(resolver_laberinto(laberinto))

#===========================================

# --- FUERZA BRUTA: Usar bits para generar todas las combinaciones ---
def subconjuntos_fuerza_bruta(nums):
    """
    Genera subconjuntos usando máscara de bits.
    Para cada número del 0 al 2ⁿ-1, los bits indican qué elementos incluir.
    """
    n = len(nums)                      # guarda la cantidad de elementos del arreglo
    resultado = []                     # lista donde se almacenan todos los subconjuntos

    for mascara in range(2 ** n):      # recorre desde 0 hasta 2^n - 1 (todas las combinaciones posibles)
        subconjunto = []               # crea un subconjunto vacío para esta máscara

        for i in range(n):             # recorre cada posición del arreglo original
            if mascara & (1 << i):     # verifica si el bit i está encendido en la máscara
                subconjunto.append(nums[i])  # si está encendido, incluye ese elemento

        resultado.append(subconjunto)  # guarda el subconjunto generado

    return resultado                  # retorna todos los subconjuntos


# --- BACKTRACKING ---
def subconjuntos(nums):
    """
    Genera todos los subconjuntos usando backtracking.

    El parámetro 'inicio' evita generar duplicados como [1,2] y [2,1].
    Cada nodo del árbol de recursión es un subconjunto válido.
    """
    resultado = []                    # lista donde se almacenan los subconjuntos

    def backtrack(inicio, actual):    # función recursiva
        resultado.append(actual[:])   # guarda una copia del subconjunto actual

        for i in range(inicio, len(nums)):  # recorre desde 'inicio' hasta el final
            actual.append(nums[i])          # elegir: agrega el elemento actual
            backtrack(i + 1, actual)        # explorar: sigue construyendo el subconjunto
            actual.pop()                   # deshacer: elimina el último elemento agregado

    backtrack(0, [])                 # inicia desde índice 0 con subconjunto vacío
    return resultado                # retorna todos los subconjuntos

  # Complejidad de tiempo: O(2^n × n)
    # - Hay 2^n subconjuntos posibles
    # - Cada subconjunto se copia en O(n)

    # Complejidad de espacio: O(2^n × n)
    # - Se almacenan todos los subconjuntos (hasta 2^n)
    # - Cada uno puede tener tamaño hasta n


#=================================================

# --- FUERZA BRUTA: Usar itertools ---
from itertools import permutations as itertools_permutations  # importa función que genera permutaciones automáticamente

def permutaciones_fuerza_bruta(nums):
    """Genera permutaciones usando itertools (referencia)."""
    return [list(p) for p in itertools_permutations(nums)]  
    # genera todas las permutaciones como tuplas y las convierte a listas


# --- BACKTRACKING ---
def permutaciones(nums):
    """
    Genera todas las permutaciones usando backtracking.

    Diferencia con subconjuntos:
    - Subconjuntos: el orden NO importa → usar 'inicio' para avanzar
    - Permutaciones: el orden SÍ importa → verificar 'not in actual'
    """
    resultado = []                          # lista donde se guardan todas las permutaciones

    def backtrack(actual):                  # función recursiva que construye una permutación
        if len(actual) == len(nums):        # caso base: ya tenemos una permutación completa
            resultado.append(actual[:])     # guardar copia de la permutación actual
            return                         # detener esta rama

        for num in nums:                    # intentar usar cada número
            if num not in actual:           # poda: evitar repetir elementos en la misma permutación
                actual.append(num)          # elegir: agregar número
                backtrack(actual)           # explorar: seguir construyendo
                actual.pop()                # deshacer: quitar el último número

    backtrack([])                           # iniciar con lista vacía
    return resultado                        # retornar todas las permutaciones

# Complejidad de tiempo: O(n! × n)
    # - Hay n! permutaciones posibles
    # - Cada una se copia en O(n)

    # Complejidad de espacio: O(n! × n)
    # - Se almacenan todas las permutaciones
    # - Cada una tiene tamaño n

#=====================================

# --- FUERZA BRUTA: Probar TODAS las posiciones ---
from itertools import product   # importa función para generar combinaciones cartesianas

def n_reinas_fuerza_bruta(n):
    """
    Genera todas las combinaciones de columnas (nⁿ) y filtra las válidas.
    Extremadamente lento para n > 8.
    """
    resultado = []                              # lista donde se guardan soluciones válidas

    for posiciones in product(range(n), repeat=n):  
        # genera todas las combinaciones posibles de columnas (n^n posibilidades)

        valida = True                           # bandera para saber si la combinación sirve

        for i in range(n):                      # recorre cada reina
            for j in range(i + 1, n):           # compara con las demás reinas
                # Misma columna o misma diagonal
                if posiciones[i] == posiciones[j] or \
                   abs(posiciones[i] - posiciones[j]) == abs(i - j):
                    valida = False              # conflicto detectado
                    break

            if not valida:                      # si ya no es válida
                break                           # salir del ciclo

        if valida:                              # si la configuración es válida
            resultado.append(list(posiciones))  # guardarla como solución

    return resultado                            # retorna todas las soluciones válidas


# --- BACKTRACKING ---
def n_reinas(n):
    """
    Resuelve el problema de las N-Reinas con backtracking.

    tablero[i] = columna donde está la reina de la fila i.
    La poda verifica columnas y diagonales ANTES de colocar.
    """
    resultado = []                              # lista de soluciones

    def es_valida(tablero, fila, col):
        # verifica si se puede colocar una reina en (fila, col)

        for f in range(fila):                   # revisa todas las filas anteriores
            # Misma columna o misma diagonal
            if tablero[f] == col or \
               abs(tablero[f] - col) == abs(f - fila):
                return False                    # conflicto → no se puede colocar

        return True                             # posición válida


    def backtrack(tablero, fila):
        # tablero = lista de columnas donde están las reinas
        # fila = fila actual donde queremos colocar una reina

        if fila == n:                           # caso base: ya colocamos todas las reinas
            resultado.append(tablero[:])        # guardar solución
            return

        for col in range(n):                    # probar cada columna en esta fila
            if es_valida(tablero, fila, col):   # poda: solo posiciones válidas
                tablero.append(col)             # elegir: colocar reina
                backtrack(tablero, fila + 1)    # explorar: siguiente fila
                tablero.pop()                   # deshacer: quitar reina

    backtrack([], 0)                            # iniciar con tablero vacío
    return resultado                            # retornar soluciones

def imprimir_tablero(solucion):
    """Imprime un tablero de N-Reinas de forma visual."""

    n = len(solucion)                 # obtiene el tamaño del tablero (n x n)

    for fila in range(n):             # recorre cada fila del tablero
        linea = ""                    # inicializa una cadena vacía para construir la fila

        for col in range(n):          # recorre cada columna de la fila actual
            # si la reina está en esta columna → imprimir "Q"
            # si no → imprimir "."
            linea += " Q" if solucion[fila] == col else " ."

        print(f"    {linea}")         # imprime la fila con formato

# Complejidad de tiempo:
# - Fuerza bruta: O(n^n)
#   (se prueban todas las combinaciones posibles sin restricciones)

# - Backtracking: O(n!)
#   (la poda evita explorar muchas configuraciones inválidas)

# Complejidad de espacio: O(n)
# - Profundidad de la recursión = n (una reina por fila)
# - El tablero guarda hasta n posiciones

#====================================================

# --- FUERZA BRUTA: Generar todos los subconjuntos y filtrar ---
def suma_subconjuntos_fuerza_bruta(nums, objetivo):
    """Genera todos los 2ⁿ subconjuntos y filtra los que suman el objetivo."""

    n = len(nums)                      # cantidad de elementos
    resultado = []                     # lista de subconjuntos válidos

    for mascara in range(2 ** n):      # recorre todos los 2^n subconjuntos posibles
        subconjunto = []               # subconjunto actual

        for i in range(n):             # revisa cada bit
            if mascara & (1 << i):     # si el bit está encendido
                subconjunto.append(nums[i])  # agrega el elemento

        if sum(subconjunto) == objetivo:  # si la suma coincide con el objetivo
            resultado.append(subconjunto) # guardar solución

    return resultado                  # retornar resultados


# --- BACKTRACKING con poda ---
def suma_subconjuntos(nums, objetivo):
    """
    Encuentra subconjuntos que sumen el objetivo usando backtracking.

    Poda clave: si ordenamos los números, podemos hacer break
    cuando la suma parcial ya excede el objetivo.
    """
    resultado = []                     # lista de soluciones
    nums.sort()                        # ordenar para poder aplicar poda

    def backtrack(inicio, actual, suma):
        # inicio → desde dónde seguir
        # actual → subconjunto actual
        # suma → suma actual del subconjunto

        if suma == objetivo:           # caso base: encontramos solución
            resultado.append(actual[:])  # guardar copia
            return                    # no seguir explorando esta rama

        for i in range(inicio, len(nums)):  # recorrer candidatos
            if suma + nums[i] > objetivo:   # poda: si ya nos pasamos
                break                       # cortar el ciclo (gracias al orden)

            actual.append(nums[i])          # elegir
            backtrack(i + 1, actual, suma + nums[i])  # explorar
            actual.pop()                    # deshacer

    backtrack(0, [], 0)              # iniciar con subconjunto vacío y suma 0
    return resultado                 # retornar soluciones


# Complejidad de tiempo:
# - Fuerza bruta: O(2^n)
#   (se generan todos los subconjuntos y se filtran)

# - Backtracking: O(2^n) en el peor caso
#   (pero en la práctica es mucho menor gracias a la poda)

# Complejidad de espacio: O(n)
# - Profundidad de la recursión es n
# - El subconjunto actual puede tener hasta n elementos

#==========================================================

def resolver_sudoku(tablero):
    """
    Resuelve un Sudoku usando backtracking.
    Las celdas vacías se representan con 0.
    Modifica el tablero in-place y retorna True si tiene solución.
    """

    def encontrar_vacia(tablero):
        # busca la primera celda vacía (valor 0)
        for i in range(9):                    # recorre filas
            for j in range(9):                # recorre columnas
                if tablero[i][j] == 0:        # si encuentra un 0
                    return (i, j)             # retorna posición (fila, columna)
        return None                           # si no hay vacías → tablero completo

    def es_valido(tablero, fila, col, num):
        # verifica si se puede colocar 'num' en (fila, col)

        # Verificar fila
        if num in tablero[fila]:              # si el número ya está en la fila
            return False                     # no es válido

        # Verificar columna
        for i in range(9):                   # recorre toda la columna
            if tablero[i][col] == num:       # si ya está el número
                return False                # no es válido

        # Verificar caja 3×3
        box_fila = (fila // 3) * 3           # calcula inicio de la subcuadrícula
        box_col = (col // 3) * 3

        for i in range(box_fila, box_fila + 3):   # recorre filas de la caja
            for j in range(box_col, box_col + 3): # recorre columnas de la caja
                if tablero[i][j] == num:          # si ya existe el número
                    return False                 # no es válido

        return True                             # pasa todas las validaciones

    vacia = encontrar_vacia(tablero)            # busca celda vacía

    if not vacia:                              # si no hay vacías
        return True                            # sudoku resuelto

    fila, col = vacia                          # obtiene posición vacía

    for num in range(1, 10):                   # probar números del 1 al 9
        if es_valido(tablero, fila, col, num): # poda: solo números válidos
            tablero[fila][col] = num           # elegir: colocar número

            if resolver_sudoku(tablero):       # explorar: resolver recursivamente
                return True                   # si funciona, terminar

            tablero[fila][col] = 0             # deshacer: quitar número

    return False                               # ningún número funcionó → backtrack


def imprimir_sudoku(tablero):
    """Imprime un tablero de Sudoku formateado."""

    for i in range(9):                         # recorre filas
        if i % 3 == 0 and i != 0:              # cada 3 filas (excepto la primera)
            print("    ------+-------+------") # separador visual

        fila = ""                              # cadena para construir la fila

        for j in range(9):                     # recorre columnas
            if j % 3 == 0 and j != 0:          # cada 3 columnas
                fila += " | "                  # separador vertical

            # imprime número o punto si está vacío
            fila += f" {tablero[i][j]}" if tablero[i][j] != 0 else " ."

        print(f"    {fila}")                   # imprime la fila completa


# Complejidad de tiempo:
# - Sin poda: O(9^81)
#   (cada una de las 81 celdas puede tener hasta 9 opciones)

# - Con backtracking: mucho menor en la práctica
#   (solo se prueban valores válidos, se descartan muchas ramas)

# Complejidad de espacio: O(81) ≈ O(1)
# - profundidad máxima de recursión: 81 celdas
# - el tablero se modifica en el mismo espacio (in-place)