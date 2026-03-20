
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

#=====


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