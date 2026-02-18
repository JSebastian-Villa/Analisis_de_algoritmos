#Ejercicio 1: Asesoría

#Buscar objetivo x en una matriz n*m
#Descripcion exacta del problema Dada una matriz de enteros de tamano n*m y un valor objetivo x, 
# determinar si x aparece en la matriz usando una busqueda lineal por filas.

matriz1 = [[3,5,2],[7,1,9],[4,6,8]]
matriz2 = [[10, 11], [12, 13]]
matriz3 = [[2], [4], [6]]
x = 1


def f1(matrix, x):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == x:
                return True
    return False


print(f"el valor de la x fue encontrado :{f1(matriz1,1)}")
print(f"el valor de la x fue encontrado :{f1(matriz2,9)}")
print(f"el valor de la x fue encontrado :{f1(matriz3,4)}")

#Ejercicio 2

#Descripcion exacta del problema Dado un arreglo de enteros, 
# ordenar los elementos en orden ascendente usando ciclos y explicar la complejidad O( N ).

def f2(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - i - 1 ):
            if lista[j] > lista[j + 1]:
                lista[j],lista[j+1] = lista[j + 1], lista[j]
    return lista
    


lista = [5,1,4,2,8]
print(f"la lista ordenada es: {f2(lista)}")


#Ejercicio 3 **Descripcion exacta del problema ** Dado un entero positivo  n , verificar si su representacion binaria tiene bits alternados, es decir,
#  si cada par de bits adyacentes es distinto. Se cumple  1<=n<=231−1 .

def f3():
    pass
