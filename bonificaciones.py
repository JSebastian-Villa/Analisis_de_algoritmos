
# Tenemos una lista de valores [100,50,300,220,10] (n valores) y voy a tener una variable objetivo, y ahi va a haber un valor, 
#y quiero saber si hay dos valores en la lista que sumados den ese valor objetivo.

def encontrar_pares(lista, objetivo):
    vistos = set()
    for valor in lista:
        if objetivo - valor in vistos:
            return True
        vistos.add(valor)
    return False


print("Ejemplos de prueba:")
lista = [100, 50, 300, 220, 10]
objetivo = 270
  
print(f"Lista: {lista }, objetivo: {objetivo} -> que son : {encontrar_pares(lista, objetivo)}")  
