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

#========================================

"""
Enunciado

Dado un arreglo de números positivos y un valor objetivo T, encuentra todas las combinaciones de números cuya suma sea exactamente T.
Cada número puede usarse a lo sumo una vez.

Ejemplo:
nums = [2, 3, 5, 6, 8]
T = 10

Soluciones:

[2, 3, 5]
[2, 8]
"""
def combinaciones_suma(nums, T):
    resultado = []

    def backtrack(i, actual, suma):
        if suma == T:
            resultado.append(actual[:])
            return

        if suma > T:
            return

        if i == len(nums):
            return

        # Tomar nums[i]
        actual.append(nums[i])
        backtrack(i + 1, actual, suma + nums[i])
        actual.pop()

        # No tomar nums[i]
        backtrack(i + 1, actual, suma)

    backtrack(0, [], 0)
    return resultado

# ── Ejemplo 1: Combinaciones de suma ──
print("1. COMBINACIONES DE SUMA")
print("-" * 50)
nums = [2, 3, 5, 6, 8]
T = 10
print("Números:", nums)
print("Objetivo:", T)
print("Combinaciones que suman T:", combinaciones_suma(nums, T))

"""
Cómo justificar la poda en examen

Se poda cuando la suma parcial supera el objetivo, ya que todos los números son positivos y seguir agregando solo aumentaría más la suma.

🔥 Esa justificación está perfecta.
"""

# Complejidad de tiempo: O(2^n)
# - En cada posición del arreglo hay dos decisiones posibles:
#   1) Tomar el elemento actual
#   2) No tomarlo
# - Esto genera un árbol de decisiones binario con altura n
# - Por lo tanto, en el peor caso se exploran hasta 2^n combinaciones posibles
#
# - La poda (cuando suma > T) reduce el número de llamadas en la práctica,
#   pero no cambia la complejidad en el peor caso
# - Esto se debe a que podría darse un caso donde casi ninguna rama se poda
#
# - Además, cada vez que se encuentra una solución, se copia el arreglo actual,
#   lo cual cuesta O(n), pero el factor dominante sigue siendo 2^n
#
# 👉 Conclusión: la complejidad total es O(2^n)

#=============================================

"""
Enunciado

Dado un conjunto de empleados y turnos, y una disponibilidad por turno, genera todas las asignaciones válidas tales que:

Cada turno tenga exactamente un empleado
Ningún empleado trabaje en más de un turno
Ejemplo:
empleados = ["Ana", "Luis", "Carlos"]
turnos = ["Mañana", "Tarde"]

disponibilidad = {
    "Mañana": ["Ana", "Luis"],
    "Tarde": ["Luis", "Carlos"]
}
"""
def asignar_turnos(turnos, disponibilidad):
    resultado = []

    def backtrack(i, asignacion, usados):
        # Caso base
        if i == len(turnos):
            resultado.append(asignacion.copy())
            return

        turno = turnos[i]

        for empleado in disponibilidad[turno]:
            # Poda: no repetir empleado
            if empleado in usados:
                continue

            asignacion[turno] = empleado
            usados.add(empleado)

            backtrack(i + 1, asignacion, usados)

            usados.remove(empleado)
            del asignacion[turno]

    backtrack(0, {}, set())
    return resultado

turnos = ["Mañana", "Tarde"]
disponibilidad = {
    "Mañana": ["Ana", "Luis"],
    "Tarde": ["Luis", "Carlos"]
}

print(asignar_turnos(turnos, disponibilidad))
"""
O(m^n)
m = empleados posibles
n = cantidad de turnos
8. Justificación para examen

Se utiliza backtracking porque el problema consiste en construir una asignación válida turno por turno.
Se poda cuando un empleado ya ha sido asignado previamente, ya que no puede ocupar más de un turno.
"""

