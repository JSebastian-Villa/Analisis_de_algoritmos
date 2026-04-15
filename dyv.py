def potencia(x, n):

    resultado = 1
    for _ in range(n):
        resultado *= x
    
    return resultado

print("=== Potencia Iterativa ===")
res1 = potencia(2, 5)
print(f"Resultado final: {res1}\n")


#Con divide y venceras

def potencia(x , n):
    if n == 0:
        return 1
    
    if n % 2 == 0:
        mitad = potencia(x, n//2)
        return mitad * mitad
    else:
        return x * potencia(x, n-1)

print("=== Potencia Iterativa ===")
res1 = potencia(2, 5)
print(f"Resultado final: {res1}\n")


#=====================================================================


def max_min(arr):
    maximo = minimo = arr[0]

    for valor in arr[1:]:
        if valor > maximo:
            maximo = valor
        if valor < minimo:
            minimo = valor
    return maximo, minimo

#=========

def max_min_dyv(arr, izq = 0, der = None):
    if der is None:
        der = len(arr) - 1
    
    if der - izq == 1:
        if arr[izq] < arr[der]:
            return arr[der], arr[izq]
        return arr[izq], arr[der]
    
    if izq == der:
        return arr[izq], arr[izq]
    
    medio = (izq + der) // 2

    max_izq, min_izq = max_min_dyv(arr, izq, medio)
    max_der, min_der = max_min_dyv(arr, medio + 1, der) 



def ordenamiento():
    