import heapq


def solucion_min_paradas(distancia_total, capacidad, estaciones):
    estaciones = [0] + sorted(estaciones) + [distancia_total]
    paradas = []
    combustible = capacidad

    for i in range(1, len(estaciones)):
        distancia = estaciones[i] - estaciones[i-1]

        if distancia > capacidad:
            return -1 #Imposible
        
        if distancia > combustible: #Parar en la anterior
            paradas.append(estaciones[i-1])
            combustible = capacidad
        
        combustible -= distancia
    
    return paradas

# Reto 3
print("\n3. ESTACIONES DE GASOLINA")
paradas = solucion_min_paradas(25, 10, [5, 8, 15, 22])
print(f"   Distancia: 25, Tanque: 10km, Estaciones: [5, 8, 15, 22]")
print(f"   Paradas necesarias: {paradas}")

def max_peliculas(peliculas):

    peliculas_ordenadas = sorted(peliculas, key = lambda x: x[1])
    seleccionadas = []
    fin_actual = 0

    for inicio, fin in peliculas_ordenadas:
        if inicio >= fin_actual:
            seleccionadas.append((inicio, fin))
            fin_actual = fin
    
    return seleccionadas

print("\n1. MÁXIMO REUNIONES")
peliculas = [(13,15),(14,16),(15,17),(16,18),(17,19)]
print(f"   Reuniones: {peliculas}")
print(f"   Seleccionadas: {max_peliculas(peliculas)}")


#2 Camion con cajas, pero no se pueden repartir cajas

def llenar_camion(capacidad, cajas):
    
    cajas_con_ratio = [(p, v, v/p, i) for i, (p,v) in enumerate(cajas)]
    cajas_con_ratio.sort(key = lambda x: x[2], reverse = True)

    valor_total = 0
    seleccionadas = []

    for peso, valor, ratio, idx in cajas_con_ratio:
        if peso <= capacidad:
            seleccionadas.append((peso, valor))
            valor_total += valor
            capacidad -= peso
    
    return valor_total, seleccionadas

print("\n2. LLENAR CAMIÓN")
cajas = [(5, 10), (4, 40), (6, 30), (3, 50)]
valor, selec = llenar_camion(10, cajas)
print(f"   Cajas (peso, valor): {cajas}")
print(f"   Capacidad: 10")

def cargar_camion(capacidad, cajas):

    cajas_seleccionadas = [(p, v, i) for i,(p,v) in enumerate(cajas)]
    cajas_seleccionadas.sort(key = lambda x: x[1], reverse = True)

    valor_total = 0
    seleccionadas = []

    for peso, valor, idx in cajas_seleccionadas:
        if peso <= capacidad:
            seleccionadas.append((peso, valor))
            valor_total += valor
            capacidad -= peso
    
    return valor_total, seleccionadas

print("\n2. LLENAR CAMIÓN")

cajas = [(10,60),(20,100),(30,120)]
valor, selec = cargar_camion(50, cajas)

print(f"   Cajas (peso, valor): {cajas}")
print(f"   Capacidad: 50")
print(f"   Valor obtenido: {valor}, Cajas: {selec}")

# 4 Asignar tareas a servidores

def asignar_tareas(tareas, num_servidores):
    if not tareas:
        return 0, [[] for _ in range(num_servidores)]
    tareas_ordenadas = sorted(enumerate(tareas), key = lambda x: -x[1])

    servidores = [(0, i, [] ) for i in range(num_servidores)]
    heapq.heapify(servidores)

    for idx_original, tiempo in tareas_ordenadas:
        carga, id_servidor, lista = heapq.heappop(servidores)
        lista.append(tiempo)
        heapq.heappush(servidores, (carga + tiempo, id_servidor, lista))
    
    tiempo_total = max(s[0] for s in servidores)
    asignacion = [s[2] for s in sorted(servidores, key = lambda x: x[1])]

    return tiempo_total, asignacion
    
    
# Reto 4
print("\n4. ASIGNAR TAREAS")
tiempo, asig = asignar_tareas([2, 14, 4, 16, 6, 5], 3)
print(f"   Tareas: [2, 14, 4, 16, 6, 5], Servidores: 3")
print(f"   Tiempo total: {tiempo}")
print(f"   Asignación: {asig}")

"""
Una empresa de tecnología tiene una lista de n trabajos que pueden realizarse en un único procesador. Cada trabajo i está asociado a:

Un tiempo límite (deadline): el trabajo debe completarse antes o en ese tiempo (1 unidad de tiempo por trabajo).
Una ganancia (profit): si el trabajo se completa dentro de su plazo, se obtiene esta ganancia; si no, la ganancia es 0.
El procesador solo puede realizar un trabajo por unidad de tiempo, y cada trabajo dura exactamente 1 unidad.

👉 El objetivo es seleccionar y ordenar los trabajos de manera que la ganancia total sea máxima.

Ejemplo
Entrada: Trabajos = [(J1, deadline=2, profit=100), (J2, deadline=1, profit=19), (J3, deadline=2, profit=27), (J4, deadline=1, profit=25), (J5, deadline=3, profit=15)]

Salida: Secuencia = [J1, J3, J5], Ganancia = 142

Explicación:

J1 se programa en la unidad de tiempo 2.
J3 se programa en la unidad de tiempo 1.
J5 se programa en la unidad de tiempo 3. Ganancia total = 100 + 27 + 15 = 142.
"""

def job_scheduling(jobs):
    
    # Ordena los trabajos por ganancia (profit) de mayor a menor
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Encuentra el mayor deadline entre todos los trabajos
    max_deadline = max(job[1] for job in jobs)

    # Crea una lista de espacios de tiempo disponibles (slots)
    # Cada posición representa una unidad de tiempo
    # Se usa max_deadline + 1 porque no se usa la posición 0
    slots = [None] * (max_deadline + 1)

    # Variable para almacenar la ganancia total
    total_profit = 0

    # Lista para guardar los trabajos seleccionados
    seleccionados = []

    # Recorre cada trabajo en la lista ordenada
    for job in jobs:

        # Descompone la tupla del trabajo en nombre, deadline y profit
        name, deadline, profit = job

        # Intenta ubicar el trabajo en el último espacio disponible antes de su deadline
        # Empieza desde el deadline y retrocede hasta el tiempo 1
        for t in range(deadline, 0, -1):

            # Verifica si ese espacio de tiempo está libre
            if slots[t] is None:

                # Asigna el trabajo a ese espacio de tiempo
                slots[t] = name

                # Suma la ganancia del trabajo a la ganancia total
                total_profit += profit

                # Guarda el nombre del trabajo en la lista de seleccionados
                seleccionados.append(name)

                # Sale del ciclo porque el trabajo ya fue asignado
                break

    # Retorna la lista de trabajos seleccionados y la ganancia total
    return seleccionados, total_profit


# Lista de trabajos (nombre, deadline, profit)
jobs = [
("J1",2,100),
("J2",1,19),
("J3",2,27),
("J4",1,25),
("J5",3,15)
]

# Ejecuta el algoritmo y muestra el resultado
print(job_scheduling(jobs))

def job_scheduling_deadline(jobs):

    # Ordena los trabajos primero por deadline ascendente
    # y en caso de empate por mayor profit
    jobs = sorted(jobs, key=lambda x: (x[1], -x[2]))

    # Lista para almacenar los trabajos seleccionados
    trabajos_elegidos = []

    # Variable para almacenar la ganancia total
    profit_total = 0

    # Conjunto para registrar qué deadlines ya fueron utilizados
    deadlines_usados = set()

    # Recorre cada trabajo de la lista ordenada
    for id_trabajo, deadline, profit in jobs:

        # Verifica si ese deadline aún no ha sido usado
        if deadline not in deadlines_usados:

            # Agrega el trabajo a la lista de seleccionados
            trabajos_elegidos.append(id_trabajo)

            # Suma la ganancia del trabajo al total
            profit_total += profit

            # Marca ese deadline como utilizado
            deadlines_usados.add(deadline)

    # Retorna los trabajos elegidos y la ganancia total
    return trabajos_elegidos, profit_total


# Lista de trabajos (nombre, deadline, profit)
jobs = [
("J1",2,100),
("J2",1,19),
("J3",2,27),
("J4",1,25),
("J5",3,15)
]

# Ejecuta el algoritmo y muestra el resultado
print(job_scheduling_deadline(jobs))

#=====

"""
Dada una lista de intervalos, combina los que se superponen.

Ejemplo:
    intervalos = [(1,3), (2,6), (8,10), (15,18)]
    Respuesta: [(1,6), (8,10), (15,18)]

    intervalos = [(1,4), (4,5)]
    Respuesta: [(1,5)]  # Se tocan en el punto 4
"""