# Complejidad de tiempo: O(m^n)
# - n es la cantidad de turnos
# - m es el número máximo de empleados disponibles por turno
#
# - En cada turno (nivel del árbol), se puede elegir entre hasta m empleados
# - Esto genera un árbol de decisiones de altura n, con hasta m opciones por nivel
# - Por lo tanto, el número máximo de combinaciones exploradas es m^n
#
# - La poda (cuando un empleado ya fue usado) reduce el número de ramas,
#   ya que evita asignaciones inválidas
# - Sin embargo, en el peor caso (cuando todos los empleados están disponibles en todos los turnos),
#   el algoritmo sigue siendo exponencial
#
# - En cada solución válida se hace una copia del diccionario de asignación,
#   lo cual cuesta O(n), pero el factor dominante sigue siendo m^n
#
# 👉 Conclusión: la complejidad total es O(m^n)

#?============================


"""
EJERCICIO 2 — Formar grupos sin incompatibilidades
Enunciado

Tienes una lista de personas y una lista de pares incompatibles.
Debes formar un grupo de tamaño k sin incluir personas incompatibles entre sí.

Ejemplo:
personas = ["Ana", "Luis", "Carlos", "Sofia", "Marta"]
incompatibles = {("Ana", "Luis"), ("Carlos", "Sofia")}
k = 3
"""
def formar_grupos(personas, incompatibles, k):
    resultado = []

    def son_compatibles(grupo, persona):
        for p in grupo:
            if (p, persona) in incompatibles or (persona, p) in incompatibles:
                return False
        return True

    def backtrack(i, grupo):
        if len(grupo) == k:
            resultado.append(grupo[:])
            return

        if i == len(personas):
            return

        if len(grupo) + (len(personas) - i) < k:
            return

        if son_compatibles(grupo, personas[i]):
            grupo.append(personas[i])
            backtrack(i + 1, grupo)
            grupo.pop()

        backtrack(i + 1, grupo)

    backtrack(0, [])
    return resultado

# ── Ejemplo 2: Formar grupos sin incompatibilidades ──
print("\n2. FORMAR GRUPOS SIN INCOMPATIBILIDADES")                      
print("-" * 50)
personas = ["Ana", "Luis", "Carlos", "Sofia", "Marta"]
incompatibles = {("Ana", "Luis"), ("Carlos", "Sofia")}
k = 3
print("Personas:", personas)
print("Incompatibles:", incompatibles)
print("Grupos de tamaño k sin incompatibilidades:", formar_grupos(personas, incompatibles, k))

"""
Cómo justificar la poda

Se poda cuando el grupo parcial contiene una incompatibilidad, porque ya no puede convertirse en una solución válida.
También se poda cuando no quedan suficientes personas para completar el tamaño requerido del grupo.

💥 Esto es exactamente lo que suele preguntar un profe.
"""

# Complejidad de tiempo: O(C(n, k) * k)
# - n es la cantidad total de personas
# - k es el tamaño del grupo que queremos formar
#
# - El algoritmo genera combinaciones de tamaño k a partir de n personas
# - La cantidad de combinaciones posibles es:
#   C(n, k) = n! / (k! * (n-k)!)
#
# - Por cada combinación, se verifica si las personas son compatibles
# - La función son_compatibles revisa el grupo actual, lo cual cuesta O(k)
#
# - Por lo tanto, el costo total es:
#   O(C(n, k) * k)
#
# - Las podas reducen significativamente el número de combinaciones exploradas:
#   1) Se evita formar grupos con incompatibilidades
#   2) Se corta cuando no hay suficientes personas restantes para completar el grupo
#
# - Sin embargo, en el peor caso (sin incompatibilidades),
#   el algoritmo sigue generando todas las combinaciones posibles
#
# 👉 Conclusión: la complejidad es O(C(n, k) * k)

#=================================

"""
EJERCICIO 3 — Cadenas binarias sin dos 1 seguidos
Enunciado

Genera todas las cadenas binarias de longitud n que no tengan dos 1 consecutivos.

Ejemplo:

Para n = 3:

000
001
010
100
101
"""
def binarias_sin_unos_consecutivos(n):
    resultado = []

    def backtrack(cadena):
        if len(cadena) == n:
            resultado.append("".join(cadena))
            return

        cadena.append("0")
        backtrack(cadena)
        cadena.pop()

        if not cadena or cadena[-1] != "1":
            cadena.append("1")
            backtrack(cadena)
            cadena.pop()

    backtrack([])
    return resultado

