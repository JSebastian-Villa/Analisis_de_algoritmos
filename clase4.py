"""
def palindromo(texto):
    texto_limpio = texto.replace("", "").lower
    invertido = texto_limpio

    return texto_limpio == invertido

"""

"""
def palindromo(texto):
    texto_limpio = texto.replace("","").lower()
    izq = 0
    der = len(texto_limpio) - 1

    while izq < der:
        if texto_limpio[izq] != texto_limpio[der]:
            return False
        izq += 1
        der -= 1
    
    return True


texto1 = "reconocer"
texto2 = "oso"
texto3 = "robar"
print(f"La palabra es palindromo: {palindromo(texto1)}")
print(f"La palabra es palindromo: {palindromo(texto2)}")
print(f"La palabra es palindromo: {palindromo(texto3)}")

"""
"""

def palindromo_recursivo(texto): #Complejidad n**2
    
    texto_limpio = texto.replace("","").lower()

    if len(texto_limpio) <= 1:
        return True
    
    if texto_limpio[0] != texto_limpio[-1]:
        return False
    
    return palindromo_recursivo(texto_limpio[1:-1])

palabra1 = "reconoCer"
palabra2 = "Ana"
palabra3 = "robar"
print(f"es palindromo : {palindromo_recursivo(palabra1)}")
print(f"es palindromo : {palindromo_recursivo(palabra2)}")
print(f"es palindromo : {palindromo_recursivo(palabra3)}")

"""
"""
def palindromo_mejorado(texto):      #Mas optimizado  
    texto_limpio = texto.replace("","").lower()
    
    def verificar_mejorado(izq, der):
        if izq >= der:
            return True
        if texto_limpio[izq] != texto_limpio[der]:
            return False
        return verificar_mejorado(izq + 1, der - 1)

    return verificar_mejorado(0, len(texto_limpio) -1)

palabra1 = "reconoCer"
palabra2 = "Ana"
palabra3 = "robar"
print(f"es palindromo : {palindromo_mejorado(palabra1)}")
print(f"es palindromo : {palindromo_mejorado(palabra2)}")
print(f"es palindromo : {palindromo_mejorado(palabra3)}")

"""
from itertools import combinations

def usando_libreria(lista, objetivo):
    n = len(lista)

    for tamaño in range(0, n + 1):

        for subconjunto in combinations(lista, tamaño):
            if sum(subconjunto) == objetivo:
                return True, list(subconjunto)
    
    return False, None

print(usando_libreria([3,5,7], 12))