def solucion_comprimir_intervalos(intervalos):

    # Verifica si la lista de intervalos está vacía
    # Si no hay intervalos, devuelve una lista vacía
    if not intervalos:
        return []
    
    # Ordena los intervalos según el valor de inicio
    # Esto permite comparar intervalos consecutivos fácilmente
    intervalos = sorted(intervalos, key=lambda x: x[0])
    
    # Inicializa la lista resultado con el primer intervalo
    # Se convierte a lista para poder modificar el final si se extiende
    resultado = [list(intervalos[0])]
    
    # Recorre todos los intervalos excepto el primero
    for inicio, fin in intervalos[1:]:

        # Obtiene el último intervalo agregado al resultado
        ultimo = resultado[-1]
        
        # Verifica si el intervalo actual se superpone con el último
        # o si se tocan en el mismo punto
        if inicio <= ultimo[1]:

            # Si se superponen, se extiende el intervalo anterior
            # tomando el máximo entre los dos finales
            ultimo[1] = max(ultimo[1], fin)

        else:
            # Si no se superponen, se agrega un nuevo intervalo
            resultado.append([inicio, fin])
    
    # Convierte los intervalos de lista a tupla antes de retornarlos
    return [tuple(i) for i in resultado]


# Lista de intervalos de ejemplo
intervalos = [(1,3), (2,6), (8,10), (15,18)]

# Llama a la función y muestra el resultado
print(solucion_comprimir_intervalos(intervalos))

#=== 

"""
Una estación de tren tiene trenes que llegan y salen a diferentes horas.
¿Cuál es el MÍNIMO número de plataformas necesarias para que ningún tren tenga que esperar?

Ejemplo:
    llegadas =  [9.00, 9.40, 9.50, 11.00, 15.00, 18.00]
    salidas  =  [9.10, 12.00, 11.20, 11.30, 19.00, 20.00]
    Respuesta: 3 plataformas

Explicación:
A las 11:00 hay 3 trenes simultáneamente en la estación.
"""

def solucion_min_plataformas(llegadas, salidas):

    # Lista donde se guardarán todos los eventos de llegada y salida
    eventos = []

    # Recorre todas las horas de llegada
    for t in llegadas:
        # Agrega un evento de llegada
        # (tiempo, 1) → 1 significa que llega un tren
        eventos.append((t, 1))

    # Recorre todas las horas de salida
    for t in salidas:
        # Agrega un evento de salida
        # (tiempo, -1) → -1 significa que un tren se va
        eventos.append((t, -1))
    
    # Ordena todos los eventos por tiempo
    # Si dos eventos ocurren al mismo tiempo, se procesa primero la salida
    # porque -1 < 1
    eventos.sort(key=lambda x: (x[0], x[1]))
    
    # Variable para contar cuántas plataformas están ocupadas en un momento
    plataformas_actuales = 0

    # Variable para guardar el máximo número de plataformas usadas
    max_plataformas = 0
    
    # Recorre todos los eventos en orden de tiempo
    for tiempo, tipo in eventos:

        # Si llega un tren (+1) aumenta el número de plataformas ocupadas
        # Si sale un tren (-1) disminuye
        plataformas_actuales += tipo

        # Guarda el máximo número de plataformas usadas hasta ahora
        max_plataformas = max(max_plataformas, plataformas_actuales)
    
    # Devuelve el número mínimo de plataformas necesarias
    return max_plataformas


# Lista de horas de llegada de los trenes
llegadas =  [9.00, 9.40, 9.50, 11.00, 15.00, 18.00]

# Lista de horas de salida de los trenes
salidas  =  [9.10, 12.00, 11.20, 11.30, 19.00, 20.00]

# Ejecuta la función y muestra el resultado
print(solucion_min_plataformas(llegadas, salidas))

#=== 

"""
Problema: Número mínimo de salas necesarias

Dada una lista de intervalos de tiempo que representan reuniones
(o actividades), se quiere determinar el número mínimo de salas
necesarias para que todas las reuniones se puedan realizar sin
que se superpongan en la misma sala.

Cada intervalo tiene:
(inicio, fin)

Ejemplo:
intervalos = [(0,30), (5,10), (15,20)]

Explicación:
- La reunión (0,30) ocupa una sala durante todo ese tiempo.
- La reunión (5,10) ocurre mientras la primera sigue en curso.
- La reunión (15,20) también ocurre mientras la primera sigue.

Por lo tanto, en algunos momentos hay 2 reuniones al mismo tiempo,
así que se necesitan al menos 2 salas.
"""

import heapq  # Librería que permite usar una cola de prioridad (min heap)


def min_salas(intervalos):

    # Ordena los intervalos según la hora de inicio
    # Esto permite procesar las reuniones en orden cronológico
    intervalos.sort(key=lambda x: x[0])

    # Heap (cola de prioridad) donde se guardan las horas de finalización
    # de las reuniones que están usando una sala
    heap = []

    # Recorre cada intervalo (reunión)
    for inicio, fin in intervalos:

        # Si el heap no está vacío y la reunión que termina primero
        # termina antes o justo cuando empieza la nueva reunión
        if heap and heap[0] <= inicio:

            # Se libera esa sala (se elimina del heap)
            heapq.heappop(heap)

        # Se asigna una sala a la reunión actual
        # guardando su hora de finalización en el heap
        heapq.heappush(heap, fin)

    # El tamaño del heap representa el número de salas usadas simultáneamente
    # que corresponde al número mínimo de salas necesarias
    return len(heap)

 #Complejidad temporal:
# O(n log n)
# Porque primero se ordenan los intervalos (O(n log n))
# y luego para cada intervalo se realizan operaciones
# en el heap (push y pop) que cuestan O(log n).

# Complejidad espacial:
# O(n)
# porque el heap puede llegar a almacenar hasta n reuniones.

# Decisión local (Greedy):
# Siempre reutilizar la sala que se libera más temprano.
# Es decir, si la reunión que termina primero finaliza antes
# de que empiece la nueva reunión, se reutiliza esa sala.
# Si no, se asigna una nueva sala.

#===
"""
Problema: Problema del cambio (Coin Change) usando algoritmo Greedy

Dado un conjunto de monedas disponibles y un monto a pagar,
el objetivo es devolver el cambio utilizando la menor cantidad
de monedas posible.

El algoritmo greedy consiste en escoger siempre la moneda
de mayor valor posible que no exceda el monto restante.

Ejemplo:
monedas = [1, 5, 10, 25]
monto = 63

Resultado esperado:
[25, 25, 10, 1, 1, 1]

Explicación:
63 = 25 + 25 + 10 + 1 + 1 + 1
"""

def cambio_greedy(monedas, monto):

    # Ordena las monedas de mayor a menor valor
    # Esto permite intentar usar primero las monedas más grandes
    monedas = sorted(monedas, reverse=True)

    # Lista donde se guardarán las monedas utilizadas
    resultado = []

    # Recorre cada tipo de moneda disponible
    for moneda in monedas:

        # Mientras el monto restante sea mayor o igual a la moneda actual
        # se puede usar esa moneda
        while monto >= moneda:

            # Resta el valor de la moneda al monto restante
            monto -= moneda

            # Guarda la moneda usada en la lista resultado
            resultado.append(moneda)

    # Devuelve la lista de monedas utilizadas
    return resultado


# Lista de monedas disponibles
monedas = [1, 5, 10, 25]

# Monto para el cual se quiere dar cambio
monto = 63

# Ejecuta el algoritmo y muestra el resultado
print(cambio_greedy(monedas, monto))


# ---------------- ANÁLISIS DEL ALGORITMO ----------------

# Complejidad temporal:
# O(n + k)
# n = número de tipos de monedas
# k = número de monedas utilizadas en el cambio
# El algoritmo recorre cada tipo de moneda y puede usar varias veces cada moneda.

# Complejidad espacial:
# O(k)
# porque se guarda en la lista resultado cada moneda utilizada.

# Decisión local (Greedy):
# En cada paso se selecciona la moneda de mayor valor posible
# que no supere el monto restante.
# Es decir, siempre se toma la moneda más grande disponible
# antes de considerar monedas más pequeñas.

# ===
"""
Problema: Asignación de tareas a servidores

Dada una lista de tareas donde cada tarea tiene un tiempo de ejecución,
y un número fijo de servidores, el objetivo es asignar las tareas de
forma que la carga de trabajo entre los servidores quede lo más balanceada posible.

El algoritmo usa un heap (cola de prioridad) para siempre asignar la
siguiente tarea al servidor que tenga la menor carga en ese momento.

Ejemplo:
tareas = [2, 5, 4, 7, 1]
servidores = 3

La idea es que cada nueva tarea se asigne al servidor menos ocupado.
"""

import heapq  # Librería para trabajar con colas de prioridad (min heap)


def asignar(tareas, servidores):

    # Crear un heap con los servidores
    # Cada elemento del heap es una tupla (carga_actual, id_servidor)
    # Inicialmente todos los servidores tienen carga 0
    heap = [(0, i) for i in range(servidores)]

    # Convierte la lista en un heap válido
    heapq.heapify(heap)

    # Recorre cada tarea
    for t in tareas:

        # Extrae el servidor con menor carga actual
        carga, id_servidor = heapq.heappop(heap)

        # Calcula la nueva carga del servidor después de asignar la tarea
        nueva_carga = carga + t

        # Vuelve a insertar el servidor en el heap con su nueva carga
        heapq.heappush(heap, (nueva_carga, id_servidor))

    # Devuelve el heap final con las cargas de cada servidor
    return heap


# ---------------- EJEMPLO ----------------

