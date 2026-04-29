
def fibonacci_memo(n, memo = {}):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2)
    return memo[n]

print(fibonacci_memo(10))

print("========")
# Cuantas formas puedo subir n cantidad de escaleras, de a una escalera dos 

def formas(n, memo={}):
    if n in memo:
        return memo[n]
    
    if n == 0 or n == 1:
        return 1
    
    memo[n] = formas(n-1, memo) + formas(n-2, memo)
    return memo[n]

# Ejemplo
n = 740
print(formas(n)) 

print("========")

# Contar monedas

def contar_monedas(monedas, monto):
    if monto == 0:
        return 0
    if monto < 0:
        return float('inf')
    
    minimo = float('inf')

    for moneda in monedas:
        resultado = contar_monedas(monedas, monto-moneda)
        minimo = min(minimo, resultado + 1)
    
    return minimo

def contar_memo(monedas, monto, memo = {}):
    
    if monto in memo:
        return memo[monto]
    if monto < 0:
        return float('inf')
    
    minimo = float('inf')
    for moneda in monedas:
        resultado = contar_memo(monedas, monto - moneda, memo)
        minimo = min(minimo, resultado + 1)
    
    memo[monto] = minimo
    return memo[monto] 