# ── Ejemplo 3: Cadenas binarias sin dos 1 seguidos ──
print("\n3. CADENAS BINARIAS SIN DOS 1 SEGUIDOS")
print("-" * 50)
n = 5
print(f"Cadenas binarias de longitud {n} sin dos 1 seguidos:")
print(binarias_sin_unos_consecutivos(n))

"""
Cómo justificar la poda

Se poda cuando la cadena parcial termina en 1 y se intenta agregar otro 1, ya que esto violaría la restricción del problema.

Muy limpia.
"""

# Complejidad de tiempo: O(2^n)
# - En cada posición de la cadena hay dos decisiones posibles:
#   1) Agregar '0'
#   2) Agregar '1'
#
# - Esto genera un árbol de decisiones binario de altura n
# - En el peor caso, el número de nodos explorados es del orden de 2^n
#
# - Sin embargo, existe poda:
#   - No se permite agregar '1' si el último elemento ya es '1'
#   - Esto reduce el número de combinaciones generadas
#
# - De hecho, la cantidad real de soluciones sigue la sucesión de Fibonacci:
#   - f(n) = f(n-1) + f(n-2)
#   - Esto crece aproximadamente como O(φ^n), donde φ ≈ 1.618
#
# - Aun así, para análisis de peor caso en backtracking,
#   se considera la cota superior O(2^n)
#
# - Además, cada cadena generada se construye en O(n)
#   por el join, pero el factor dominante sigue siendo exponencial
#
# 👉 Conclusión: O(2^n) en peor caso (más preciso: O(φ^n))

#================================

"""
EJERCICIO 4 — Selección de tareas con tiempo límite
Enunciado

Tienes varias tareas, cada una con una duración.
Encuentra todas las formas de seleccionar tareas de modo que el tiempo total no supere un límite L.

Ejemplo:
tareas = [2, 4, 5, 3]
L = 7
"""
def seleccionar_tareas(tareas, L):
    resultado = []

    def backtrack(i, actual, tiempo):
        if tiempo > L:
            return

        if i == len(tareas):
            resultado.append(actual[:])
            return

        actual.append(tareas[i])
        backtrack(i + 1, actual, tiempo + tareas[i])
        actual.pop()

        backtrack(i + 1, actual, tiempo)

    backtrack(0, [], 0)
    return resultado

# ── Ejemplo 4: Selección de tareas con tiempo límite ──    
print("\n4. SELECCIÓN DE TAREAS CON TIEMPO LÍMITE")
print("-" * 50)
tareas = [2, 4, 5, 3]
L = 7
print("Tareas:", tareas)
print("Límite de tiempo:", L)
print("Combinaciones de tareas que no superan el límite:", seleccionar_tareas(tareas, L))

"""
Justificación de poda

Se poda cuando el tiempo acumulado supera el límite permitido, ya que agregar más tareas solo incrementaría el tiempo total.
"""

# Complejidad de tiempo: O(2^n)
# - n es la cantidad de tareas
#
# - En cada tarea hay dos decisiones:
#   1) Incluir la tarea
#   2) No incluir la tarea
#
# - Esto genera un árbol de decisiones binario de altura n
# - En el peor caso, se exploran hasta 2^n combinaciones posibles
#
# - La poda ocurre cuando el tiempo acumulado supera L,
#   lo que evita seguir explorando esa rama
#
# - Sin embargo, en el peor caso (cuando L es grande y casi todas las combinaciones son válidas),
#   la poda casi no reduce el árbol
#
# - Cada subconjunto válido se copia en O(n),
#   pero el factor dominante sigue siendo la cantidad de combinaciones
#
# 👉 Conclusión: la complejidad es O(2^n)

#====================================