tareas = [2, 5, 4, 7, 1]
servidores = 3

print(asignar(tareas, servidores))


# ---------------- ANÁLISIS DEL ALGORITMO ----------------

# Complejidad temporal:
# O(n log m)
# n = número de tareas
# m = número de servidores
# Para cada tarea se hace un pop y un push en el heap,
# y cada operación en el heap cuesta O(log m).

# Complejidad espacial:
# O(m)
# porque el heap guarda un elemento por cada servidor.

# Decisión local (Greedy):
# Siempre asignar la siguiente tarea al servidor que tenga
# la menor carga en ese momento.
# Es decir, se elige localmente el servidor menos ocupado
# para intentar balancear la carga global del sistema.

#===

"""
Si ves en el problema:

intervalos → ordenar por fin

valor y peso → valor/peso

asignar tareas / servidores → heap

mínimo monedas / mínimo cosas → tomar el mayor posible

mínimo salas → heap de finales

Con eso puedes resolver la mayoría de ejercicios de greedy.
"""
"""
interval scheduling → ordenar por fin
cobertura intervalos → el que llegue más lejos
mochila fraccionaria → valor/peso
servidores → menos cargado
MST → arista más barata sin ciclo
"""

#===

"""
Problema: Maximizar el número de tareas que se pueden realizar antes de su deadline.

Contexto:
Una universidad quiere apagar el mayor número posible de computadoras
para ahorrar energía. Cada computadora necesita un tiempo para apagarse
(duración) y debe terminar antes de un tiempo límite (deadline).

El objetivo es seleccionar la mayor cantidad de tareas que puedan
completarse antes de su deadline.

Cada tarea tiene:
(nombre, duración, deadline)

Ejemplo:
("A", 2, 4) significa:
- Tarea A tarda 2 unidades de tiempo
- Debe terminar antes del tiempo 4
"""

def max_tareas(tareas):

    # Ordena las tareas por su deadline (de menor a mayor)
    # Esto permite priorizar las tareas que vencen primero
    tareas = sorted(tareas, key=lambda x: x[2])

    # Variable que guarda el tiempo total utilizado hasta ahora
    tiempo = 0

    # Lista donde se guardarán las tareas seleccionadas
    resultado = []

    # Recorre cada tarea
    for nombre, duracion, deadline in tareas:

        # Verifica si la tarea puede realizarse antes de su deadline
        if tiempo + duracion <= deadline:

            # Si es posible, se suma su duración al tiempo actual
            tiempo += duracion

            # Se agrega la tarea a la lista de tareas seleccionadas
            resultado.append(nombre)

    # Devuelve la lista de tareas que se pueden realizar
    return resultado


# Lista de tareas (nombre, duración, deadline)
tareas = [
    ("A", 2, 4),   # nombre, tiempo_apagado, deadline
    ("B", 1, 3),
    ("C", 3, 5),
    ("D", 2, 6)
]

# Ejecuta la función y muestra el resultado
print(max_tareas(tareas))


# ---------------- ANÁLISIS DEL ALGORITMO ----------------

# Complejidad temporal:
# O(n log n)
# porque primero se ordenan las tareas por deadline,
# lo cual cuesta O(n log n), y luego se recorren una sola vez O(n).

# Complejidad espacial:
# O(n)
# porque se guarda la lista de tareas seleccionadas.

# Decisión local (Greedy):
# Siempre seleccionar primero la tarea con el deadline más cercano.
# Si una tarea puede realizarse sin violar su deadline,
# se acepta y se actualiza el tiempo total utilizado.
# Esto permite completar la mayor cantidad posible de tareas.

#===

"""
Problema: Colocación mínima de antenas

Dada una lista de ciudades ubicadas en una línea (representadas por
sus posiciones), queremos colocar el menor número de antenas posible
para cubrir todas las ciudades.

Cada antena cubre un rango de 4 unidades a la izquierda y 4 unidades
a la derecha de su posición.

Objetivo:
Cubrir todas las ciudades usando la menor cantidad de antenas.
"""

def antenas(ciudades):

    # Ordena las ciudades de menor a mayor posición
    ciudades.sort()

    # Índice para recorrer las ciudades
    i = 0

    # Número total de ciudades
    n = len(ciudades)

    # Lista donde se guardarán las posiciones de las antenas
    antenas = []

    # Mientras queden ciudades sin cubrir
    while i < n:

        # Tomamos la ciudad más a la izquierda que no esté cubierta
        start = ciudades[i]

        # Colocamos la antena a 4 unidades de esa ciudad
        # para cubrir el mayor rango posible hacia la derecha
        pos = start + 4

        # Guardamos la posición de la antena
        antenas.append(pos)

        # Saltamos todas las ciudades que quedan cubiertas
        # por esta antena (hasta pos + 4)
        while i < n and ciudades[i] <= pos + 4:
            i += 1

    # Retorna las posiciones de las antenas
    return antenas


ciudades = [1,2,3,6,9,11,12]

print(antenas(ciudades))


# ---------------- ANÁLISIS DEL ALGORITMO ----------------

# Complejidad temporal:
# O(n log n)
# porque primero se ordenan las ciudades (O(n log n))
# y luego se recorren una sola vez (O(n)).

# Complejidad espacial:
# O(k)
# donde k es el número de antenas colocadas.

# Decisión local (Greedy):
# Siempre colocar la antena lo más a la derecha posible
# dentro del rango que aún cubre la ciudad más a la izquierda
# que no está cubierta.

"""
Variante del problema de antenas.

En esta versión la antena debe colocarse en la posición
de una ciudad existente, no en cualquier punto.
"""

def colocar_antenas(ciudades):

    # Ordena las ciudades por posición
    ciudades.sort()

    # Número total de ciudades
    n = len(ciudades)

    # Índice para recorrer la lista
    i = 0

    # Lista donde se guardarán las antenas colocadas
    antenas = []

    # Mientras existan ciudades sin cubrir
    while i < n:

        # Ciudad más a la izquierda que no está cubierta
        start = ciudades[i]

        # Avanzamos mientras las ciudades estén dentro
        # del rango start + 4
        while i < n and ciudades[i] <= start + 4:
            i += 1

        # Colocamos la antena en la última ciudad válida
        antena = ciudades[i-1]

        # Guardamos la posición de la antena
        antenas.append(antena)

        # Saltamos todas las ciudades cubiertas
        # por esta antena (antena + 4)
        while i < n and ciudades[i] <= antena + 4:
            i += 1

    # Devuelve las posiciones de las antenas
    return antenas


ciudades = [1,2,3,6,9,11,12]

print(colocar_antenas(ciudades))


# ---------------- ANÁLISIS DEL ALGORITMO ----------------

# Complejidad temporal:
# O(n log n)
# porque se ordenan las ciudades primero (O(n log n))
# y luego se recorren una sola vez (O(n)).

# Complejidad espacial:
# O(k)
# donde k es el número de antenas colocadas.

# Decisión local (Greedy):
# 1. Tomar la ciudad más a la izquierda no cubierta.
# 2. Avanzar hasta la ciudad más a la derecha que aún pueda cubrirla.
# 3. Colocar la antena en esa ciudad.
# 4. Saltar todas las ciudades que quedan cubiertas por esa antena.

"""
Problema: Colocación mínima de radares

Tenemos varias islas ubicadas en coordenadas (x, y).
Los radares se colocan sobre la línea y = 0 (la costa).

Cada radar tiene un alcance máximo d.

Un radar puede cubrir una isla si la distancia entre el radar y la isla
es menor o igual que d.

Objetivo:
Colocar el menor número de radares posible para cubrir todas las islas.
"""

import math  # Librería para usar la raíz cuadrada


def radares(islas, d):

    # Lista donde se guardarán los intervalos donde podría colocarse
    # un radar para cubrir cada isla
    intervalos = []

    # Recorre cada isla
    for x, y in islas:

        # Si la isla está más lejos que el alcance del radar
        # entonces es imposible cubrirla
        if y > d:
            return -1

        # Calcula cuánto se puede mover el radar horizontalmente
        # usando el teorema de Pitágoras
        dx = math.sqrt(d**2 - y**2)

        # Calcula el intervalo de posiciones en la costa
        # donde se puede colocar un radar para cubrir esta isla
        intervalos.append((x - dx, x + dx))

    # Ordena los intervalos por su punto final (derecha)
    # para aplicar la estrategia greedy
    intervalos.sort(key=lambda x: x[1])

    # Lista donde se guardarán las posiciones de los radares
    radares = []

    # Posición del último radar colocado
    pos = -float("inf")

    # Recorre cada intervalo
    for inicio, fin in intervalos:

        # Si la isla actual no está cubierta por el radar anterior
        if inicio > pos:

            # Coloca un nuevo radar en el punto más a la derecha
            # posible de este intervalo
            pos = fin

            # Guarda la posición del radar
            radares.append(pos)

    # Devuelve la lista de posiciones donde se colocaron los radares
    return radares


# Lista de islas (x, y)
islas = [(1,2),(2,4),(5,3),(7,2),(9,1)]

# Alcance del radar
d = 5

# Ejecuta el algoritmo
print(radares(islas,5))


