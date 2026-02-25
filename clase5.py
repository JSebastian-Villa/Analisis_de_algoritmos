# Solucion ejercicios del examen

# Ejercicio 1 - A

a = [8,2,15,4,20,1]

n = len(a)
elem1, elem2 = 0, 0
diferencia_menor = float('inf')

for i in range(n):
    for j in range(i + 1, n):
        diff = abs(a[1] - a[j])
        if diff < diferencia_menor:
            diferencia_menor = diff
            elem1 = a[i]
            elem2 = a[j]

#Mejorado

a_ordenado = sorted(a)
for i in range(0, n-1):
    diff = a_ordenado[i+1] - a_ordenado[i]
    if diff < diferencia_menor:
        diferencia_menor = diff
        elem1 = a_ordenado[i+1]
        elem2 = a_ordenado[i]


#Ejercicio 2 - B

a = [2,3,5,3,2]
n = len(a)

def encontrar_unico(a):
    for i in range(n):
        cont = 0
        for j in range(n):
            if a[i] == a[j]:
                cont += 1
        if cont == 1:
            return a[i]
    return None

# Mejorado

def encontrar_unico(a):
    conteo = {}
    for num in a:
        conteo[num] = conteo.get(num, 0) + 1

    for num, cantidad in conteo.items():
        if cantidad == 1:
            return num

def encontrar_unico(a):
    resultado = 0
    for num in a:
        resultado ^= num
    return resultado

#===========================

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def factorial_tail(n, acumulador=1):
    if n == 1:
        return acumulador
    return factorial_tail(n-1, acumulador * n)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_tail(n, actual = 0 , siguiente = 1):
    if n == 0:
        return actual 
    return fibonacci_tail(n-1, siguiente, actual + siguiente)

print(fibonacci_tail(996))