"""
Enunciado

Dadas letras distintas, genera todas las palabras de longitud k sin repetir letras.

Ejemplo:
letras = ["A", "B", "C", "D"]
k = 3
"""

def palabras(letras, k):
    resultado = []
    usadas = [False] * len(letras)

    def backtrack(actual):
        if len(actual) == k:
            resultado.append("".join(actual))
            return

        for i in range(len(letras)):
            if not usadas[i]:
                usadas[i] = True
                actual.append(letras[i])

                backtrack(actual)

                actual.pop()
                usadas[i] = False

    backtrack([])
    return resultado

# ── Ejemplo 1: Generar palabras sin repetir letras ──
print("1. GENERAR PALABRAS SIN REPETIR LETRAS")         
print("-" * 50)
letras = ["A", "B", "C", "D"]
k = 3
print("Letras:", letras)
print("Palabras de longitud k sin repetir letras:", palabras(letras, k))

"""
Justificación de poda

Se evita explorar ramas donde una letra ya fue utilizada, porque el problema exige que no haya repeticiones.
"""

# Complejidad de tiempo: O(P(n, k)) = O(n! / (n-k)!)
# - n es la cantidad de letras disponibles
# - k es la longitud de cada palabra
#
# - El algoritmo genera todas las formas de elegir k letras sin repetir y con orden
# - Esto corresponde a las permutaciones de n elementos tomados de k en k:
#   P(n, k) = n! / (n-k)!
#
# - En el primer nivel hay n opciones, luego n-1, luego n-2, ..., hasta k niveles
# - Por lo tanto, el número total de combinaciones es:
#   n * (n-1) * (n-2) * ... * (n-k+1)
#
# - Cada palabra generada se construye en O(k) (por el join)
# - Pero el factor dominante es la cantidad de permutaciones
#
# 👉 Conclusión: la complejidad es O(n! / (n-k)!)

#========================================

"""
Enunciado

Dado un arreglo de enteros positivos, encuentra todos los subconjuntos de tamaño k cuya suma sea impar.

Ejemplo:
nums = [1, 2, 3, 4]
k = 2

Soluciones:

[1, 2]
[1, 4]
[2, 3]
[3, 4]
"""
def subconjuntos_impares(nums, k):
    resultado = []

    def backtrack(i, actual, suma):
        if len(actual) == k:
            if suma % 2 == 1:
                resultado.append(actual[:])
            return

        if i == len(nums):
            return

        if len(actual) + (len(nums) - i) < k:
            return

        actual.append(nums[i])
        backtrack(i + 1, actual, suma + nums[i])
        actual.pop()

        backtrack(i + 1, actual, suma)

    backtrack(0, [], 0)
    return resultado
# Ejemplo de uso
nums = [1, 2, 3, 4]
k = 2
print(subconjuntos_impares(nums, k))
# Salida:
# [[1, 2], [1, 4], [2, 3], [3, 4]]  

# Complejidad de tiempo: O(C(n, k) * k)
# - n es la cantidad de elementos en el arreglo
# - k es el tamaño del subconjunto que queremos formar
#
# - El algoritmo genera combinaciones de tamaño k a partir de n elementos
# - La cantidad de combinaciones posibles es:
#   C(n, k) = n! / (k! * (n-k)!)
#
# - Por cada subconjunto generado, se verifica si la suma es impar
# - Esta verificación es O(1) porque ya llevamos la suma acumulada
#
# - Sin embargo, al guardar el subconjunto se hace una copia,
#   lo cual cuesta O(k)
#
# - La poda:
#   if len(actual) + (len(nums) - i) < k
#   evita explorar ramas donde no es posible completar k elementos,
#   reduciendo el número de llamadas recursivas
#
# - Aun así, en el peor caso se generan todas las combinaciones posibles
#
# 👉 Conclusión: la complejidad total es O(C(n, k) * k)

#===========================================