# ---------------- ANÁLISIS DEL ALGORITMO ----------------

# Complejidad temporal:
# O(n log n)
# porque primero se calculan los intervalos O(n)
# luego se ordenan los intervalos O(n log n)
# y finalmente se recorren una vez O(n).

# Complejidad espacial:
# O(n)
# porque se guarda una lista de intervalos y una lista de radares.

# Decisión local (Greedy):
# Colocar cada radar lo más a la derecha posible
# sin perder la cobertura de la isla más restrictiva.
# De esta forma un solo radar puede cubrir la mayor cantidad
# posible de islas siguientes.

"""
Problema: Conectar casas con el menor costo posible (Árbol de Expansión Mínima)

Tenemos varias casas y posibles cables que las pueden conectar.
Cada cable tiene un costo.

Objetivo:
Conectar todas las casas con el menor costo total posible,
sin crear ciclos innecesarios.

Este problema corresponde al algoritmo de Kruskal para
encontrar un Árbol de Expansión Mínima (Minimum Spanning Tree).
"""

def cables_internet(casas, cables):

    # Ordena los cables por costo de menor a mayor
    # para siempre intentar usar primero el cable más barato
    cables.sort(key=lambda x: x[2])
    
    # Diccionario que representa a qué grupo pertenece cada casa
    # inicialmente cada casa está en su propio grupo
    grupos = {c: c for c in casas}
    
    # Lista donde se guardarán los cables seleccionados
    resultado = []

    # Variable que acumula el costo total
    costo_total = 0

    # Recorre todos los cables ordenados por costo
    for casa1, casa2, costo in cables:
        
        # Si las casas pertenecen a grupos diferentes
        # significa que aún no están conectadas
        if grupos[casa1] != grupos[casa2]:
            
            # Guardamos el grupo de la segunda casa
            grupo_viejo = grupos[casa2]
            
            # Unimos los grupos cambiando todas las casas
            # que pertenecían al grupo viejo
            for c in grupos:
                if grupos[c] == grupo_viejo:
                    grupos[c] = grupos[casa1]
            
            # Agregamos el cable seleccionado
            resultado.append((casa1, casa2, costo))

            # Sumamos su costo al costo total
            costo_total += costo

    # Devuelve el costo total y los cables utilizados
    return costo_total, resultado


# Lista de casas
casas = ["A","B","C","D"]

# Lista de cables posibles (casa1, casa2, costo)
cables = [
("A","B",4),
("A","C",2),
("B","C",1),
("B","D",5),
("C","D",8)
]

# Ejecuta el algoritmo
print(cables_internet(casas, cables))


# ---------------- ANÁLISIS DEL ALGORITMO ----------------

# Complejidad temporal:
# O(E log E + E * V)
# donde:
# E = número de cables
# V = número de casas
#
# Primero se ordenan los cables O(E log E)
# Luego, por cada cable se puede recorrer todo el diccionario
# para actualizar grupos O(V)

# Complejidad espacial:
# O(V)
# porque se guarda el diccionario de grupos y la lista de cables seleccionados.

# Decisión local (Greedy):
# Ordenar los cables por costo y seleccionar siempre el más barato
# que conecte dos casas que aún no estén conectadas entre sí.
#
# De esta forma se minimiza el costo total sin crear ciclos,
# siguiendo la estrategia del algoritmo de Kruskal.

"""
Problema: Selección de actividades (Activity Selection Problem)

Se tienen n actividades. Cada actividad tiene:
- un tiempo de inicio (start[i])
- un tiempo de finalización (finish[i])

Una persona solo puede realizar una actividad a la vez.
Una actividad solo puede comenzar si su tiempo de inicio es mayor o
igual al tiempo de finalización de la última actividad realizada.

Objetivo:
Seleccionar el mayor número posible de actividades que no se solapen.

Entrada:
start[]  -> tiempos de inicio
finish[] -> tiempos de finalización

Salida:
- número máximo de actividades
- índices de las actividades seleccionadas
"""

def activity_selection(start, finish):

    # Combina los arreglos en una lista de tuplas:
    # (inicio, fin, índice original)
    actividades = list(zip(start, finish, range(len(start))))

    # Ordena las actividades por su tiempo de finalización (fin)
    # Esto permite seleccionar primero las que terminan antes
    actividades.sort(key=lambda x: x[1])

    # Se selecciona la primera actividad (la que termina primero)
    seleccion = [actividades[0][2]]

    # Guarda el tiempo de finalización de la última actividad elegida
    last_finish = actividades[0][1]

    # Recorre el resto de las actividades
    for s, f, idx in actividades[1:]:

        # Si el inicio de la actividad es mayor o igual
        # al final de la última actividad seleccionada
        if s >= last_finish:

            # Se selecciona esta actividad
            seleccion.append(idx)

            # Se actualiza el tiempo de finalización
            last_finish = f

    # Devuelve:
    # 1) número de actividades seleccionadas
    # 2) lista de índices de esas actividades
    return len(seleccion), seleccion


# ---------------- EJEMPLO ----------------

start = [1,3,0,5,8,5]
finish = [2,4,6,7,9,9]

print(activity_selection(start, finish))


# ---------------- ANÁLISIS DEL ALGORITMO ----------------

# Complejidad temporal:
# O(n log n)
# porque primero se ordenan las actividades por tiempo de finalización
# lo cual cuesta O(n log n), y luego se recorren una sola vez O(n).

# Complejidad espacial:
# O(n)
# porque se crea la lista de actividades y la lista de actividades seleccionadas.

# Decisión local (Greedy):
# Siempre seleccionar la actividad que termine más temprano.
# Esto deja el mayor espacio posible para realizar más actividades después.

"""
Problema: Cubrir una carretera con el menor número de intervalos.

Se tiene una carretera que va desde una posición inicio hasta una
posición fin. También se tiene una lista de intervalos que representan
segmentos de cobertura (por ejemplo cámaras, sensores o tramos de
servicio).

Cada intervalo tiene la forma:
(inicio, fin)

Objetivo:
Seleccionar el menor número de intervalos que cubran completamente
la carretera desde inicio hasta fin.

Estrategia greedy:
Desde la posición actual, elegir el intervalo que empiece antes o igual
y que extienda la cobertura lo más lejos posible.
"""

def cubrir_carretera(intervalos, inicio, fin):

    # Ordena los intervalos por su punto de inicio
    intervalos.sort()

    # Índice para recorrer los intervalos
    i = 0

    # Número total de intervalos
    n = len(intervalos)

    # Posición actual cubierta en la carretera
    posicion = inicio

    # Lista de intervalos seleccionados
    seleccionados = []

    # Mientras aún no se haya cubierto toda la carretera
    while posicion < fin:

        # Guarda el punto más lejano que podemos cubrir
        mejor_fin = posicion

        # Guarda el intervalo que logra esa mejor cobertura
        mejor_intervalo = None

        # Revisar todos los intervalos que comiencen
        # antes o en la posición actual
        while i < n and intervalos[i][0] <= posicion:

            # Si este intervalo llega más lejos que el mejor actual
            if intervalos[i][1] > mejor_fin:

                # Actualizamos la mejor cobertura encontrada
                mejor_fin = intervalos[i][1]

                # Guardamos este intervalo como el mejor
                mejor_intervalo = intervalos[i]

            # Pasamos al siguiente intervalo
            i += 1

        # Si no encontramos ningún intervalo que cubra la posición actual
        # significa que la carretera no se puede cubrir completamente
        if mejor_intervalo is None:
            return None

        # Agregamos el mejor intervalo encontrado
        seleccionados.append(mejor_intervalo)

        # Actualizamos la posición cubierta
        posicion = mejor_fin

    # Devuelve los intervalos seleccionados
    return seleccionados


# ---------------- EJEMPLO ----------------

intervalos = [(0,5),(3,8),(6,10),(9,14),(13,18),(17,20),(4,12)]

print(cubrir_carretera(intervalos,0,20))


# ---------------- ANÁLISIS DEL ALGORITMO ----------------

# Complejidad temporal:
# O(n log n)
# porque primero se ordenan los intervalos O(n log n)
# y luego se recorren una sola vez O(n).
# Aunque hay un while dentro de otro, el índice i solo avanza hacia adelante,
# por lo que cada intervalo se procesa una sola vez.

# Complejidad espacial:
# O(k)
# donde k es el número de intervalos seleccionados.

# Decisión local (Greedy):
# Desde la posición actual, seleccionar el intervalo que empiece antes o igual
# y que extienda la cobertura lo más lejos posible.
# Esto garantiza cubrir la mayor distancia en cada paso.

"""
Problema: Minimizar el número de transportes para barcos

Se tiene una lista de barcos con distintos pesos.
Cada transporte puede cargar como máximo un peso total igual a "capacidad".

Objetivo:
Transportar todos los barcos usando el menor número de transportes posible.

Reglas:
- En cada transporte se pueden llevar uno o dos barcos.
- La suma de sus pesos no puede superar la capacidad máxima.

Estrategia:
Combinar el barco más pesado con el más ligero posible.
"""

