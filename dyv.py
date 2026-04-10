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