"""
EJERCICIO 1 — Equipos de tamaño k con puntaje exacto
⭐ MUY TIPO EXAMEN
Enunciado

Tienes una lista de jugadores con puntajes.
Debes formar todos los equipos de tamaño k cuya suma de puntajes sea exactamente T.

Ejemplo:
jugadores = [("Ana", 3), ("Luis", 5), ("Carlos", 2), ("Marta", 4)]
k = 2
T = 7
Salida esperada:
[["Ana", "Marta"], ["Luis", "Carlos"]]
1. ¿Por qué esto es backtracking?

Porque:

estás eligiendo jugadores
construyes el equipo paso a paso
cada jugador se toma o no se toma
si ya te pasaste del puntaje o ya no puedes completar el equipo, podas

👉 Este es el modelo clásico de subconjuntos / combinaciones.
"""
def equipos_puntaje(jugadores, k, T):
    resultado = []

    def backtrack(i, equipo, suma_actual):
        # Caso base: si ya tengo k jugadores
        if len(equipo) == k:
            if suma_actual == T:
                resultado.append(equipo[:])
            return

        # Si ya recorrí todos los jugadores
        if i == len(jugadores):
            return

        # Poda 1: si la suma ya se pasó
        if suma_actual > T:
            return

        # Poda 2: si ya no alcanza para completar k
        if len(equipo) + (len(jugadores) - i) < k:
            return

        nombre, puntaje = jugadores[i]

        # Opción 1: tomar al jugador actual
        equipo.append(nombre)
        backtrack(i + 1, equipo, suma_actual + puntaje)
        equipo.pop()

        # Opción 2: no tomar al jugador actual
        backtrack(i + 1, equipo, suma_actual)

    backtrack(0, [], 0)
    return resultado
# Ejemplo de uso
jugadores = [("Ana", 3), ("Luis", 5), ("Carlos", 2), ("Marta", 4)]
k = 2
T = 7
print(equipos_puntaje(jugadores, k, T))
# Salida esperada:          
# [["Ana", "Marta"], ["Luis", "Carlos"]]

"""
Se utiliza backtracking porque el problema consiste en construir equipos válidos de manera incremental,
explorando las decisiones de incluir o no incluir cada jugador.
Se poda una rama cuando la suma parcial supera el objetivo o cuando
ya no quedan suficientes jugadores para completar un equipo de tamaño k
.
complejidad:    O(2^n) 
Porque para cada jugador decides:
tomarlo
no tomarlo
"""
# Complejidad de tiempo: O(C(n, k) * k)
# - n es la cantidad de jugadores
# - k es el tamaño del equipo
#
# - El algoritmo genera combinaciones de tamaño k a partir de n jugadores
# - La cantidad de combinaciones posibles es:
#   C(n, k) = n! / (k! * (n-k)!)
#
# - Aunque el árbol de decisiones es binario (tomar / no tomar),
#   las podas obligan a que solo se formen equipos de tamaño k
#   → esto reduce el espacio de búsqueda a combinaciones
#
# - Por cada equipo válido:
#   - Se verifica la suma (ya llevada acumulada → O(1))
#   - Se hace una copia del equipo → O(k)
#
# - Las podas ayudan bastante:
#   1) suma_actual > T → corta ramas inválidas
#   2) no alcanzan jugadores → evita exploraciones inútiles
#
# - Aun así, en el peor caso (cuando muchas combinaciones cumplen),
#   se generan todas las combinaciones de tamaño k
#
# 👉 Conclusión: O(C(n, k) * k)

#================================================

"""
Una empresa genera códigos con las letras:

["A", "B", "C"]

Debes generar todos los códigos de longitud n tales que:

No haya dos letras iguales consecutivas
El código contenga al menos una vez la letra "B"
Ejemplo:
n = 3
"""
def generar_codigos(n):
    letras = ["A", "B", "C"]
    resultado = []

    def backtrack(actual, tiene_b):
        # Caso base
        if len(actual) == n:
            if tiene_b:
                resultado.append("".join(actual))
            return

        for letra in letras:
            # Poda: no repetir consecutivamente
            if actual and actual[-1] == letra:
                continue

            actual.append(letra)
            backtrack(actual, tiene_b or letra == "B")
            actual.pop()

    backtrack([], False)
    return resultado