def cargar_barcos(pesos, capacidad):

    # Ordena los pesos de menor a mayor
    pesos.sort()

    # i apunta al barco más ligero
    i = 0

    # j apunta al barco más pesado
    j = len(pesos) - 1

    # Lista donde se guardan los transportes realizados
    transportes = []

    # Mientras queden barcos sin transportar
    while i <= j:

        # Si el barco más ligero y el más pesado caben juntos
        if pesos[i] + pesos[j] <= capacidad:

            # Se transportan juntos
            transportes.append((pesos[j], pesos[i]))

            # Avanza el puntero del más ligero
            i += 1

            # Retrocede el puntero del más pesado
            j -= 1

        else:
            # Si no caben juntos, el barco más pesado va solo
            transportes.append((pesos[j],))

            # Solo se mueve el puntero del más pesado
            j -= 1

    # Devuelve la lista de transportes realizados
    return transportes


# ---------------- EJEMPLO ----------------

pesos = [2,3,5,7,4,6]

print(cargar_barcos(pesos,10))


# ---------------- ANÁLISIS DEL ALGORITMO ----------------

# Complejidad temporal:
# O(n log n)
# porque primero se ordenan los pesos O(n log n)
# y luego se recorren con dos punteros una sola vez O(n).

# Complejidad espacial:
# O(n)
# porque se guarda la lista de transportes realizados.

# Decisión local (Greedy):
# Ordenar los pesos y siempre intentar combinar
# el barco más pesado con el más ligero posible
# sin superar la capacidad del transporte.
# Si no es posible, el barco más pesado se transporta solo.

"""
Problema: Asignación de becas

Se tiene una lista de calificaciones de estudiantes.

Solo los estudiantes con nota mayor o igual a 80 pueden recibir beca.

La universidad tiene un número limitado de becas y quiere dárselas
a los estudiantes con mejores calificaciones.

Objetivo:
Seleccionar los estudiantes elegibles con las notas más altas
hasta completar el número de becas disponibles.
"""

def becas(estudiantes, num_becas):

    # Lista donde se guardarán los estudiantes que cumplen el requisito
    elegibles = []

    # Recorrer todas las calificaciones
    for e in estudiantes:

        # Si la nota es mayor o igual a 80, puede optar por beca
        if e >= 80:
            elegibles.append(e)

    # Ordenar las notas elegibles de mayor a menor
    elegibles.sort(reverse=True)

    # Devolver solo la cantidad de estudiantes según el número de becas
    return elegibles[:num_becas]


# ---------------- EJEMPLO ----------------

notas = [95,88,72,60,99,81,77]

print(becas(notas,3))


# ---------------- ANÁLISIS DEL ALGORITMO ----------------

# Complejidad temporal:
# O(n log n)
# porque primero se recorren todas las notas para filtrar los elegibles O(n)
# y luego se ordena la lista de elegibles O(n log n).

# Complejidad espacial:
# O(n)
# porque se crea una lista adicional para guardar los estudiantes elegibles.

# Decisión local (Greedy):
# Elegir siempre primero a los estudiantes con mayor calificación
# para asignar las becas disponibles.

"""
Problema: Ordenar tareas para minimizar penalización

Cada tarea tiene:
(tiempo, penalización)

Si una tarea se retrasa, genera una penalización.
Para reducir la penalización total, se deben ejecutar primero
las tareas que generan mayor penalización.

Objetivo:
Ordenar las tareas para ejecutarlas en un orden que reduzca
la penalización total.
"""

def ordenar_tareas(tareas):

    # Ordena las tareas según la penalización (posición 1 de la tupla)
    # reverse=True hace que se ordenen de mayor a menor penalización
    tareas.sort(key=lambda x: x[1], reverse=True)

    # Devuelve la lista de tareas ya ordenada
    return tareas


# ---------------- EJEMPLO ----------------

tareas = [(2,50),(1,10),(3,60),(2,30)]

print(ordenar_tareas(tareas))


# ---------------- ANÁLISIS DEL ALGORITMO ----------------

# Complejidad temporal:
# O(n log n)
# porque la operación dominante es ordenar las tareas.

# Complejidad espacial:
# O(1)
# porque sort() ordena la lista en el mismo lugar sin crear otra estructura grande.

# Decisión local (Greedy):
# Ejecutar primero las tareas con mayor penalización
# para evitar pagar los costos más altos por retraso.

"""
Problema: Colocar routers WiFi

Se tienen edificios ubicados en distintas posiciones en una calle.

Cada router puede cubrir una distancia de ±rango metros.

Objetivo:
Colocar el menor número de routers posible para cubrir todos los edificios.

Estrategia Greedy:
Desde el edificio más a la izquierda que no esté cubierto,
colocar el router lo más a la derecha posible sin dejar de cubrirlo.
"""

def colocar_wifi(edificios, rango):

    # Ordenar las posiciones de los edificios de menor a mayor
    edificios.sort()

    # Índice para recorrer los edificios
    i = 0

    # Cantidad total de edificios
    n = len(edificios)

    # Lista donde se guardan las posiciones de los routers
    routers = []

    # Mientras aún queden edificios sin cubrir
    while i < n:

        # Tomamos el edificio más a la izquierda que aún no está cubierto
        start = edificios[i]

        # Avanzamos mientras los edificios estén dentro del rango
        # donde aún se podría colocar el router
        while i < n and edificios[i] <= start + rango:
            i += 1

        # Colocamos el router en el edificio más a la derecha posible
        # que todavía cubre al primero
        router = edificios[i-1]

        # Guardamos la posición del router
        routers.append(router)

        # Saltamos todos los edificios que quedan cubiertos por ese router
        while i < n and edificios[i] <= router + rango:
            i += 1

    # Devolver la lista de posiciones donde se colocaron los routers
    return routers


# ---------------- EJEMPLO ----------------

edificios = [2,4,7,10,13,15]

print(colocar_wifi(edificios,2))


# ---------------- ANÁLISIS DEL ALGORITMO ----------------

# Complejidad temporal:
# O(n log n)
# porque primero se ordenan los edificios O(n log n)
# y luego se recorren una sola vez con el índice i O(n).

# Complejidad espacial:
# O(n)
# porque se guarda la lista de routers colocados.

# Decisión local (Greedy):
# Desde el edificio más a la izquierda no cubierto,
# colocar el router lo más a la derecha posible
# para cubrir la mayor cantidad de edificios con un solo router.

"""
Problema: Empaquetar cajas en contenedores

Se tiene una lista de cajas con diferentes volúmenes.

Cada contenedor tiene una capacidad máxima.

Objetivo:
Usar el menor número de contenedores posible para transportar todas las cajas.

Estrategia:
Intentar combinar la caja más grande con la más pequeña posible
sin superar la capacidad del contenedor.
"""

# Ordenar cajas y llenar cada contenedor con la combinación
# que más se acerque a la capacidad.
def empaquetar(cajas, capacidad):

    # Ordenar las cajas de menor a mayor volumen
    cajas.sort()

    # i apunta a la caja más pequeña
    i = 0

    # j apunta a la caja más grande
    j = len(cajas) - 1

    # Lista donde se guardan los contenedores usados
    contenedores = []

    # Mientras aún queden cajas por empaquetar
    while i <= j:

        # Si la caja más pequeña y la más grande caben juntas
        if cajas[i] + cajas[j] <= capacidad:

            # Se colocan juntas en el mismo contenedor
            contenedores.append((cajas[j], cajas[i]))

            # Avanza al siguiente más pequeño
            i += 1

            # Retrocede al siguiente más grande
            j -= 1

        else:
            # Si no caben juntas, la caja más grande va sola
            contenedores.append((cajas[j],))

            # Solo se mueve el puntero del más grande
            j -= 1

    # Devuelve la lista de contenedores usados
    return contenedores


# ---------------- EJEMPLO ----------------

cajas = [4,8,1,4,2,1]

print(empaquetar(cajas,10))


# ---------------- ANÁLISIS DEL ALGORITMO ----------------

# Complejidad temporal:
# O(n log n)
# porque primero se ordenan las cajas O(n log n)
# y luego se recorren una sola vez con dos punteros O(n).

# Complejidad espacial:
# O(n)
# porque se guarda la lista de contenedores utilizados.

# Decisión local (Greedy):
# Ordenar las cajas y combinar siempre la caja más grande
# con la más pequeña posible sin superar la capacidad
# para aprovechar mejor cada contenedor.

"""
Problema: Minimizar el número de viajes

Se tienen paquetes con diferentes pesos.

Ejemplo:
[1, 2, 3, 4, 5]

Un camión puede transportar como máximo cierta capacidad de peso
en cada viaje.

Objetivo:
Minimizar el número de viajes necesarios para transportar todos
los paquetes sin superar la capacidad del camión en cada viaje.

Estrategia Greedy:
Combinar el paquete más pesado con el más ligero posible
para aprovechar al máximo la capacidad en cada viaje.
"""

