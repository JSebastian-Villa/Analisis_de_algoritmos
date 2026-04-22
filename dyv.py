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
print("======")
print("Clase 4/22/2026")

# Clase 4/22/2026

# Validar si una lista dada esta ordenada, returnando true o false
#Ejercicio 1
def esta_ordenado(arr, izq, der):

    if izq == der:
        return True
    
    medio = (izq + der) // 2

    izq_ordenado = esta_ordenado(arr, izq, medio)
    der_ordenado = esta_ordenado(arr, medio + 1, der)

    if izq_ordenado and der_ordenado and arr[medio] > arr[medio + 1]:
        return False

    return True

arr = [1, 2, 3, 4, 5]
print(esta_ordenado(arr, 0, len(arr) - 1))  

arr2 = [1, 3, 2, 4]
print(esta_ordenado(arr2, 0, len(arr2) - 1))  

#Ejercicio 2

#Me dan un arreglo y quiero revertirlo

def invertir(lista):
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]

    return invertir(derecha) + invertir(izquierda)


lista = [6, 3, 5, 4]
resultado = invertir(lista)

print("Lista original:", lista)
print("Lista invertida:", resultado)

print("version profe")


def revertir_arreglo(arr, izq= 0, der = None):
    if der is None:
        der = len(arr) - 1
    
    if izq >= der:
        return arr
    
    arr[izq], arr[der] = arr[der], arr[izq]

    return revertir_arreglo(arr, izq + 1, der - 1)

#Ejercicio 3 - me dan una palabra y decir si es palindromo o no

def es_palindromo(palabra, izq, der):
    if izq >= der:
        return True

    if palabra[izq] != palabra[der]:
        return False

    return es_palindromo(palabra, izq + 1, der - 1)


p1 = "reconocer"
p2 = "hola"

print(p1, ":", es_palindromo(p1, 0, len(p1) - 1))
print(p2, ":", es_palindromo(p2, 0, len(p2) - 1))


#Ejercicio 4 - me dan un arreglo ordenado, y me dan un numero, buscar cual es el piso, el piso es un numero del arreglo que sea menor o igual al que me dieron