# Ejemplo de uso
n = 3
print(generar_codigos(n))
# Salida:
# ['ABA', 'ABC', 'ACA', 'ACB', 'BAA', ' BAC', 'BCA', 'BCB', 'CAB', 'CBC']       
"""
8. Justificación para examen

Se aplica backtracking porque el código se construye carácter por carácter, evaluando en cada paso qué letra puede agregarse.
Se poda cuando una letra es igual a la anterior, ya que eso violaría la restricción del problema.
complejidad:
O(3^n) Cada posición tiene hasta 3 opciones: A, B o C, pero debido a la poda, el número real de combinaciones es menor.
"""

# Complejidad de tiempo: O(3^n)
# - n es la longitud del código
#
# - En cada posición hay hasta 3 opciones posibles: A, B o C
# - Esto genera un árbol de decisiones de altura n con un máximo de 3 ramas por nivel
# - Por lo tanto, en el peor caso se exploran hasta 3^n combinaciones
#
# - Sin embargo, existe poda:
#   - No se permite repetir la misma letra consecutivamente
#   - Esto reduce las opciones a lo sumo 2 por nivel después del primero
#
# - Por eso, el número real de combinaciones es menor,
#   aproximadamente del orden de 3 * 2^(n-1)
#
# - Además, se lleva un control con 'tiene_b' para verificar si aparece la letra B,
#   pero esto no afecta el número de ramas exploradas, solo filtra al final
#
# - Cada código válido se construye en O(n) (por el join),
#   pero el factor dominante sigue siendo exponencial
#
# 👉 Conclusión:
# - Cota superior: O(3^n)
# - Más preciso: O(2^n)

#====================================

"""
Enunciado

Dada una lista de materias y una lista de pares incompatibles por cruce de horario, genera todas las selecciones de tamaño k tales que ninguna materia sea incompatible con otra.

Ejemplo:
materias = ["MAT", "FIS", "PROG", "BD", "REDES"]
incompatibles = {("MAT", "FIS"), ("PROG", "BD")}
k = 3
"""
def materias_compatibles(materias, incompatibles, k):
    resultado = []

    def es_compatible(actual, materia):
        for m in actual:
            if (m, materia) in incompatibles or (materia, m) in incompatibles:
                return False
        return True

    def backtrack(i, actual):
        # Caso base válido
        if len(actual) == k:
            resultado.append(actual[:])
            return

        # Si se acabaron las materias
        if i == len(materias):
            return

        # Poda: ya no alcanza
        if len(actual) + (len(materias) - i) < k:
            return

        # Opción 1: tomar materia si es compatible
        if es_compatible(actual, materias[i]):
            actual.append(materias[i])
            backtrack(i + 1, actual)
            actual.pop()

        # Opción 2: no tomarla
        backtrack(i + 1, actual)

    backtrack(0, [])
    return resultado

materias = ["MAT", "FIS", "PROG", "BD", "REDES"]
incompatibles = {("MAT", "FIS"), ("PROG", "BD")}

print(materias_compatibles(materias, incompatibles, 3))
"""
complejidad: O(2^n) en el peor caso, ya que cada materia puede ser tomada o no, pero la poda reduce significativamente 
el número de combinaciones a evaluar.
8. Justificación de poda

Se poda una rama cuando la materia actual es incompatible con alguna materia ya seleccionada, porque esa selección parcial no puede convertirse en una solución válida.
También se poda cuando ya no quedan suficientes materias para completar una selección de tamaño k.

💥 Muy buena explicación de parcial.
"""