def min_viajes(paquetes, capacidad):

    # Ordenar los paquetes de menor a mayor peso
    paquetes.sort()

    # i apunta al paquete más ligero
    i = 0

    # j apunta al paquete más pesado
    j = len(paquetes) - 1

    # Contador de viajes realizados
    viajes = 0

    # Mientras aún queden paquetes sin transportar
    while i <= j:

        # Si el paquete más ligero y el más pesado caben juntos
        if paquetes[i] + paquetes[j] <= capacidad:

            # Se transporta también el paquete ligero
            i += 1

        # El paquete más pesado siempre se transporta en este viaje
        j -= 1

        # Se cuenta un nuevo viaje
        viajes += 1

    # Devuelve el número mínimo de viajes
    return viajes


# ---------------- EJEMPLO ----------------

print(min_viajes([1,2,3,4,5],7))


# ---------------- ANÁLISIS DEL ALGORITMO ----------------

# Complejidad temporal:
# O(n log n)
# porque primero se ordenan los paquetes O(n log n)
# y luego se recorren una sola vez con dos punteros O(n).

# Complejidad espacial:
# O(1)
# porque solo se usan variables auxiliares.

# Decisión local (Greedy):
# En cada viaje transportar el paquete más pesado posible
# y combinarlo con el paquete más ligero que aún quepa
# para aprovechar al máximo la capacidad del camión.

"""
Problema: Cubrir una carretera con estaciones

Una carretera va desde el km 0 hasta el km 20.

Existen estaciones de servicio que cubren ciertos intervalos
de la carretera.

Ejemplo de intervalos:
(0,5)
(3,9)
(6,12)
(10,15)
(14,20)
(8,18)

Objetivo:
Usar el menor número de estaciones para cubrir toda la carretera
desde el inicio hasta el final.
"""

def cubrir_carretera(intervalos, inicio, fin):

    # Ordenar los intervalos según su punto de inicio
    intervalos.sort()

    # Índice para recorrer los intervalos
    i = 0

    # Número total de intervalos
    n = len(intervalos)

    # Posición actual cubierta de la carretera
    actual = inicio

    # Lista donde se guardan los intervalos utilizados
    usados = []

    # Mientras aún no se cubra toda la carretera
    while actual < fin:

        # Variable que guarda el punto más lejano que podemos cubrir
        mejor = actual

        # Revisar todos los intervalos que comienzan antes o en la posición actual
        while i < n and intervalos[i][0] <= actual:

            # Elegir el intervalo que llegue más lejos
            mejor = max(mejor, intervalos[i][1])

            # Pasar al siguiente intervalo
            i += 1

        # Si no encontramos ningún intervalo que extienda la cobertura
        # significa que no es posible cubrir toda la carretera
        if mejor == actual:
            return []

        # Guardamos hasta dónde se extendió la cobertura
        usados.append(mejor)

        # Actualizamos la posición cubierta
        actual = mejor

    # Devolver los puntos hasta donde se extendió cada estación usada
    return usados


# ---------------- EJEMPLO ----------------

intervalos = [(0,5),(3,9),(6,12),(10,15),(14,20),(8,18)]

print(cubrir_carretera(intervalos,0,20))


# ---------------- ANÁLISIS DEL ALGORITMO ----------------

# Complejidad temporal:
# O(n log n)
# porque primero se ordenan los intervalos O(n log n)
# y luego se recorren una sola vez O(n).

# Complejidad espacial:
# O(n)
# porque se guarda la lista de estaciones utilizadas.

# Decisión local (Greedy):
# Desde la posición actual elegir el intervalo que empiece antes
# o igual y que extienda la cobertura lo más lejos posible.
# Así se minimiza el número total de estaciones utilizadas.

"""
Problema: Fusión de archivos con costo mínimo

Se tienen varios archivos con diferentes tamaños.

Ejemplo:
[5, 2, 4, 7, 1]

Para fusionar dos archivos, el costo es la suma de sus tamaños.

Después de fusionarlos, se obtiene un nuevo archivo cuyo tamaño
también es esa suma.

Objetivo:
Fusionar todos los archivos minimizando el costo total de fusiones.
"""

import heapq

def costo_minimo_fusion(archivos):

    # Convertir la lista en un min-heap
    # Esto permite obtener siempre el archivo más pequeño rápidamente
    heapq.heapify(archivos)

    # Variable para acumular el costo total de todas las fusiones
    costo_total = 0

    # Mientras haya más de un archivo para fusionar
    while len(archivos) > 1:

        # Extraer el archivo más pequeño
        a = heapq.heappop(archivos)

        # Extraer el segundo archivo más pequeño
        b = heapq.heappop(archivos)

        # Calcular el costo de fusionarlos
        costo = a + b

        # Sumar ese costo al costo total
        costo_total += costo

        # El nuevo archivo resultante vuelve al heap
        heapq.heappush(archivos, costo)

    # Devolver el costo total mínimo de todas las fusiones
    return costo_total


# ---------------- EJEMPLO ----------------

print(costo_minimo_fusion([5,2,4,7,1]))


# ---------------- ANÁLISIS DEL ALGORITMO ----------------

# Complejidad temporal:
# O(n log n)
# porque cada operación de extracción o inserción en el heap cuesta O(log n)
# y se realizan aproximadamente n fusiones.

# Complejidad espacial:
# O(n)
# porque el heap almacena los tamaños de los archivos.

# Decisión local (Greedy):
# Siempre fusionar primero los dos archivos más pequeños
# para minimizar el costo acumulado de todas las fusiones.

"""
Problema: Asignación de tareas a servidores

Se tienen tareas con diferentes duraciones.

Ejemplo:
[8, 5, 4, 3, 2, 1]

Hay varios servidores que pueden ejecutar tareas.

Reglas:
- Cada tarea debe ejecutarse completa en un solo servidor.
- Un servidor puede ejecutar varias tareas, pero una a la vez.

Objetivo:
Minimizar el tiempo en el que termina el último servidor
(es decir, balancear la carga entre servidores).
"""

import heapq

def asignar_tareas(tareas, servidores):

    # Ordenar las tareas de mayor a menor duración
    # Así asignamos primero las tareas más largas
    tareas.sort(reverse=True)

    # Crear un heap donde cada elemento es:
    # (carga_actual_del_servidor, id_del_servidor)
    heap = [(0,i) for i in range(servidores)]

    # Convertir la lista en un min-heap
    heapq.heapify(heap)

    # Recorrer todas las tareas
    for t in tareas:

        # Sacar el servidor que tenga menor carga actualmente
        carga, id_servidor = heapq.heappop(heap)

        # Asignar la tarea a ese servidor
        # La nueva carga será la carga actual más la duración de la tarea
        heapq.heappush(heap, (carga + t, id_servidor))

    # Devuelve el estado final de los servidores
    return heap


# ---------------- EJEMPLO ----------------

print(asignar_tareas([8,5,4,3,2,1],3))


# ---------------- ANÁLISIS DEL ALGORITMO ----------------

# Complejidad temporal:
# O(n log m)
# donde:
# n = número de tareas
# m = número de servidores
#
# porque cada tarea implica una extracción y una inserción en el heap,
# y cada operación cuesta O(log m).

# Complejidad espacial:
# O(m)
# porque el heap almacena solo los servidores.

# Decisión local (Greedy):
# Asignar siempre la siguiente tarea al servidor que tenga
# la menor carga en ese momento para balancear el trabajo
# y minimizar el tiempo final de ejecución.

"""
Una empresa de transporte tiene un camión con capacidad limitada de carga (capacity). Debes transportar una selección de n objetos, cada uno con:

val[i]: el valor asociado al objeto.
wt[i]: el peso del objeto.
📌 Restricciones:

No se puede exceder la capacidad total de la mochila.
A diferencia del problema clásico de 0/1 Knapsack, aquí puedes tomar fracciones de un objeto.
🎯 Objetivo: Determinar el valor máximo total que se puede obtener llenando la mochila.

📥 Entrada
val[]: arreglo de enteros que representa el valor de cada objeto.
wt[]: arreglo de enteros que representa el peso de cada objeto.
capacity: entero que representa la capacidad máxima de la mochila.
📤 Salida
Un número real que representa el valor máximo total alcanzable, permitiendo tomar objetos completos o fracciones.
✅ Ejemplos
Ejemplo 1 val = [60, 100, 120] wt = [10, 20, 30] capacity = 50 Salida: 240

Explicación:

Tomamos los objetos de 10kg y 20kg completos.
Tomamos 2/3 del objeto de 30kg.
Valor total = 60 + 100 + (2/3 × 120) = 240.
"""

def mochilla(capacidad= int, valor =[],peso =[]):
    contador_valor = 0
    contador_peso =0
    for i in range(len(valor)):
        contador_valor += valor[i]
        contador_peso += peso[i]

        if contador_peso > capacidad:
            contador_valor -= valor[i]
            contador_peso -= peso[i]
            restante = capacidad - contador_peso
            fraccion = restante / peso[i]
            contador_valor += valor[i]*fraccion
            return contador_valor
        elif contador_peso == capacidad:
            return contador_valor 
    return contador_valor

valor = [60,100,120]
peso = [10,20,30]
capacidad = 50
print(mochilla(capacidad,valor,peso))

"""
Problema: Mochila fraccionaria

Se tienen objetos con:
(peso, valor)

Ejemplo:
(4,20)
(2,14)
(6,30)
(3,18)

La mochila tiene una capacidad máxima.

A diferencia de la mochila clásica, aquí se pueden tomar
fracciones de los objetos.

Objetivo:
Maximizar el valor total dentro de la mochila.
"""

