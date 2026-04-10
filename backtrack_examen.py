def particiones_numero(n):
    resultado = []

    def backtracking(restante, particion_actual, maximo):
        if restante == 0:
            resultado.append(particion_actual[:])
            return

        for i in range(min(maximo, restante), 0, -1):
            particion_actual.append(i)
            backtracking(restante - i, particion_actual, i)
            particion_actual.pop()

    backtracking(n, [], n)
    return resultado

# Ejercicio 1
print("\n1. PARTICIONES DE UN NÚMERO")
print("-" * 40)

for n in [4, 5, 6]:
    resultado = particiones_numero(n)
    print(f"n = {n}")
    print(f"Resultado: {resultado}\n")


print("=========================================================")

def dados_suma(k, objetivo):
    resultado = []

    def backtracking(dados_restantes, suma_actual, combinacion_actual):
        if dados_restantes == 0:
            if suma_actual == objetivo:
                resultado.append(combinacion_actual[:])
            return

        for valor in range(1, 7):
            if suma_actual + valor > objetivo:
                continue

            if suma_actual + valor + (dados_restantes - 1) * 1 < objetivo:
                continue

            if suma_actual + valor + (dados_restantes - 1) * 6 > objetivo:
                continue

            
            combinacion_actual.append(valor)
            backtracking(dados_restantes - 1, suma_actual + valor, combinacion_actual)
            combinacion_actual.pop()

    backtracking(k, 0, [])
    return resultado

# Ejercicio 2
print("\n2. FORMAR NÚMERO CON DADOS")
print("-" * 40)

casos_ej2 = [
    (2, 7),
    (3, 5),
    (2, 12),
]

for k, objetivo in casos_ej2:
    resultado = dados_suma(k, objetivo)
    print(f"k = {k}, objetivo = {objetivo}")
    print(f"Resultado: {resultado}\n")

#===========================================

# EJERCICIO 1

# en el primero particiones_numero lo que hay que hacer es que con un numero n
# tenemos que buscar como los subconjuntos de enteros positivos que sumen n,
# entonces la funcion recibe n y luego definimos resultado como una lista vacia
# donde guardaremos las combinaciones.

# empezamos con la funcion de backtracking que recibe restante que es lo que falta
# para llegar a n, particion_actual que es la lista donde vamos guardando lo que llevamos
# y el maximo que en principio seria n pero luego este numero con las iteraciones va bajando.

# entonces el caso base del backtracking verifica si restante == 0,
# esto significa que ya llegamos al numero n y conseguimos una combinacion,
# entonces a resultado se le añade particion_actual como una copia
# y terminamos el llamado con return.

# ya luego para seguir explorando el ciclo usa el minimo entre maximo y restante
# porque no se puede pasar, si el restante es 2 no puede usar despues un 3,
# y si el maximo es 4 no puede usar valores mayores que 4,
# y el ciclo va de mayor a menor.

# a particion_actual se le añade el valor i del ciclo
# y llamamos recursivamente backtracking donde hacemos restante - i
# y vamos evaluando hasta llegar a 0.

# despues de esto se hace pop para no mezclar resultados
# y poder explorar otras combinaciones.

# ya luego backtracking(n, [], n) lo que hace es iniciar todo el proceso
# con n, la lista vacia y n como maximo.

#===========================================

# EJERCICIO 2

# en el ejercicio dados_suma la funcion recibe k que es el numero de dados
# y objetivo que es el valor al cual queremos llegar,
# resultado es una lista vacia donde se guardaran las combinaciones.

# luego tenemos la funcion de backtracking que recibe dados_restantes,
# suma_actual y combinacion_actual que es la lista de lo que llevamos.

# el caso base es cuando dados_restantes == 0,
# o sea ya no puedo usar mas dados,
# y si la suma_actual es igual al objetivo se agrega al resultado
# porque encontramos una solucion.

# luego usamos un ciclo que prueba valores del 1 al 6.

# la primera poda verifica si suma_actual + valor es mayor al objetivo,
# si es asi descartamos porque nos pasamos.

# la segunda poda verifica si suma_actual + valor + los valores minimos
# de los dados restantes no alcanza el objetivo,
# si pasa eso descartamos porque no se puede llegar.

# la tercera poda hace lo mismo pero con valores maximos,
# pero esta tiene un error porque puede descartar combinaciones validas,
# ya que no tiene en cuenta que se pueden usar valores menores.

# despues de las podas agregamos el valor a combinacion_actual,
# llamamos recursivamente backtracking con dados_restantes - 1,
# suma_actual + valor y la combinacion,
# y luego hacemos pop para deshacer y probar otras opciones.

# finalmente backtracking(k, 0, []) inicia todo el proceso
# con todos los dados, suma en 0 y sin combinaciones.

#===========================================

# PODAS

# ejercicio 1:
# se usa maximo para restringir que los valores sean menores o iguales al anterior,
# esto evita repetir combinaciones y mantiene el orden.

# ejercicio 2:
# poda 1: evita pasarse del objetivo
# poda 2: evita caminos donde no se puede alcanzar el objetivo ni con valores minimos
# poda 3: intenta usar valores maximos pero es incorrecta porque elimina soluciones validas

#===========================================

# COMPLEJIDAD

# ejercicio 1:
# complejidad exponencial, aproximadamente O(2^n)
# porque el numero de particiones crece rapidamente

# ejercicio 2:
# complejidad O(6^k)
# porque cada dado tiene 6 posibles valores y hay k dados