# Complejidad de tiempo: O(C(n, k) * k)
# - n es la cantidad de materias
# - k es el tamaño de la selección
#
# - Aunque el algoritmo toma decisiones binarias (tomar o no tomar),
#   las restricciones hacen que solo se generen combinaciones de tamaño k
#
# - Por lo tanto, el número de posibles soluciones es:
#   C(n, k) = n! / (k! * (n-k)!)
#
# - En cada paso, al intentar agregar una materia,
#   se verifica si es compatible con las ya seleccionadas
#
# - La función es_compatible recorre el grupo actual,
#   lo cual cuesta O(k) en el peor caso
#
# - Entonces, por cada combinación evaluada hay un costo adicional O(k)
#
# - Las podas reducen el árbol:
#   1) incompatibilidad → evita combinaciones inválidas
#   2) no alcanzan materias → evita ramas inútiles
#
# - Sin embargo, en el peor caso (sin incompatibilidades),
#   se generan todas las combinaciones posibles
#
# 👉 Conclusión: la complejidad es O(C(n, k) * k)

#==========================================

"""
1) Cómo reconocer un problema de Backtracking en 10 segundos

Si el problema tiene estas características, casi seguro es backtracking:

Señales claras:
Hay que probar posibilidades.
La solución se construye paso a paso.
En cada paso hay varias opciones.
Algunas decisiones pueden hacer que la solución sea inválida.
Quieren:
todas las soluciones,
una solución válida,
o la mejor solución entre muchas.
Frase mental:

“Voy armando una solución parcial, y si veo que ya no sirve, me devuelvo.”

Eso es backtracking.
2) formato general de un algoritmo de Backtracking
def backtrack(estado_actual):
    if caso_base:
        guardar_respuesta()
        return

    for opcion in opciones_posibles:
        if es_valida(opcion):
            hacer(opcion)
            backtrack(nuevo_estado)
            deshacer(opcion)
3) Lo MÁS importante del examen: ¿cómo encontrar la PODA?

Esta es la parte clave.

Regla de oro:

La poda aparece cuando puedes decir:

“Aunque siga explorando por aquí, ya sé que esto no puede terminar bien”.

Entonces cortas esa rama.

4) Tipos de poda que más salen en examen
PODA TIPO 1: Restricción violada

La más fácil y más común.

Idea:

Si la solución parcial ya incumple una regla, no tiene sentido seguir.

Ejemplo:
“La suma no puede pasar de 10”
“No se pueden repetir números”
“No pueden ir dos personas incompatibles juntas”
“No puede haber dos letras iguales consecutivas”
Forma mental:

“Ya me pasé / ya rompí una regla / ya quedó inválido”.

✅ Se poda inmediatamente.

PODA TIPO 2: Ya no alcanza para completar

Muy típica y muy buena.

Idea:

Aunque sigas, ya no te quedan suficientes elementos para completar la solución.

Ejemplo:

“Debo escoger 4 elementos y llevo 2, pero solo me queda 1 disponible”.

Entonces:

necesito 2 más,
pero solo hay 1,
imposible terminar.
Condición típica:
if len(solucion_actual) + elementos_restantes < tamaño_objetivo:
    return
Forma mental:

“Ya no me da”.

PODA TIPO 3: Me pasé del objetivo

Muy común en problemas de suma, peso, costo, capacidad, etc.

Ejemplo:
suma objetivo = 15
llevas 18

Ya no sirve seguir si solo puedes agregar positivos.

Condición típica:
if suma_actual > objetivo:
    return
Forma mental:

“Ya me pasé, no hay forma de arreglarlo”.

⚠️ Ojo: esta poda solo sirve si no existen negativos o algo que pueda compensar.

PODA TIPO 4: No puede superar la mejor solución actual

Esto sale cuando el problema es de optimización:

máximo valor,
mínimo costo,
mejor combinación,
etc.
Idea:

Si ya tienes una mejor respuesta guardada, y esta rama ni en el mejor caso puede superarla, la cortas.

Ejemplo:

“Quiero el subconjunto de mayor suma sin pasarme de 20”.

Si una rama actual lleva suma 7, y aun usando todo lo que queda solo llegaría a 10, pero ya tienes una solución de 14…

❌ Esa rama ya no sirve.

Forma mental:

“Ni esforzándose esta rama gana”.

Esto ya es una poda más fuerte.

5) Cómo sacar la poda en un examen paso a paso

Cuando leas el enunciado, pregúntate esto:

Pregunta 1:
“¿Qué hace inválida una solución parcial?”

Eso te da la poda más obvia.

Ejemplos:

repetir elementos,
exceder una suma,
romper una regla de adyacencia,
usar más recursos de los permitidos.
Pregunta 2:
“¿Qué me falta para completar la solución?”

Eso te da la poda de “ya no alcanza”.

Ejemplos:

faltan k elementos,
faltan letras,
faltan grupos,
faltan posiciones.
Pregunta 3:
“¿Hay una meta numérica que pueda pasarme?”

Eso te da poda por exceso.

Ejemplos:

suma,
costo,
peso,
tiempo,
capacidad.
Pregunta 4:
“¿Estoy buscando la mejor solución?”

Eso te da poda por comparación con la mejor actual.

6) La plantilla mental que debes decir en el examen

Cuando te pidan explicar la poda, puedes escribir algo como esto:

Criterio de poda:
Se detiene la exploración de una rama cuando la solución parcial ya no puede conducir a una solución válida u óptima.
En este caso, se poda cuando ________, porque continuar explorando no produciría una respuesta útil.

Y luego lo adaptas:

“...cuando la suma parcial supera el objetivo”
“...cuando se repite un elemento”
“...cuando no quedan suficientes elementos para completar la solución”
“...cuando la rama actual no puede superar la mejor solución encontrada”

Eso queda muy bien explicado.

"""