def mochila_fraccionaria(capacidad, objetos):

    # Ordenar los objetos según su relación valor/peso
    # (valor por unidad de peso), de mayor a menor
    objetos.sort(key=lambda x: x[1]/x[0], reverse=True)

    # Variable para acumular el valor total en la mochila
    valor_total = 0

    # Recorrer todos los objetos
    for peso, valor in objetos:

        # Si el objeto completo cabe en la mochila
        if capacidad >= peso:

            # Reducir la capacidad disponible
            capacidad -= peso

            # Sumar su valor completo
            valor_total += valor

        else:
            # Si no cabe completo, tomar solo la fracción posible
            valor_total += valor * (capacidad/peso)

            # La mochila queda llena, se termina el proceso
            break

    # Devolver el valor máximo obtenido
    return valor_total


# ---------------- EJEMPLO ----------------

objetos = [(4,20),(2,14),(6,30),(3,18)]

print(mochila_fraccionaria(10, objetos))


# ---------------- ANÁLISIS DEL ALGORITMO ----------------

# Complejidad temporal:
# O(n log n)
# porque primero se ordenan los objetos según valor/peso.

# Complejidad espacial:
# O(1)
# porque solo se usan variables auxiliares.

# Decisión local (Greedy):
# Elegir primero el objeto con mayor relación valor/peso
# para obtener el mayor valor posible por cada unidad
# de capacidad de la mochila.

"""
Problema: Selección de anuncios sin superposición

Una empresa quiere transmitir anuncios en televisión.

Cada anuncio tiene un intervalo de tiempo:
(inicio, fin)

Ejemplo:
(1,4)
(2,6)
(4,7)
(6,9)
(8,10)

Regla:
Los anuncios no pueden superponerse.

Objetivo:
Transmitir la mayor cantidad posible de anuncios.
"""

def max_anuncios(intervalos):

    # Ordenar los intervalos según su tiempo de finalización
    # Esto permite elegir primero los anuncios que terminan antes
    intervalos.sort(key=lambda x: x[1])

    # Lista donde se guardarán los anuncios seleccionados
    seleccionados = []

    # Variable que guarda el tiempo de finalización del último anuncio elegido
    ultimo_fin = -float('inf')

    # Recorrer todos los intervalos
    for inicio, fin in intervalos:

        # Si el anuncio comienza después o justo cuando termina el anterior
        if inicio >= ultimo_fin:

            # Se puede transmitir este anuncio
            seleccionados.append((inicio, fin))

            # Actualizar el tiempo de finalización
            ultimo_fin = fin

    # Devolver los anuncios seleccionados
    return seleccionados


# ---------------- EJEMPLO ----------------

intervalos = [(1,4),(2,6),(4,7),(6,9),(8,10)]

print(max_anuncios(intervalos))


# ---------------- ANÁLISIS DEL ALGORITMO ----------------

# Complejidad temporal:
# O(n log n)
# porque primero se ordenan los intervalos por tiempo de finalización.

# Complejidad espacial:
# O(n)
# porque se guarda la lista de anuncios seleccionados.

# Decisión local (Greedy):
# Elegir siempre el anuncio que termine más temprano
# para dejar el mayor espacio posible para anuncios futuros.

"""
Problema: Conectar cuerdas con costo mínimo

Se tiene un arreglo con las longitudes de varias cuerdas.

Ejemplo:
[4, 3, 2, 6]

Regla:
El costo de unir dos cuerdas es la suma de sus longitudes.

Después de unirlas, la nueva cuerda puede volver a usarse
para conectarse con otra.

Objetivo:
Conectar todas las cuerdas en una sola minimizando el costo total.
"""

import heapq

def conectar_cuerdas(arr):

    # Convertir la lista en un min-heap
    # Esto permite obtener rápidamente las dos cuerdas más pequeñas
    heapq.heapify(arr)

    # Variable para acumular el costo total
    total_cost = 0

    # Mientras haya más de una cuerda
    while len(arr) > 1:

        # Sacar la cuerda más pequeña
        a = heapq.heappop(arr)

        # Sacar la segunda cuerda más pequeña
        b = heapq.heappop(arr)

        # Calcular el costo de unirlas
        cost = a + b

        # Sumar ese costo al total
        total_cost += cost

        # Insertar la nueva cuerda resultante al heap
        heapq.heappush(arr, cost)

    # Devolver el costo mínimo total
    return total_cost


# ---------------- EJEMPLO ----------------

arr = [4,3,2,6]

print(conectar_cuerdas(arr))


# ---------------- ANÁLISIS DEL ALGORITMO ----------------

# Complejidad temporal:
# O(n log n)
# porque cada operación de extracción o inserción en el heap
# cuesta O(log n) y se realizan aproximadamente n fusiones.

# Complejidad espacial:
# O(n)
# porque el heap almacena las cuerdas.

# Decisión local (Greedy):
# Siempre conectar primero las dos cuerdas más pequeñas
# para minimizar el costo acumulado de todas las conexiones.

"""
Problema: Coincidencia de patrón con comodines

Se tienen dos cadenas:
s → cadena de entrada
p → patrón

Reglas de coincidencia:

?  coincide con exactamente un carácter cualquiera
*  coincide con cualquier secuencia de caracteres (incluso vacía)

La coincidencia debe cubrir TODA la cadena.

Ejemplos:
s = "aa", p = "a"  → False
s = "aa", p = "*"  → True
s = "cb", p = "?a" → False
"""

def coincide_patron(cadena, patron):

    # Puntero para recorrer la cadena
    posicion_cadena = 0

    # Puntero para recorrer el patrón
    posicion_patron = 0

    # Guarda la última posición donde apareció '*'
    posicion_estrella = -1

    # Guarda la posición en la cadena donde comenzó la coincidencia con '*'
    coincidencia = 0

    # Recorrer la cadena
    while posicion_cadena < len(cadena):

        # Caso 1: los caracteres coinciden o el patrón tiene '?'
        if (posicion_patron < len(patron) and
            (patron[posicion_patron] == cadena[posicion_cadena] or
             patron[posicion_patron] == '?')):

            # Avanzar en ambas cadenas
            posicion_cadena += 1
            posicion_patron += 1

        # Caso 2: encontramos '*'
        elif posicion_patron < len(patron) and patron[posicion_patron] == '*':

            # Guardamos la posición de la estrella
            posicion_estrella = posicion_patron

            # Guardamos la posición actual en la cadena
            coincidencia = posicion_cadena

            # Avanzamos en el patrón
            posicion_patron += 1

        # Caso 3: hubo una estrella antes y podemos intentar extenderla
        elif posicion_estrella != -1:

            # Volvemos al carácter después de '*'
            posicion_patron = posicion_estrella + 1

            # Extendemos lo que cubre la estrella
            coincidencia += 1

            # Avanzamos en la cadena
            posicion_cadena = coincidencia

        # Caso 4: no hay coincidencia posible
        else:
            return False

    # Saltar estrellas restantes en el patrón
    while posicion_patron < len(patron) and patron[posicion_patron] == '*':
        posicion_patron += 1

    # Si llegamos al final del patrón, hay coincidencia
    return posicion_patron == len(patron)


# ---------------- EJEMPLO ----------------

cadena = "aa"
patron = "*"

print(coincide_patron(cadena, patron))


# ---------------- ANÁLISIS DEL ALGORITMO ----------------

# Complejidad temporal:
# O(n)
# donde n es la longitud de la cadena.
# Cada carácter se procesa como máximo unas pocas veces
# gracias al manejo de la posición de '*'.

# Complejidad espacial:
# O(1)
# porque solo se utilizan variables auxiliares.

# Decisión local (Greedy):
# Cuando aparece '*', inicialmente se asume que coincide con
# la menor cantidad posible de caracteres y solo se expande
# si es necesario para que el resto del patrón coincida.

"""
Problema: Jump Game (alcanzar el final del arreglo)

Se tiene un arreglo de números enteros no negativos.

Cada posición indica la longitud máxima de salto que puedes hacer
desde ese índice.

Ejemplo:
nums = [2,3,1,1,4]

Desde el índice 0 puedes saltar hasta 2 posiciones.
Desde el índice 1 puedes saltar hasta 3 posiciones.

Objetivo:
Determinar si es posible llegar o sobrepasar el último índice del arreglo.
"""

def puede_llegar_final(numeros):

    # Guarda el índice más lejano al que podemos llegar
    alcance_maximo = 0

    # Recorrer el arreglo
    for indice in range(len(numeros)):

        # Si el índice actual está más allá del alcance máximo
        # significa que no podemos llegar a esta posición
        if indice > alcance_maximo:
            return False

        # Actualizar el alcance máximo posible
        # indice + numeros[indice] indica hasta dónde podemos saltar
        alcance_maximo = max(alcance_maximo, indice + numeros[indice])

    # Si nunca encontramos una posición inaccesible,
    # entonces sí podemos llegar al final
    return True


# ---------------- EJEMPLO ----------------

numeros = [2,3,1,1,4]

print(puede_llegar_final(numeros))


