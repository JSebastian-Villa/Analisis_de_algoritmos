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


#========================= 17/05/2026

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivote = arr[0]
    menores = [x for x in arr[1:] if x <= pivote]
    mayor = [x for x in arr[1:] if x > pivote]

    return quick_sort(menores) + [pivote] + quick_sort(mayor)


print(quick_sort([5, 10, 4, 1, 3, 7]))

#Dado un arreglo de números enteros (positivos y negativos), 
# encuentra la máxima suma posible de un subarreglo continuo usando Divide y Vencerás.

def max_subarreglo(arr, izq, der):  # función que calcula la suma máxima en el rango [izq, der]
    
    if izq == der:  # caso base: solo hay un elemento
        return arr[izq]  # la suma máxima es ese mismo elemento

    medio = (izq + der) // 2  # calculamos el punto medio para dividir el problema

    suma_izq = max_subarreglo(arr, izq, medio)  # resolvemos recursivamente la mitad izquierda
    suma_der = max_subarreglo(arr, medio + 1, der)  # resolvemos recursivamente la mitad derecha

    suma = 0  # acumulador para recorrer hacia la izquierda desde el medio
    max_izq_cruzando = float('-inf')  # guardará la mejor suma hacia la izquierda

    for i in range(medio, izq - 1, -1):  # recorremos desde el medio hacia la izquierda
        suma += arr[i]  # acumulamos la suma
        max_izq_cruzando = max(max_izq_cruzando, suma)  # guardamos la mejor suma encontrada

    suma = 0  # reiniciamos acumulador para recorrer hacia la derecha
    max_der_cruzando = float('-inf')  # guardará la mejor suma hacia la derecha

    for i in range(medio + 1, der + 1):  # recorremos desde el medio+1 hacia la derecha
        suma += arr[i]  # acumulamos la suma
        max_der_cruzando = max(max_der_cruzando, suma)  # guardamos la mejor suma encontrada

    suma_cruzada = max_izq_cruzando + max_der_cruzando  # suma total cruzando el medio

    return max(suma_izq, suma_der, suma_cruzada)  # devolvemos el máximo entre izquierda, derecha y cruzado

#Dado un arreglo, encuentra un elemento que sea mayor o igual que sus vecinos.

def encontrar_pico(arr, izq, der):  # función que busca un pico en el rango
    
    medio = (izq + der) // 2  # calculamos la posición del medio

    if (medio == 0 or arr[medio] >= arr[medio - 1]) and \
       (medio == len(arr) - 1 or arr[medio] >= arr[medio + 1]):  
        return arr[medio]  # si es mayor que sus vecinos (o está en borde), es un pico

    if medio > 0 and arr[medio - 1] > arr[medio]:  
        return encontrar_pico(arr, izq, medio - 1)  # si el vecino izquierdo es mayor, el pico está a la izquierda

    return encontrar_pico(arr, medio + 1, der)  # si no, el pico está a la derecha