#elegir una posible solucion
#explorar esa posible solucion
#deshacer: hacer poda

"""
8) El truco más importante: cómo saber si el for va sobre posiciones o sobre elementos

Esto también te lo pueden evaluar.

Caso A: elegir / no elegir elementos

Cuando el problema es tipo:

subconjuntos,
combinaciones,
grupos,
selección,

normalmente usas:

backtrack(i, ...)

Y en cada elemento decides:

lo tomo,
no lo tomo.

O también:

for j in range(i, len(nums)):
Caso B: llenar posiciones

Cuando el problema es tipo:

formar cadenas,
armar palabras,
llenar casillas,
asignar algo en orden,

normalmente haces:

for opcion in opciones:

Porque estás decidiendo qué poner en la siguiente posición.

9)Preguntas trampa de examen que tu profe puede hacer
Trampa 1:
“¿Esto no se puede hacer con fuerza bruta?”

Sí, pero backtracking = fuerza bruta inteligente.

La diferencia es que:

fuerza bruta prueba todo,
backtracking prueba y poda.

💥 Esa frase sirve mucho.

Trampa 2:
“¿Cuál es la diferencia entre recursión y backtracking?”

Muy importante:

Recursión = técnica de programación.
Backtracking = estrategia de búsqueda que usa recursión + deshacer decisiones + poda.

O sea:

No toda recursión es backtracking, pero casi todo backtracking usa recursión.

Trampa 3:
“¿Por qué haces pop()?”

Porque cuando vuelves de la llamada recursiva debes deshacer la decisión para probar otra opción.

Eso es el famoso:

hacer → explorar → deshacer

10) Mini plantilla que te salva cualquier ejercicio

Si mañana te ponen un ejercicio raro, usa esto:

PASO 1: ¿Qué estoy construyendo?
una lista,
una cadena,
un grupo,
un subconjunto,
una asignación.
PASO 2: ¿Qué representa el estado?
índice,
suma,
usados,
solución parcial,
contador.
PASO 3: ¿Cuál es el caso base?
ya completé tamaño,
llegué al final,
alcancé objetivo.
PASO 4: ¿Cuáles son las opciones?
tomar / no tomar,
elegir uno entre varios,
poner 0 o 1,
asignar un elemento.
PASO 5: ¿Dónde podo?

Busca:

restricción rota,
me pasé,
ya no alcanza,
ya está usado,
no supera la mejor.

"""