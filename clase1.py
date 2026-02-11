import time
import os

N = 8
tablero = [-1] * N
columnas = set()
diag1 = set()
diag2 = set()

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def dibujar_tablero():
    limpiar()
    for fila in range(N):
        for col in range(N):
            if tablero[fila] == col:
                print("♛", end=" ")
            else:
                print(".", end=" ")
        print()
    time.sleep(0.2)

def resolver(fila=0):
    if fila == N:
        dibujar_tablero()
        return True  # cambia a False si quieres todas las soluciones

    for col in range(N):
        if col in columnas or (fila - col) in diag1 or (fila + col) in diag2:
            continue

        tablero[fila] = col
        columnas.add(col)
        diag1.add(fila - col)
        diag2.add(fila + col)

        dibujar_tablero()

        if resolver(fila + 1):
            return True

        # backtrack
        tablero[fila] = -1
        columnas.remove(col)
        diag1.remove(fila - col)
        diag2.remove(fila + col)
        dibujar_tablero()

    return False


resolver()
print("\nSolución encontrada 👑")

#=====================================================================================

def funcion(n):
    print("Hola")
    if n == 1:
        print(n)
    for i in range(0,n): # Se ejecuta n veces porque empieza desde el 0
        print("Adios")

# Si hay un ciclo o varios y depende de al entrada significa que va a ser de complejidad lineal
# Si el ciclo no depende la entrada es constante 
# Cuando llegamos al limite seria el caso Big O, el peor caso de todos por ser probado
# Para saber cual es el caso Big O, lo unico que hago es eliminar nuestras constantes y evaluar en esas términos