# ---------------- ANÁLISIS DEL ALGORITMO ----------------

# Complejidad temporal:
# O(n)
# porque se recorre el arreglo una sola vez.

# Complejidad espacial:
# O(1)
# porque solo se utilizan variables auxiliares.

# Decisión local (Greedy):
# En cada posición mantener el alcance máximo posible
# y actualizarlo con el salto disponible en esa posición.
# Si en algún momento el índice actual supera ese alcance,
# significa que no es posible continuar.

"""
Problema: Máximo número de reuniones

Eres un gerente y tienes varias reuniones propuestas para hoy.
Cada reunión tiene una hora de inicio y una hora de fin.

No puedes asistir a dos reuniones al mismo tiempo.

Objetivo:
Asistir al mayor número posible de reuniones sin que se superpongan.

Ejemplo:
reuniones = [(9, 10), (9, 12), (10, 11), (11, 13), (12, 14)]
Respuesta posible:
[(9, 10), (10, 11), (12, 14)]
"""

def solucion_max_reuniones(reuniones):

    # Si no hay reuniones, devolver lista vacía
    if not reuniones:
        return []
    
    # Ordenar las reuniones según su hora de finalización
    # Esto permite elegir primero las reuniones que terminan antes
    reuniones_ordenadas = sorted(reuniones, key=lambda x: x[1])
    
    # Seleccionar la primera reunión (la que termina más temprano)
    seleccionadas = [reuniones_ordenadas[0]]

    # Guardar la hora en que termina la última reunión seleccionada
    ultimo_fin = reuniones_ordenadas[0][1]
    
    # Recorrer el resto de reuniones
    for inicio, fin in reuniones_ordenadas[1:]:

        # Si la reunión empieza después o justo cuando termina la anterior
        if inicio >= ultimo_fin:

            # Se puede asistir a esta reunión
            seleccionadas.append((inicio, fin))

            # Actualizar el tiempo de finalización
            ultimo_fin = fin
    
    # Devolver las reuniones seleccionadas
    return seleccionadas


# ---------------- EJEMPLO ----------------

reuniones = [(9, 10), (9, 12), (10, 11), (11, 13), (12, 14)]

print(solucion_max_reuniones(reuniones))


# ---------------- ANÁLISIS DEL ALGORITMO ----------------

# Complejidad temporal:
# O(n log n)
# porque primero se ordenan las reuniones por su tiempo de finalización.

# Complejidad espacial:
# O(n)
# porque se guarda la lista de reuniones seleccionadas.

# Decisión local (Greedy):
# Elegir siempre la reunión que termine más temprano
# para dejar el mayor espacio posible para reuniones futuras.

"""

HOJA RÁPIDA – PATRONES GREEDY PARA EXAMEN

Regla general Greedy
1. Ordenar los datos si es necesario
2. Elegir la mejor opción local
3. Actualizar el estado del problema
4. Repetir hasta terminar

--------------------------------------------------

1. Activity Selection (Intervalos / Reuniones / Anuncios)

Problema:
Maximizar el número de actividades sin solaparse.

Decisión Greedy:
Elegir siempre la actividad que termina primero.

Pasos:
1. Ordenar por tiempo de finalización
2. Seleccionar la primera actividad
3. Elegir la siguiente cuyo inicio sea >= al último fin

Complejidad:
O(n log n)

--------------------------------------------------

2. Mochila Fraccionaria

Problema:
Maximizar el valor dentro de una capacidad limitada.

Decisión Greedy:
Elegir primero el objeto con mayor relación valor/peso.

Pasos:
1. Calcular valor/peso
2. Ordenar descendente por esa relación
3. Tomar el objeto completo o la fracción posible

Complejidad:
O(n log n)

--------------------------------------------------

3. Conectar cuerdas / Fusionar archivos

Problema:
Minimizar el costo total de fusiones.

Decisión Greedy:
Siempre combinar los dos elementos más pequeños.

Estructura usada:
Min Heap (heapq)

Proceso:
1. Convertir lista en heap
2. Sacar los dos menores
3. Sumarlos
4. Insertar el resultado nuevamente

Complejidad:
O(n log n)

--------------------------------------------------

4. Jump Game

Problema:
Determinar si se puede llegar al final del arreglo.

Decisión Greedy:
Mantener el mayor alcance posible en cada posición.

Idea clave:
alcance_max = max(alcance_max, indice + salto)

Si indice > alcance_max → no se puede llegar.

Complejidad:
O(n)

--------------------------------------------------

5. Interval Covering (Cubrir carretera)

Problema:
Cubrir un rango usando el menor número de intervalos.

Decisión Greedy:
Elegir el intervalo que empiece antes o igual al punto actual
y que llegue más lejos.

Proceso:
1. Ordenar intervalos
2. Desde la posición actual buscar el que más se extienda
3. Avanzar hasta ese punto

Complejidad:
O(n log n)

--------------------------------------------------

6. Emparejar pesado con ligero (contenedores / barcos / viajes)

Problema:
Minimizar el número de contenedores o viajes.

Decisión Greedy:
Combinar el objeto más pesado con el más ligero posible.

Técnica:
Dos punteros.

Proceso:
1. Ordenar la lista
2. i = ligero
3. j = pesado
4. Si caben juntos → mover ambos
5. Si no → mover solo el pesado

Complejidad:
O(n log n)

--------------------------------------------------

7. Asignación de tareas a servidores

Problema:
Minimizar el tiempo en que termina el último servidor.

Decisión Greedy:
Asignar cada tarea al servidor menos ocupado.

Estructura usada:
Min Heap.

Proceso:
1. Ordenar tareas
2. Extraer servidor con menor carga
3. Asignar tarea
4. Volver a insertar con nueva carga

Complejidad:
O(n log m)

m = número de servidores

--------------------------------------------------

Estructuras que aparecen frecuentemente en Greedy

sort() → ordenar intervalos o valores
heap / heapq → mínimos o fusiones
dos punteros → emparejar pesos
recorrido simple → máximo alcance
valor/peso → mochila

--------------------------------------------------

Regla rápida para reconocer Greedy en un examen

Si el problema dice:

- máximo número
- mínimo costo
- mínimo número
- maximizar valor
- intervalos
- asignar tareas
- fusionar elementos

es muy probable que sea Greedy.

--------------------------------------------------

Patrón mental para construir un algoritmo Greedy

1 ordenar
2 elegir la mejor decisión local
3 actualizar estado
4 repetir

"""
"""

CONSEJOS CLAVE PARA RESOLVER GREEDY EN EXAMEN

1. Primero piensa si el problema se puede ordenar
Muchísimos algoritmos Greedy empiezan ordenando.

Si ves:
- intervalos
- pesos
- tiempos
- valores
- tareas

Probablemente el primer paso es:

sort()

--------------------------------------------------

2. Identifica la decisión local

Greedy siempre toma una decisión local óptima.

Pregúntate:

¿Qué decisión parece mejor en ESTE momento?

Ejemplos típicos:

intervalos → terminar primero
mochila → mayor valor/peso
cuerdas → dos más pequeños
servidores → menor carga
barcos → pesado + ligero
jump game → mayor alcance

Si encuentras esa regla → ya tienes el algoritmo.

--------------------------------------------------

3. Muchos problemas Greedy tienen estas estructuras

sort()
heap
dos punteros
for simple

Si ves estas estructuras, probablemente es Greedy.

--------------------------------------------------

4. Si puedes resolver el problema avanzando sin retroceder

Greedy casi siempre:

- recorre una vez
- no vuelve atrás
- no prueba muchas combinaciones

Eso significa que probablemente es O(n) o O(n log n).

--------------------------------------------------

5. Si necesitas probar todas las combinaciones NO es Greedy

Si el problema requiere:

- probar todas las opciones
- backtracking
- programación dinámica

Entonces NO es Greedy.

--------------------------------------------------

6. En muchos parciales Greedy siempre empieza así

datos.sort()

Luego:

for elemento in datos:

Esto ya te da media solución.

--------------------------------------------------

7. Complejidades típicas de Greedy

Si hay sort:

O(n log n)

Si hay heap:

O(n log n)

Si es recorrido simple:

O(n)

Muy raro que sea O(n²).

--------------------------------------------------

8. Cómo justificar la decisión Greedy en un examen

Puedes escribir algo como:

"La estrategia greedy consiste en elegir en cada paso la opción
que optimiza el criterio local del problema, lo que conduce
a una solución global óptima."

O algo más simple:

"En cada paso elegimos la opción que produce el mejor resultado inmediato."

--------------------------------------------------

9. Si te bloqueas en el examen

Usa esta receta:

1 ordenar datos
2 elegir mejor opción local
3 actualizar estado
4 repetir hasta terminar

Esto funciona en la mayoría de problemas Greedy.

--------------------------------------------------

10. Tip que usan mucho los profesores

Muchos problemas Greedy en parciales son variaciones de:

- Activity Selection
- Mochila Fraccionaria
- Conectar Cuerdas
- Jump Game
- Interval Covering
- Barcos / Contenedores
- Scheduling de tareas

Si reconoces uno de estos patrones,
puedes adaptar la solución rápidamente.

"""